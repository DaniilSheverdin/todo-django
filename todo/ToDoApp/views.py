from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic.list import ListView
from .models import Task
# Create your views here.


class TaskList(ListView):
    """controller for task list"""
    model = Task
   # template = loader.get_template('ToDoApp/task_list.html')
