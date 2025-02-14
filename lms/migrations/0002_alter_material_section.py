# Generated by Django 5.0.7 on 2024-07-18 17:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lms", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="material",
            name="section",
            field=models.ForeignKey(
                blank=True,
                help_text="Укажите раздел",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="lms.section",
                verbose_name="Раздел",
            ),
        ),
    ]
