from django.urls import path
from projects.views import project_list, show_project_details, create_project

urlpatterns = [
    path("", project_list, name="list_projects"),
    path("<int:id>/", show_project_details, name="show_project"),
    path("create/", create_project, name="create_project"),
]
