from django.shortcuts import render
import sys
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
# from .models import Home, About, Pricing, Feedback, Faqs


# Local import
from dashboard.models import *

# Create your views here.
from gspread import service_account
import environ

env = environ.Env()
environ.Env.read_env()  # Assuming you have a .env file with credentials

def home(request):
    homes = Home.objects.all()
    # about = About.objects.all()
    pricing = Pricing.objects.all().order_by('id')
    feedback = Feedback.objects.all()
    faqs = Faqs.objects.all()
    coverage = Coverage.objects.all()

    context = {
        'homes': homes,
        # 'about': about,
        'pricing': pricing,
        'feedback': feedback,
        'faqs': faqs,
        'coverage': coverage
    }
    return render(request, '../templates/ftth/home.html', context=context)


def contact(request):
    context = {}
    return render(request, 'ftth/contact.html', context)
    
def update_google_sheet(data, sheet_id):
    gc = service_account(filename=env('GOOGLE_APPLICATION_CREDENTIALS'))
    sheet = gc.open_by_key(sheet_id).sheet1
    sheet.append_row(data)
    return JsonResponse({"message": "Success"}, status=200)
    

def plan(request, id):
    pricing = Pricing.objects.all().order_by('id')
    context = {
        'plan_id': id,
        'prices': pricing,
    }
    if request.method == 'POST':
        subject = "New Campaign lead "
        name = request.POST["fullname"]
        email = request.POST["email"]
        msg = f'You have a new request. kindly update on Odoo.'
        msg += f'\nDetails:\n'
        msg += f'Name: {request.POST["fullname"]}\n'
        msg += f'Phone: {request.POST["phone"]}\n'
        msg += f'Email: {request.POST["email"]}\n'
        msg += f'Address: {request.POST["address"]}\n'
        msg += f'Plan interested in: {request.POST["product"]}\n'
        msg += f'Home type: {request.POST["home_type"]}\n'

        recipient_list = ['salesunit@layer3.com.ng', 'john.onuorah@amplify.ng']
        # recipient_list = ['wisdom.george@layer3.com.ng', 'wisgeorge.wg@gmail.com']

        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list= recipient_list,
        )

        # Construct the data dictionary for Google Sheet
        data = {
            'Name': request.POST["fullname"],
            'Phone': request.POST["phone"],
            'Email': request.POST["email"],
            'Address': request.POST["product"],
            'Plan interested in': request.POST["home_type"],
            'Home type': request.POST["address"],
        }

        # Update Google Sheet
        update_google_sheet(list(data.values()), env('GOOGLE_SHEET_ID'))

        messages.success(request, 'Service request submitted successfully.')
        return render(request, 'ftth/plan.html', context)

    return render(request, 'ftth/plan.html', context)

def getlocation(request):
    if request.is_ajax and request.method == "GET":
    # if request.headers.get('X-Requested-With') == 'XMLHttpRequest' and request.method == "GET":
        location_id = request.GET.get("location_id", None)
        location = Coverage.objects.filter(id=location_id).values()

        client_name = request.GET.get("client_name", None)
        client_email = request.GET.get("client_email", None)
        client_phone = request.GET.get("client_phone", None)

        subject = "New Campaign lead"
        msg = f'You have a new Service Enquiry. kindly update on Odoo.'
        msg += f'{client_name} will like to know if {location[0]["coverage_name"]} is within our area of coverage\n\n'
        msg += f'See the details below:\n'
        msg += f'Phone: {client_phone}\n'
        msg += f'Email: {client_email}\n\n'
        msg += f'Thank You!'

        recipient_list = ['salesunit@layer3.com.ng', 'john.onuorah@amplify.ng']
        # recipient_list = ['wisdom.george@layer3.com.ng', 'wisgeorge.wg@gmail.com']

        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list= recipient_list,
        )

        # Construct the data dictionary for Google Sheet
        data1 = {
            'Location': location[0]["coverage_name"],
            'Name': client_name,
            'Email': client_email,
            'Phone': client_phone,
        }

        update_google_sheet(list(data1.values()), env('GOOGLE_SHEET_2_ID'))

        return JsonResponse({"data": list(location)}, status=200)
    return JsonResponse({"error": "Not Found"}, status=404)