import markdown
from django.db import models
from django.urls import reverse
from django.utils.text import Truncator
from django.utils.safestring import mark_safe
from bs4 import BeautifulSoup
from django_extensions.db.fields import AutoSlugField



class Topic(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.name



class PostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="P")
    
class Post(models.Model):
    class Status(models.TextChoices):
        EDITING = ("E", "Editing")
        PUBLISHED = ("P", "Published")

    title = models.CharField(max_length=100)
    slug =  AutoSlugField(populate_from='title')
    body = models.TextField()
    image = models.ImageField(upload_to='posts', null=True, blank=True)

    topics = models.ManyToManyField(Topic, related_name="posts")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=Status.choices, default=Status.EDITING)
    
    objects = models.Manager()  
    published = PostManager()

    def publish(self) -> None:
        self.status = Post.Status.PUBLISHED
        self.save()
    
    def unpublish(self) -> None:
        self.status = Post.Status.EDITING
        self.save()

    def get_absolute_url(self):
        return reverse("blog:detail", args=[self.slug])
    

    @property
    def body_html(self) -> str:
        return mark_safe(markdown.markdown(self.body))
    
    @property
    def preview(self) -> str:
        soup = BeautifulSoup(self.body_html, 'html.parser')
        first_paragraph = soup.find('p')
        return first_paragraph.text if first_paragraph else ""

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        indexes = [
            models.Index(fields=["-created"])
        ]
        ordering = ["-created"]


    #  "title": "Las Tags de Componentes de django-allauth",
    # "body": "string",
    # "image": "core/images/allauth.png",
    # "topics": ["Django", "django-allauth"],
    # "preview": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Iste minus id, architecto ipsum numquam eius!"