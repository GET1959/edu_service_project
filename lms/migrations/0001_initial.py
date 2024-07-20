# Generated by Django 5.0.7 on 2024-07-12 16:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Section",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=100, verbose_name="Название")),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите изображение",
                        null=True,
                        upload_to="lms/images",
                        verbose_name="Просмотр",
                    ),
                ),
                ("description", models.TextField(help_text="Добавьте описание", verbose_name="Описание")),
            ],
            options={
                "verbose_name": "раздел",
                "verbose_name_plural": "разделы",
            },
        ),
        migrations.CreateModel(
            name="Material",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=100, verbose_name="Название")),
                ("content", models.TextField(help_text="Добавьте описание", verbose_name="Описание")),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите изображение",
                        null=True,
                        upload_to="lms/images",
                        verbose_name="Просмотр",
                    ),
                ),
                (
                    "section",
                    models.ForeignKey(
                        blank=True,
                        help_text="Укажите курс",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="lms.section",
                        verbose_name="Курс",
                    ),
                ),
            ],
            options={
                "verbose_name": "материал",
                "verbose_name_plural": "материалы",
            },
        ),
    ]
