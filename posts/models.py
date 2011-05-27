from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.contenttypes import generic
from datetime import datetime
from managers import PostViewManager

class Post(models.Model):
    author = models.ForeignKey(User)
    pub_date = models.DateField(default = datetime.now)
    slug = models.SlugField(unique = True)
    
    def __unicode__(self):
        return self.slug
  
    
class PostView(models.Model):
    post = models.ForeignKey(Post, related_name = "views")
    title = models.CharField(max_length = 80)
    teaser = models.TextField()
    content = models.TextField()
    language = models.CharField(max_length = 2, choices = settings.LANGUAGES)
    content_object = generic.GenericForeignKey("content_type", "object_id")

    objects = PostViewManager()

    def __unicode__(self):
        return u'%s %s' % (self.teaser, self.content)

    @models.permalink
    def get_absolute_url(self):
        return('posts_view', (), {
                'year': self.post.pub_date.year,
                'month': self.post.pub_date.month,
                'day': self.post.pub_date.day,
                'slug': self.post.slug,
                'language': self.language,
            }
        )

    class Meta:
        ordering = ['-post__pub_date']

    def get_translations(self):
        views = PostView.objects.filter(post = self.post)
        map = {}
        for v in views:
            if v.language != self.language:
                map[v.get_language_display()] = v.get_absolute_url()
        return map
