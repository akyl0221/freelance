from django.urls import path

from .views import TaskDetailView, TaskCreateView, TaskListView


urlpatterns = [
    path('task/', TaskCreateView.as_view(), name='task'),
    path('tasks/', TaskListView.as_view(), name='tasks'),
    path('tasks/<int:pk>', TaskDetailView.as_view(), name='tasks_detail'),
]