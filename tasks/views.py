from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from django.contrib.auth.models import User
from .models import Task
from .serializers import UserSerializer, TaskSerializer
from .permissions import IsTaskAssignee


# =========================
# RBAC: View specific task
# =========================
class TaskDetailView(APIView):
    permission_classes = [IsAuthenticated, IsTaskAssignee]

    def get(self, request, pk):
        task = Task.objects.get(pk=pk)
        self.check_object_permissions(request, task)
        return Response({"title": task.title, "description": task.description})


# =========================
# Users: Create & List
# =========================
class UserListCreate(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # password hashing handled in serializer
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# =========================
# Tasks: Create & List
# =========================
class TaskListCreate(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# =========================
# Task Detail CRUD + RBAC
# =========================
class TaskDetail(APIView):
    permission_classes = [IsAuthenticated, IsTaskAssignee]

    def get_object(self, pk):
        return Task.objects.get(pk=pk)

    def get(self, request, pk):
        task = self.get_object(pk)
        self.check_object_permissions(request, task)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_object(pk)
        self.check_object_permissions(request, task)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_object(pk)
        self.check_object_permissions(request, task)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# =========================
# STEP 4: Secure Endpoint
# =========================
class SecureView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Secure endpoint accessed!"})
