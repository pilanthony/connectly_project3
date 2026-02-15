from django.db import models

class User(models.Model):  #User model representing system users
    username = models.CharField(max_length=100, unique=True)  #Ensure unique usernames
    email =models.EmailField(unique=True) #Enforce unique email addreses
    created_at =models.DateTimeField(auto_now_add=True) # Automatically ser creations timestamps

def __str__(self):
    return self.username  #Return username as string representation of the User model

#Task model linked to User through a Foreign Key
class Task(models.Model):
    title = models.TextField(max_length=255)  #Task title with a max length
    description = models.CharField() #Optional detailed task description
    assigned_to = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE) # Delete tasks if the user is deleted
    created_at = models.DateTimeField(auto_now_add=True) # Automatically set creation timestamps

    def __str__(self):
        return f"Task: {self.title} assigned to {self.assigned_to.username}"
