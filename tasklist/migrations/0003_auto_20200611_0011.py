# Generated by Django 3.0.7 on 2020-06-11 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasklist', '0002_auto_20200610_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='description',
            field=models.TextField(max_length=256, verbose_name='descrição'),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='is_done',
            field=models.BooleanField(default=False, verbose_name='concluída'),
        ),
    ]
