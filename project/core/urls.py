from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
    path("about", views.AboutPage.as_view(), name="about"),
    path("contact-me", views.ContactFormPartialView.as_view(), name="contact_me"),

]
