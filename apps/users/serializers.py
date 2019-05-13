from django.contrib.auth.models import User
from apps.blog.models import Blog
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "password",)


