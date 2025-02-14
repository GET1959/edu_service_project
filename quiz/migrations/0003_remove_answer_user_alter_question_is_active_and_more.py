# Generated by Django 5.0.7 on 2024-07-20 17:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0002_answer_user"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="answer",
            name="user",
        ),
        migrations.AlterField(
            model_name="question",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Active Status"),
        ),
        migrations.CreateModel(
            name="CurrentAnswer",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("date_updated", models.DateTimeField(auto_now=True, verbose_name="Last Updated")),
                ("answer_text", models.CharField(max_length=255, verbose_name="Answer Text")),
                ("is_right", models.BooleanField(default=False)),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, related_name="cur_answer", to="quiz.question"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        help_text="Укажите Пользователя",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Test",
                "verbose_name_plural": "Tests",
                "ordering": ["id"],
            },
        ),
    ]
