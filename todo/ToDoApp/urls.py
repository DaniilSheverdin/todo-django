from django.urls import path

from .views import TaskCreate, TaskDelete, TaskList, TaskDetail, TaskUpdate

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('add-task/', TaskCreate.as_view(), name='add-task'),
    path('delete-task/<int:pk>', TaskDelete.as_view(), name='delete-task'),
    path('update-task/<int:pk>', TaskUpdate.as_view(), name='update-task'),
]
