# Generated by Django 5.0.4 on 2024-04-13 20:58

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="title",
            new_name="name",
        ),
        migrations.RemoveField(
            model_name="project",
            name="end_date",
        ),
        migrations.RemoveField(
            model_name="project",
            name="start_date",
        ),
        migrations.RemoveField(
            model_name="task",
            name="completed",
        ),
        migrations.RemoveField(
            model_name="task",
            name="due_date",
        ),
        migrations.AddField(
            model_name="project",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=datetime.datetime(
                    2024, 4, 13, 20, 58, 20, 75519, tzinfo=datetime.timezone.utc
                ),
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="task",
            name="assignee",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="tasks",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="task",
            name="status",
            field=models.CharField(
                choices=[
                    ("New", "Новая"),
                    ("In_progress", "В работе"),
                    ("Completed", "Завершена"),
                ],
                default="New",
                max_length=50,
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
