from django.test import TestCase
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

from .models import Todo


def mark_task_ask_completed(task_id):
    """
    Toggle the task completed with the given `task_id`.
    """
    try:
        task = Todo.objects.get(pk=task_id)
        task.completed = True
        task.save()
        return task
    except Todo.DoesNotExist:
        raise ValueError("The task_id doesn't exist")


def create_task(title, description, completed=False):
    """
    Create the task object.
    """
    time = timezone.now()
    return Todo.objects.create(title=title, description=description, created_date=time, completed=completed)


def delete_task(task_id):
    """
    Delete the task with the given `task_id`.
    :param task_id:
    :return:
    """
    deleted_task = Todo.objects.get(pk=task_id)
    deleted_task.delete()


# Create your tests here.
class TestTodoApp(TestCase):
    def test_completed_todo(self):
        # completed field False by default
        new_task = create_task(title="Hello", description="Test functionality")
        new_task = mark_task_ask_completed(new_task.id)
        # Mark as complete

        self.assertEqual(new_task.completed, True)

    def test_add_task(self):
        """
        The new task will be created and display on index page.
        :return:
        """
        new_task = create_task(title="Wash car", description="Wash the car before dad go home and see his car.")
        response = self.client.get(reverse("todo_app:index"))
        self.assertContains(response, new_task.title)

    def test_delete_task(self):
        """
        Delete the task.
        :return:
        """
        task = create_task(title="Task to be deleted", description="delete this task")
        task.save()
        delete_task(task.id)
        # print(task)
        with self.assertRaises(ObjectDoesNotExist):
            Todo.objects.get(pk=task.id)
