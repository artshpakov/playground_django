from django import template
from django.conf import settings
from posts.models import PostView

def get_translations(postview):
    return {'routes': postview.get_translations()}

register = template.Library()
register.inclusion_tag('posts/includes/translations.html')(get_translations)
