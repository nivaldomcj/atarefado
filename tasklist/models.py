from django.db import models
from django.contrib.auth.models import User


class TaskModel(models.Model):
    """
    An representation for a task made by a user.
    """

    class Meta:
        db_table = "task"
        verbose_name = "tarefa"
        verbose_name_plural = "tarefas"

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="usuário")
    description = models.CharField(max_length=128, verbose_name="descrição")
    schedule = models.DateTimeField(verbose_name="vencimento")
    is_done = models.BooleanField(verbose_name="concluída")

    def __str__(self):
        return self.description
