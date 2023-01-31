from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tasks.forms import TaskForm, EditTaskForm, TaskNotes
from tasks.models import Task

# Create your views here.


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("list_projects")
    else:
        form = TaskForm()
    context = {
        "form": form,
    }
    return render(request, "tasks/create.html", context)


@login_required
def my_tasks(request):
    tasks = Task.objects.filter(assignee=request.user)
    context = {
        "tasks": tasks,
    }
    return render(request, "tasks/detail.html", context)


@login_required
def edit_tasks(request, id):
    task = Task.objects.get(id=id)
    if request.method == "POST":
        form = EditTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("show_my_tasks")
    else:
        form = EditTaskForm(instance=task)

    context = {
        "task": task,
        "form": form,
    }
    return render(request, "tasks/edit.html", context)


@login_required
def task_notes(request, id):
    task = Task.objects.get(id=id)
    if request.method == "POST":
        form = TaskNotes(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("show_my_tasks")
    else:
        form = TaskNotes(instance=task)

    context = {
        "task": task,
        "form": form,
    }
    return render(request, "tasks/notes.html", context)
