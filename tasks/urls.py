from django.urls import path
from tasks.views import (
    create_task,
    my_tasks,
    edit_tasks,
    task_notes,
    delete_task,
)

urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", my_tasks, name="show_my_tasks"),
    path("edit/<int:id>", edit_tasks, name="edit_tasks"),
    path("notes/<int:id>", task_notes, name="task_notes"),
    path("delete/<int:id>", delete_task, name="delete_task"),
]
