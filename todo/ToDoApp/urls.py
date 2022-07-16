from django.urls import path

from .views import CustomLoginView, GroupList, GroupUpdate, TaskCreate, TaskDelete, TaskGroup, TaskList, TaskDetail, TaskUpdate, GroupCreate, GroupDelete
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', TaskList.as_view(), name='tasks'),
    path('group-list', GroupList.as_view(), name='groups'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('group/<int:pk>/', TaskGroup.as_view(), name='group'),
    path('add-task/', TaskCreate.as_view(), name='add-task'),
    path('add-group/', GroupCreate.as_view(), name='add-group'),
    path('delete-task/<int:pk>', TaskDelete.as_view(), name='delete-task'),
    path('delete-group/<int:pk>', GroupDelete.as_view(), name='delete-group'),
    path('update-task/<int:pk>', TaskUpdate.as_view(), name='update-task'),
    path('update-group/<int:pk>', GroupUpdate.as_view(), name='update-group'),
]
