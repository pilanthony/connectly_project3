from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)  #User's unique username
    email = models.EmailField(unique=True) #User's unique email
    created_at = models.DateTimeField(auto_now_add=True) #Timestamp when the user was created

    def __str__(self):
        return self.username
    
class Post(models.Model):
    content = models.TextField() # The text content of the post 
    author = models.ForeignKey (User, on_delete=models.CASCADE, related_name='posts')  #The user who created the post #Each post belongs one user, and if the user is deleted, the post will also be deleted
    created_at = models.DateTimeField(auto_now_add=True)  #Timestamp when the post was created

    def __str__(self):
        return self.content[:50]  #Returns a preview of the post content (first 50 characters) when the post object is printed
    
    class Meta:
        ordering = ['-created_at']
        
    