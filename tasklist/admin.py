from django.contrib import admin
from tasklist.models import TaskModel
from tasklist.models import NotificationModel


class TaskAdmin(admin.ModelAdmin):
    search_fields = ('title', 'user')
    list_display = ('title', 'user', 'due_date', 'is_done', 'is_overdue')
    list_filter = ('due_date', 'user')


class NotificationAdmin(admin.ModelAdmin):
    search_fields = ('text', 'user')
    list_display = ('text', 'user', 'sent_date', 'was_sent')
    list_filter = ('sent_date', 'user', 'was_sent')


admin.site.register(TaskModel, TaskAdmin)
admin.site.register(NotificationModel, NotificationAdmin)
admin.site.site_header = "Atarefado: Administração"