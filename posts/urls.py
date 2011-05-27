from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('posts.views',
    url(r'^$', 'posts_list', name = "posts_list"),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[a-zA-Z0-9-_]+)/(?P<language>\w{2})',
        'posts_view', name = "posts_view"),
)
