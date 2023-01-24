from django.shortcuts import render
from projects.models import Project
from django.contrib.auth.decorators import login_required

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
