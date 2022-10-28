from django.db import models
from django.utils import timezone
from datetime import timedelta


def tomorrow():
    return timezone.now() + timedelta(days=1)


class TaskCategory(models.Model):
    id: models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

    def __repr__(self) -> str:
        return f"<<TaskCategory | ID: {self.id}"


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=264)
    category = models.ForeignKey(TaskCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_on = models.DateTimeField(default=tomorrow)
    is_completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"<<Task : {self.description}>>"

    def __repr__(self) -> str:
        return f"<<Task | ID: {self.id} description: {self.description} >>"
