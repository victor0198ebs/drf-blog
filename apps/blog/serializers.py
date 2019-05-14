from rest_framework import serializers

from apps.blog.models import Category, Blog, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class BlogCommentsSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    @staticmethod
    def get_comments(obj):
        comments = Comment.objects.filter(blog=obj.id)
        return CommentSerializer(comments, many=True).data

    class Meta:
        model = Blog
        fields = ['title', 'slug', 'body', 'posted', 'category', 'enabled', "comments"]
