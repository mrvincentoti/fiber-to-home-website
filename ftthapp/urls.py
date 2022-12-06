from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='dashboard'),
    path('contact', views.contact, name='contact'),
    path('plan/<int:id>/', views.plan, name='plan')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
