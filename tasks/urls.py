from django.urls import path

from .views import TaskDetailView, TaskCreateView


urlpatterns = [
    path('tasks/', TaskCreateView.as_view(), name='tasks'),
    path('tasks/<int:pk>', TaskDetailView.as_view(), name='tasks_detail'),
]