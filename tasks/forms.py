from django.forms import ModelForm
from tasks.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            "name",
            "start_date",
            "due_date",
            "project",
            "assignee",
        ]


class EditTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            "name",
            "start_date",
            "due_date",
            "project",
            "assignee",
            "is_completed",
        ]


class TaskNotes(ModelForm):
    class Meta:
        model = Task
        fields = [
            "name",
            "due_date",
            "project",
            "notes",
        ]
