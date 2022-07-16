from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Group, Task
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin


class CustomLoginView(LoginView):
    """crontroller for user login"""
    template_name = "ToDoApp/login.html"
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class GroupList(LoginRequiredMixin, ListView):
    """controller for show group list"""
    model = Group
    context_object_name = "groups"
    template_name = 'ToDoApp/group.list.html'''


class TaskList(LoginRequiredMixin, ListView):
    """controller for show task list"""
    model = Task
    context_object_name = "tasks_n_group"
    template_name = 'ToDoApp/task.list.html'

    def get_context_data(self, **kwargs):
        context = super(TaskList, self).get_context_data(**kwargs)
        context.update({
            'tasks': Task.objects.filter(user=self.request.user),
            'groups': Group.objects.filter(user=self.request.user),
        })
        return context

    def get_queryset(self):
        return Task.objects.all()


class TaskGroup(LoginRequiredMixin, ListView):
    """controller for show task list by group"""
    model = Task
    context_object_name = "tasks_n_group"
    template_name = 'ToDoApp/by.group.list.html'

    def get_context_data(self, **kwargs):
        context = super(TaskGroup, self).get_context_data(**kwargs)
        context.update({
            'tasks': Task.objects.filter(group=self.kwargs['pk']),
            'groups': Group.objects.filter(user=self.request.user),
            'current_group': Group.objects.get(id=self.kwargs['pk'])
        })
        return context

    def get_queryset(self):
        return Task.objects.all()


class TaskDetail(LoginRequiredMixin, DetailView):
    """controller for show single task"""
    model = Task
    context_object_name = "task"
    template_name = 'ToDoApp/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    """controller for create task"""
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('tasks')
    template_name = 'ToDoApp/add.task.form.html'


class GroupCreate(LoginRequiredMixin, CreateView):
    """controller for create group"""
    model = Group
    fields = ['name']
    success_url = reverse_lazy('tasks')
    template_name = 'ToDoApp/add.group.form.html'

    # Функция для кастомной валидации полей формы модели
    def form_valid(self, form):
        # создаем форму, но не отправляем его в БД, пока просто держим в памяти
        fields = form.save(commit=False)
        # Через реквест передаем недостающую форму, которая обязательна
        fields.user = User.objects.get(id=self.request.user.id)
        # Наконец сохраняем в БД
        fields.save()
        return super().form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    """controller for update task"""
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('tasks')
    template_name = 'ToDoApp/add.task.form.html'


class GroupUpdate(LoginRequiredMixin, UpdateView):
    """controller for update group"""
    model = Group
    fields = ['name']
    success_url = reverse_lazy('tasks')
    template_name = 'ToDoApp/add.group.form.html'


class TaskDelete(LoginRequiredMixin, DeleteView):
    """controller for delete task"""
    model = Task
    success_url = reverse_lazy('tasks')
    template_name = 'ToDoApp/task.delete.confirm.html'


class GroupDelete(LoginRequiredMixin, DeleteView):
    """controller for delete task"""
    model = Group
    success_url = reverse_lazy('tasks')
    template_name = 'ToDoApp/group.delete.confirm.html'
