from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'created_time', 'executor', 'created_by')


admin.site.register(Task, TaskAdmin)


