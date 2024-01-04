from django.urls import path
from . import views

app_name = "todo_app"

urlpatterns = [
    # index path
    path("", views.IndexView.as_view(), name='index'),
    path("<int:task_id>/completed/", views.completed_task, name='completed-task'),
    path("add-task/", views.add_task, name='add-task'),
    path("<int:task_id>/delete-task/", views.delete_task, name='delete-task')
]
