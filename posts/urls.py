from django.urls import path
from .import views

urlpatterns = [
    
    # Get all users or create one/user
    path('users/', views.get_users, name='get_users'),
    path('users/create/', views.create_user, name='create_user'),
    
    # Get all posts or create one/user
    path('posts/', views.get_posts, name='get_posts'),
    path('posts/create/', views.create_post, name='create_post'),
]
