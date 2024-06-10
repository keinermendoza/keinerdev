from django.urls import path
from . import views

urlpatterns = [
    path('email-contact/', views.email_contact, name='api_email_contact'),
]
