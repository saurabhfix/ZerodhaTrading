from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('auth/', views.contact_view, name='contact'),
    path('contact/success', views.contact_success_view, name='contact-success'),   
    path('calculate', views.calculate_view, name='calculate'),
]
