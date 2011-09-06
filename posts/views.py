from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from models import PostView
        
def posts_list(request):
    language = request.session.get('lang', settings.DEFAULT_LANGUAGE)
    object_list =  PostView.objects.list(language).select_related()
    return render_to_response("posts/list.html", locals(), RequestContext(request))

def posts_view(request, **kwargs):
    try:
        if set(('slug', 'language', 'year', 'month', 'day')).issubset(kwargs):
            postview = PostView.objects.find(kwargs)
        else: raise Http404
    except ObjectDoesNotExist:
        raise Http404
    return render_to_response("posts/view.html", {'postview': postview}, RequestContext(request))
