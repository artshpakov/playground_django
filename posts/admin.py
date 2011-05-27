from django.contrib import admin
from models import PostView, Post

class PostAdmin(admin.ModelAdmin):
    exclude = ('pub_date',)
    

class PostviewAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('language',)

admin.site.register(Post, PostAdmin)    
admin.site.register(PostView, PostviewAdmin)
