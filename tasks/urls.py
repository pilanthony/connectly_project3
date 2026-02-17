from django.urls import path
from .views import UserListCreate, TaskListCreate, TaskDetail
from .views import SecureView

urlpatterns = [
    # This completes the URL: /tasks/users/ 
    path('users/', UserListCreate.as_view(), name='user-list-create'),

    # This completes the URL: /tasks/
    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),

    # This completes the URL: /tasks/<id>/
    # Detail, update, delete a task with RBAC
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('secure/', SecureView.as_view(), name='secure-endpoint'),

]
