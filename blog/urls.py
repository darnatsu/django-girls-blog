from django.urls import path
from . import views
from blog.views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:post_id>/', PostDetailView.as_view(), name='post_detail' ),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/edit/<int:post_id>/', views.post_edit, name='post_edit'),
]
