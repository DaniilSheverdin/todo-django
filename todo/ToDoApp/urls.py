from django.urls import path

from .views import GroupUpdate, TaskCreate, TaskDelete, TaskGroup, TaskList, TaskDetail, TaskUpdate, GroupCreate, GroupDelete

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('group/<int:pk>/', TaskGroup.as_view(), name='group'),
    path('add-task/', TaskCreate.as_view(), name='add-task'),
    path('add-group/', GroupCreate.as_view(), name='add-group'),
    path('delete-task/<int:pk>', TaskDelete.as_view(), name='delete-task'),
    path('delete-group/<int:pk>', GroupDelete.as_view(), name='delete-group'),
    path('update-task/<int:pk>', TaskUpdate.as_view(), name='update-task'),
    path('update-group/<int:pk>', GroupUpdate.as_view(), name='update-group'),
]
