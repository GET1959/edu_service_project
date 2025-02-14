# Generated by Django 5.0.7 on 2024-07-18 17:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("lms", "0002_alter_material_section"),
    ]

    operations = [
        migrations.CreateModel(
            name="Question",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("date_updated", models.DateTimeField(auto_now=True, verbose_name="Last Updated")),
                ("title", models.CharField(max_length=255, verbose_name="Title")),
                ("date_created", models.DateTimeField(auto_now_add=True, verbose_name="Date Created")),
                ("is_active", models.BooleanField(default=False, verbose_name="Active Status")),
            ],
            options={
                "verbose_name": "Question",
                "verbose_name_plural": "Questions",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Answer",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("date_updated", models.DateTimeField(auto_now=True, verbose_name="Last Updated")),
                ("answer_text", models.CharField(max_length=255, verbose_name="Answer Text")),
                ("is_right", models.BooleanField(default=False)),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, related_name="answer", to="quiz.question"
                    ),
                ),
            ],
            options={
                "verbose_name": "Answer",
                "verbose_name_plural": "Answers",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Quizzes",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(default="quiz_0", max_length=255, verbose_name="Quiz title")),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                (
                    "material",
                    models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to="lms.material"),
                ),
            ],
            options={
                "verbose_name": "Quiz",
                "verbose_name_plural": "Quizzes",
                "ordering": ["id"],
            },
        ),
        migrations.AddField(
            model_name="question",
            name="quiz",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, related_name="question", to="quiz.quizzes"
            ),
        ),
    ]
