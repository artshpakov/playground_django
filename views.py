from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings

def switch_language(request):
    language = request.GET.get('language', settings.DEFAULT_LANGUAGE)
    request.session['lang'] = language
    return HttpResponseRedirect(reverse('posts_list'))
