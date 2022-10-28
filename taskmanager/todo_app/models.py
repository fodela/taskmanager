from django.db import models


class TaskState(models.Model):
    id = models.AutoField(primary_key=True)
    is_completed = models.BooleanField(default=False)
    is_due = models.BooleanField(default=False)

    def __repr__(self) -> str:
        return f"<<TaskState | ID: {self.id} >>"


class TaskCategory(models.Model):
    id: models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

    def __repr__(self) -> str:
        return f"<<TaskCategory | ID: {self.id}"


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=264)
    state = models.ForeignKey(TaskState, on_delete=models.CASCADE)
    category = models.ForeignKey(TaskCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f"<<Task : {self.description}>>"

    def __repr__(self) -> str:
        return f"<<Task | ID: {self.id} description: {self.description} >>"
