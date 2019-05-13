from django.db import models
from django.contrib import admin


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    enabled = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        out = str(self.title) + " -> " + str(self.enabled)
        return out


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'enabled')


admin.site.register(Blog, BlogAdmin)
