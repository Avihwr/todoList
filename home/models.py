from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Tasks", null=True)
    taskName = models.CharField(max_length=128)
    taskDesc = models.TextField()
    taskTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.taskName + ' by ' + self.user.username

