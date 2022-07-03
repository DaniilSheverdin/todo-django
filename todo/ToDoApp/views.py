from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task
# Create your views here.


class TaskList(ListView):
    """controller for show task list"""
    model = Task
    context_object_name = "tasks"
    template_name = 'ToDoApp/task.list.html'


class TaskDetail(DetailView):
    """controller for show single task"""
    model = Task
    context_object_name = "task"
    template_name = 'ToDoApp/task.html'


class TaskCreate(CreateView):
    """controller for create task"""
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('tasks')
    template_name = 'ToDoApp/add.task.form.html'


class TaskUpdate(UpdateView):
    """controller for update task"""
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('tasks')
    template_name = 'ToDoApp/add.task.form.html'


class TaskDelete(DeleteView):
    """controller for delete task"""
    model = Task
    success_url = reverse_lazy('tasks')
    template_name = 'ToDoApp/task.delete.confirm.html'
