from django.contrib import admin
from apps.blog.models import Blog, BlogAdmin, Category, Comment

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
# admin.site.register(Comment)
