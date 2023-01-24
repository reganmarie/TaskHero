from django.urls import path
from projects.views import project_list, show_project_details

urlpatterns = [
    path("", project_list, name="list_projects"),
    path("<int:id>/", show_project_details, name="show_project"),
]
