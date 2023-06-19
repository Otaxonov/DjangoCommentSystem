from django.contrib import admin
from .models import Post, Comment

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'author']


admin.site.register(Comment)
