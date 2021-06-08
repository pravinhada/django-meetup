from os import name
from django.urls import path
from .views import index, meetup_details, confirm_registration

urlpatterns = [
    path('', index, name="all-meetups"),
    path('<slug:slug>/success', confirm_registration, name="confirm-registration"),
    path('details/<slug:slug>', meetup_details, name="meetup-details")
]
