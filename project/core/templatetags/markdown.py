import markdown
from django import template
from django.utils.safestring import mark_safe


register = template.Library()

@register.filter(name="markdown")
def from_markdown(markdown_string):
    html_string = markdown.markdown(markdown_string)
    return mark_safe(html_string)