from typing import Any, List
from django.db.models import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, FormView
from django_htmx.http import trigger_client_event
from .forms import (
    ContactForm
)
from .task import send_feedback_email_task

from core.models import (
    Testimonial,
    Project
)

from blog.models import (
    Post
)

class HomePage(TemplateView):
    template_name = "core/pages/home.html"
    PROJECT_LIMIT :int = 2
    POST_LIMIT :int = 3
    TESTIMONIALS_LIMIT :int = 3


    def get_testimonials(self) -> QuerySet[Testimonial]:
        return Testimonial.published.all()[:self.TESTIMONIALS_LIMIT]

    def get_projects(self) -> list:
        return Project.published.all()[:self.PROJECT_LIMIT]
    
    def get_posts(self) -> QuerySet[Post]:
        """last published posts"""
        return Post.published.all()[:self.POST_LIMIT]
    

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({
            "projects": self.get_projects(),
            "testimonials": self.get_testimonials(),
            "posts": self.get_posts()
        })
        return context
    
class AboutPage(TemplateView):
    template_name = "core/pages/about.html"
    PROJECT_LIMIT :int = 2
    POST_LIMIT :int = 3

class ContactFormPartialView(FormView):
    form_class = ContactForm
    template_name = "core/partials/home/contact_form.html"

    def form_valid(self, form) -> HttpResponse:
        response = self.render_to_response({})
        return trigger_client_event(
            response,
            "display_toast",
            {
                "status":200,
                "message":"Email Enviado. Revisa la Bandeja de Entrada tu Correo"
            }
        )
    
    def form_invalid(self, form) -> HttpResponse:
        response = super().form_invalid(form)
        return trigger_client_event(
            response,
            "display_toast",
            {
                "status":400,
                "message":"No fue posible enviar el su mensaje"
            }
        )   

    def post(self, request, *args, **kwargs):
        """
        Sends Async Email
        """
        form = self.get_form()
        if form.is_valid():
            form.send_email()
            return self.form_valid(form)
        else:
            if "username" in form.errors:
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
