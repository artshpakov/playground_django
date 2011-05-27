from django.db import models
from django.db.models.query import QuerySet
from datetime import datetime

class PostViewQuerySet(QuerySet):
    def language_is(self, lang):
        return self.filter(language = lang)
        
    def published_at(self, date):
        return self.filter(post__pub_date =
            datetime.min.replace(
                year = int(date['year']),
                month = int(date['month']),
                day = int(date['day'])
            )
        )

class PostViewManager(models.Manager):
    def get_query_set(self):
        return PostViewQuerySet(self.model)
    
    def list(self, language):
        return self.get_query_set().language_is(language)
    
    def find(self, params):
        return self.get_query_set().published_at(
            params
        ).language_is(
            params['language']
        ).get(
            post__slug = params['slug']
        )
