from django.contrib import admin
from tasklist.models import TaskModel


class TaskAdmin(admin.ModelAdmin):
    search_fields = ('description', 'user',)
    list_display = ('description', 'user', 'schedule', 'is_done', 'is_overdue',)
    list_filter = ('schedule', 'user',)


admin.site.register(TaskModel, TaskAdmin)
