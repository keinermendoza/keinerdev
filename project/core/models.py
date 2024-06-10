
import markdown
from django.db import models
from blog.models import Topic
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from .validators import for_published_status_require_image_not_none

class TestimonialManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="P")

class Testimonial(models.Model):
    class Status(models.TextChoices):
        EDITING = ("E", "Editing")
        PUBLISHED = ("P", "Published")

    name = models.CharField(max_length=40)
    profession = models.CharField(max_length=80)
    message = models.CharField(max_length=250)
    image = models.FileField(upload_to="testimonials", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=Status.choices, default=Status.EDITING)

    objects = models.Manager()  
    published = TestimonialManager()

    def clean(self):
        for_published_status_require_image_not_none(self.status, self.image)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
    
    def publish(self) -> None:
        self.status = Project.Status.PUBLISHED
        self.save()
    
    def unpublish(self) -> None:
        self.status = Project.Status.EDITING
        self.save()

    def __str__(self) -> str:
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=["-created"])
        ]
        ordering = ["-created"]

class ProjectManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="P")
    
class Project(models.Model):
    class Status(models.TextChoices):
        EDITING = ("E", "Editing")
        PUBLISHED = ("P", "Published")

    customer = models.CharField(max_length=40)
    customer_commercial_field = models.CharField(max_length=80)
    description = models.TextField()
    image = models.FileField(upload_to="projects", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    tecnologies = models.ManyToManyField(Topic, related_name="projects")
    status = models.CharField(max_length=1, choices=Status.choices, default=Status.EDITING)
    
    objects = models.Manager()  
    published = ProjectManager()
        
    def clean(self):
        for_published_status_require_image_not_none(self.status, self.image)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
    
    @property
    def description_html(self) -> str:
        return mark_safe(markdown.markdown(self.description))
    
    def publish(self) -> None:
        self.status = Project.Status.PUBLISHED
        self.save()
    
    def unpublish(self) -> None:
        self.status = Project.Status.EDITING
        self.save()

    def __str__(self) -> str:
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=["-created"])
        ]
        ordering = ["-created"]

