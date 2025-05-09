from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
    path('', views.hero, name='hero'),
    path('post/', views.home, name='home'),
    path('create/', views.create_post, name='create'),
    path('posts/<slug:slug>/', views.post_detail , name='detail'),
    path('posts/edit/<slug:slug>/', views.edit_post, name='edit_posts'),
    path('<slug:slug>/delete/', views.delete_post, name='delete_post'),
    path('category/<str:category>/', views.posts_by_category, name='category'),
    path('<slug:slug>/likes/', views.like_post, name='like_post'),
    path('drafts/', views.draft_posts, name='draft_posts'),
    # path('count/', views.view_count, name='view_count'),
    path('post/<slug:slug>/', views.post_detail, name='post.detail'),
    
]
