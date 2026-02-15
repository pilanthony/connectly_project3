from django.urls import path

from tasks import admin
from .views import UserListCreate, TaskListCreate
from django.urls import path, include


urlpatterns = [
    # This completes the URL: /tasks/users/ 
    path('users/', UserListCreate.as_view(), name='user-list-create'),

    # This completes the URL: /tasks/
    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),
]
