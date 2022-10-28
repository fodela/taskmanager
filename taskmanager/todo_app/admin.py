from django.contrib import admin
from models import Task, TaskCategory, TaskState
# Register your models here.

admin.register(Task)
admin.register(TaskCategory)
admin.register(TaskState)
