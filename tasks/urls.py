from django.urls import path

from tasks.views import \
    (TaskDetailView,
     TaskCreateView,
     TaskListView,
     TaskAcceptView,
     TaskDoneView,
     ExecutorAcceptedView)


urlpatterns = [
    path('task/', TaskCreateView.as_view(), name='task'),
    path('tasks/', TaskListView.as_view(), name='tasks'),
    path('tasks/<int:pk>', TaskDetailView.as_view(), name='tasks_detail'),
    path('tasks/<int:pk>/accept', TaskAcceptView.as_view(), name='tasks_accept'),
    path('tasks/<int:pk>/done', TaskDoneView.as_view(), name='tasks_done'),
    path('tasks/<int:pk>/done', ExecutorAcceptedView.as_view(), name='executor_tasks'),
]