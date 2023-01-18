from hashlib import new
from site import venv
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.csrf import csrf_protect

# Local import
from .forms import *
from .models import *


@login_required
def home(request):
    context = {}
    return render(request, 'dashboard/home.html', context)


def profile(request):
    context = {}

    if request.method == 'GET':
        form = ProfileForm(instance=request.user.profile)
        image_form = ProfileImageForm(instance=request.user.profile)
        context['form'] = form
        context['image_form'] = image_form
        return render(request, 'dashboard/profile.html', context)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        image_form = ProfileImageForm(
            request.POST, request.FILES, instance=request.user.profile)

        if form.is_valid():
            form.save()
            return redirect('profile')
        if image_form.is_valid():
            image_form.save()
            return redirect('profile')

    return render(request, 'dashboard/profile.html', context)


# def addbanner(request):
#     context = {}

#     if request.method == 'GET':
#         return render(request, 'dashboard/add.html', context)

#     if request.method == 'POST':
#         title = request.POST['title']
#         image = request.POST['image']
#         content = request.POST['content']

#         new_home = Home(title=title, image=image, content=content)
#         print(new_home.title, new_home.content, new_home.image)
#         new_home.save()
#         return render(request, 'dashboard/add.html', {})

def addbanner(request):
    if request.method == "POST":
        form = HomeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'dashboard/add.html', {'form': form})

    else:
        form = HomeForm()
    return render(request, 'dashboard/add.html', {'form': form})


def updatebanner(request):
    home = Home.objects.get(pk=1)
    form = HomeForm(request.POST or None, instance=home)
    if form.is_valid():
        form.save()
    return render(request, 'dashboard/updateBanner.html', {'home': home, 'form': form})


def addpricing(request):
    if request.method == "POST":
        form = PricingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'dashboard/addpricing.html', {'form': form})

    else:
        form = PricingForm()
    return render(request, 'dashboard/addpricing.html', {'form': form})


def listpricing(request):
    pricing = Pricing.objects.all()
    return render(request, 'dashboard/listpricing.html', {'pricing': pricing})


def updatepricing(request, pricing_id):
    pricing = Pricing.objects.get(pk=pricing_id)
    form = PricingForm(request.POST or None, instance=pricing)
    if form.is_valid():
        form.save()
    return render(request, 'dashboard/updateBanner.html', {'pricing': home, 'form': form})


def addfeedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'dashboard/addfeedback.html', {'form': form})

    else:
        form = FeedbackForm()
    return render(request, 'dashboard/addfeedback.html', {'form': form})


def listfeedback(request):
    feedback = Feedback.objects.all()
    return render(request, 'dashboard/listfeedback.html', {'feedback': feedback})


def deletefeedback(request, feedback_id):
    feedback = Feedback.objects.get(pk=feedback_id)
    feedback.delete()
    return redirect('addfeedback')


def addfaq(request):
    if request.method == "POST":
        form = FaqsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'dashboard/addfaq.html', {'form': form})

    else:
        form = FaqsForm()
    return render(request, 'dashboard/addfaq.html', {'form': form})


def listfaqs(request):
    faq = Faqs.objects.all()
    return render(request, 'dashboard/listfaqs.html', {'faq': faq})


def deletefaq(request, faq_id):
    faq = Faqs.objects.get(pk=faq_id)
    faq.delete()
    return redirect('addfaq')


def addcoverage(request):
    if request.method == "POST":
        form = CoverageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'dashboard/addcoverage.html', {'form': form})

    else:
        form = CoverageForm()
    return render(request, 'dashboard/addcoverage.html', {'form': form})

def listcoverage(request):
    coverage = Coverage.objects.all()
    context = {
        'coverage': coverage
    }
    print(context)
    return render(request, 'dashboard/listcoverage.html', context)

def updatecoverage(request, coverage_id):
    coverage = Coverage.objects.get(pk=coverage_id)
    form = CoverageForm(request.POST or None, instance=coverage)
    if form.is_valid():
        form.save()
    return render(request, 'dashboard/updatecoverage.html', {'coverage': home, 'form': form})

def deletecoverage(request, coverage_id):
    coverage = Coverage.objects.get(pk=coverage_id)
    coverage.delete()
    return redirect('addcoverage')