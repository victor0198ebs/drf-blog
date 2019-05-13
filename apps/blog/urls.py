from django.urls import path

from apps.blog.views import CategoryViewSet, BlogListView, BlogItemView, AddBlogView#, CommentListView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'categories', CategoryViewSet, basename='category')
urlpatterns = router.urls

urlpatterns += [
    path('blog/create/', AddBlogView.as_view(), name='new_blog'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogItemView.as_view(), name='blog_item'),
    # path('comment/', CommentListView.as_view(), name='comment_list'),
]
