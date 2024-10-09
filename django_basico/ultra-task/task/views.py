from datetime import date

from django.shortcuts import render

from task.models import Task


def home(request):
    all_tasks = Task.objects.all()

    finished = [task for task in all_tasks if task.completed]
    not_finished = [task for task in all_tasks if not task.completed]

    return render(request, 'task/home.html', {'completed': finished, 'uncompleted': not_finished})


def task_detail(request, task_slug):
    task = Task.objects.get(slug=task_slug)
    time_left = (task.due_date - date.today()).days
    return render(request, 'task/task_detail.html', {'task': task, 'time_left': time_left})


def done(request):
    all_tasks = Task.objects.all()
    finished = [task for task in all_tasks if task.completed]
    status = 'Done'
    return render(request, 'task/task_list.html', {'tasks': finished, 'status': status})


def undone(request):
    all_tasks = Task.objects.all()
    not_finished = [task for task in all_tasks if not task.completed]
    status = 'Done'
    return render(request, 'task/task_list.html', {'tasks': not_finished, 'status': status})
