from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class NotificationModel(models.Model):
    """
    A daily review notification sent for a user.
    """

    class Meta:
        db_table = "notification"
        verbose_name = "notificação"
        verbose_name_plural = "notificações"

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="usuário")
    text = models.CharField(max_length=255, verbose_name="texto")
    sent_date = models.DateTimeField(verbose_name="data de envio")
    was_sent = models.BooleanField(verbose_name="enviado")

    def __str__(self):
        return self.text


class TaskModel(models.Model):
    """
    A representation for a task made by a user.
    """

    class Meta:
        db_table = "task"
        verbose_name = "tarefa"
        verbose_name_plural = "tarefas"

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="usuário")
    title = models.CharField(max_length=128, verbose_name="título")
    description = models.TextField(max_length=256, verbose_name="descrição")
    due_date = models.DateTimeField(verbose_name="vencimento")
    is_done = models.BooleanField(verbose_name="concluída")

    def __str__(self):
        return self.description

    def is_overdue(self) -> bool:
        return not self.is_done and timezone.now() >= self.due_date

    is_overdue.boolean = True
    is_overdue.short_description = "atrasada"
