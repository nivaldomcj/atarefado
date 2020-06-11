from django.contrib.auth.models import User
from django.utils import timezone

from tasklist.models import TaskModel, NotificationModel

from datetime import date


def save_today_tasks_notification():
    """
    Save a notification of today's tasks of all users in the database
    """

    # Fetch users that have unfinished tasks for today
    users = User.objects.filter(tasks__due_date__date=date.today(),
                                tasks__is_done=False).distinct()

    for user in users:
        # Fetch number of tasks this user have pending for today
        count_tasks = TaskModel.objects.filter(user=user,
                                               due_date__date=date.today(),
                                               is_done=False).count()

        # Create a new daily tasks notification for this user
        text = "Bom dia, você tem {} tarefas para hoje!".format(count_tasks)
        notification = NotificationModel(user=user,
                                         text=text,
                                         sent_date=timezone.now(),
                                         was_sent=False)
        notification.save()
