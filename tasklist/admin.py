from django.contrib import admin
from tasklist.models import TaskModel


class TaskAdmin(admin.ModelAdmin):
    search_fields = ('description', 'user',)
    list_display = ('description', 'user', 'due_date', 'is_done', 'is_overdue',)
    list_filter = ('due_date', 'user',)


admin.site.register(TaskModel, TaskAdmin)
