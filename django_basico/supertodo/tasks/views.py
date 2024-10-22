from datetime import date

from django.shortcuts import redirect, render
from django.utils.text import slugify

from .forms import AddTaskForm, EditTaskForm
from .models import Task


def task_list(request):
    all_tasks = Task.objects.all()
    status = 'All Tasks'

    return render(request, 'tasks/task_list.html', {'tasks': all_tasks, 'status': status})


def done(request):
    all_tasks = Task.objects.all()
    done = list(filter(lambda task: task.done, all_tasks))
    status = 'Done'
    return render(request, 'tasks/task_list.html', {'tasks': done, 'status': status})


def pending(request):
    all_tasks = Task.objects.all()
    pending = list(filter(lambda task: not task.done, all_tasks))
    status = 'Pending'
    return render(request, 'tasks/task_list.html', {'tasks': pending, 'status': status})


def task_detail(request, task_slug):
    task = Task.objects.get(slug=task_slug)
    if task.complete_before:
        time_left = (task.complete_before - date.today()).days
    else:
        time_left = -1
    return render(request, 'tasks/task_detail.html', {'task': task, 'time_left': time_left})


def addTask(request):
    if request.method == 'POST':
        addTaskForm = AddTaskForm(request.POST)
        if addTaskForm.is_valid():
            title = addTaskForm.cleaned_data['title']
            description = addTaskForm.cleaned_data['description']
            done = addTaskForm.cleaned_data['done']
            complete_before = addTaskForm.cleaned_data['complete_before']

            task = Task(
                title=title,
                description=description,
                done=done,
                complete_before=complete_before,
                slug=slugify(title),
            )

            task.save()
            return redirect('tasks:task-list')
    else:
        addTaskForm = AddTaskForm()
    return render(request, 'tasks/taskForms.html', {'taskForm': addTaskForm})


def toggle(request, task_slug):
    task = Task.objects.get(slug=task_slug)
    print(f'1 {task.done}')
    task.done = not task.done
    print(f'2 {task.done}')
    task.save()
    print(f'3 {task.done}')
    return redirect('tasks:task-list')


def delete(request, task_slug):
    Task.objects.filter(slug=task_slug).delete()
    return redirect('tasks:task-list')


def edit(request, task_slug):
    task = Task.objects.get(slug=task_slug)

    if request.method == 'POST':
        editTaskForm = EditTaskForm(request.POST)
        if editTaskForm.is_valid():
            task.description = editTaskForm.cleaned_data['description']
            task.done = editTaskForm.cleaned_data['done']
            task.complete_before = editTaskForm.cleaned_data['complete_before']

            task.save()
            return redirect('tasks:task-list')
    else:
        editTaskForm = EditTaskForm(instance=task)

    return render(request, 'tasks/taskForms.html', {'taskForm': editTaskForm})
