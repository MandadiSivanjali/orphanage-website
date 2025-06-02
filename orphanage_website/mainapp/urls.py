from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('donation/', views.donation, name='donation'),
    path('requirements/', views.requirements, name='requirements'),
    path('add-requirement/', views.add_general_requirement, name='add_requirement'),

    # Meal Booking APIs
    path('check-booking/', views.check_and_save_booking, name='check_booking'),
    path('check-slot/', views.check_slot, name='check_slot'),
    path('confirm-booking/', views.confirm_booking, name='confirm_booking'),

    # Sponsorship Pages
    path('sponsorship/', views.sponsorship, name='sponsorship'),
    path('sponsor/<int:child_id>/', views.sponsor_child, name='sponsor_child'),
]