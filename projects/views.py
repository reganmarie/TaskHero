from django.shortcuts import render, redirect
from projects.models import Project
from django.contrib.auth.decorators import login_required
from projects.forms import ProjectForm

# Create your views here.


@login_required
def project_list(request):
    project_list = Project.objects.filter(owner=request.user)
    context = {
        "projects": project_list,
    }
    return render(request, "projects/list.html", context)


@login_required
def show_project_details(request, id):
    project_details = Project.objects.get(id=id)
    context = {
        "details": project_details,
    }
    return render(request, "projects/detail.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(False)
            project.owner = request.user
            project.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()

    context = {
        "form": form,
    }
    return render(request, "projects/create.html", context)
