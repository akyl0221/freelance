from django.contrib import admin
from django.urls import path, include

from users import views

v1 = ([
    path('', include(('tasks.urls', 'tasks'), namespace='tasks')),
    path('', include(('users.urls', 'users'), namespace='users')),
])

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(v1)),
    path('', views.index),
]
