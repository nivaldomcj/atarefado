from django.contrib import admin
from tasklist.models import TaskModel


class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'schedule', 'is_done', 'is_overdue')


admin.site.register(TaskModel, TaskAdmin)
