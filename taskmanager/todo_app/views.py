from django.shortcuts import render
from todo_app.models import Task

# Create your views here.


def index(request):
    task_list = Task.objects.order_by("created_at")
    task_dict = {"all_task": task_list}
    return render(request, "todo_app/index.html", context=task_dict)


def project(request):
    return render(request, "todo_app/project.html")


def task(request):
    return render(request, "todo_app/task.html")
