from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', views.home, name='dashboard'),
    path('profile', views.profile, name='profile'),
    path('addbanner', views.addbanner, name='addbanner'),
    path('updatebanner', views.updatebanner, name='updatebanner'),
    path('addcoverage', views.addcoverage, name='addcoverage'),
    path('listcoverage', views.listcoverage, name='listcoverage'),
    path('updatecoverage/<coverage_id>', views.updatecoverage, name='updatecoverage'),
    path('deletecoverage/<coverage_id>', views.deletecoverage, name='deletecoverage'),
    path('addpricing', views.addpricing, name='addpricing'),
    path('listpricing', views.listpricing, name='listpricing'),
    path('updatepricing/<pricing_id>', views.updatepricing, name='updatepricing'),
    path('addfeedback', views.addfeedback, name='addfeedback'),
    path('listfeedback', views.listfeedback, name='listfeedback'),
    path('deletefeedback/<feedback_id>',
         views.deletefeedback, name='deletefeedback'),
    path('addfaq', views.addfaq, name='addfaq'),
    path('listfaqs', views.listfaqs, name='listfaqs'),
    path('deletefaq/<faq_id>', views.deletefaq, name='deletefaq'),
]
