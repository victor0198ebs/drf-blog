from django.contrib.auth.models import User
from apps.blog.models import Blog
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "password",)


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ("title", "slug", "body", "posted", "enabled", "category")
