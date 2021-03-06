from django.urls import path

from apps.blog.views import CategoryViewSet, BlogListView, BlogItemView, AddBlogView, CommentListView, AddCommentView, \
    CommentItemView, BlogItemCommentsView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = router.urls

urlpatterns += [
    path('blog/create/', AddBlogView.as_view(), name='new_blog'),
    path('blog/', BlogListView.as_view(), name='blog_list'),

    # for getting comments with view -> BlogItemView
    # for getting comments with serializer -> BlogItemCommentsView
    path('blog/<int:pk>/', BlogItemCommentsView.as_view(), name='blog_item'),


    path('comment/', CommentListView.as_view(), name='new_comment'),
    path('comment/create', AddCommentView.as_view(), name='comment_list'),
    path('comment/<int:pk>/', CommentItemView.as_view(), name='comment_item'),
]
