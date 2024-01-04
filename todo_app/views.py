from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.http import Http404
from django.contrib import messages


from .forms import TodoForm
from .models import Todo


class IndexView(generic.ListView):
    template_name = "todo_app/index.html"
    model = Todo
    ordering = ['-created_date']
    context_object_name = "todos"


def completed_task(request, task_id):
    task = get_object_or_404(Todo, pk=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('todo_app:index')


def add_task(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            Todo.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description']
            )
            return redirect('todo_app:index')
    else:
        form = TodoForm()
    return render(request, 'todo_app/add_task.html', {"form": form})


def delete_task(request, task_id):
    try:
        task_deleted = get_object_or_404(Todo, pk=task_id)
        task_deleted.delete()
        messages.success(request, "Deleted successfully. ❤")
    except Http404:
        messages.error(request, f"Cannot delete this task with the given task_id: {task_id} 💔")
    return redirect('todo_app:index')
