from django.db import models

NULLABLE = {"blank": True, "null": True}


class Section(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    preview = models.ImageField(
        upload_to="lms/images", **NULLABLE, verbose_name="Просмотр", help_text="Загрузите изображение"
    )
    description = models.TextField(verbose_name="Описание", help_text="Добавьте описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "раздел"
        verbose_name_plural = "разделы"


class Material(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название"
    )
    content = models.TextField(
        verbose_name="Описание",
        help_text="Добавьте описание"
    )
    section = models.ForeignKey(
        Section,
        on_delete=models.SET_NULL,
        related_name="materials",
        verbose_name="Раздел",
        help_text="Укажите раздел",
        **NULLABLE
    )
    preview = models.ImageField(
        upload_to="lms/images", **NULLABLE,
        verbose_name="Просмотр",
        help_text="Загрузите изображение"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "материал"
        verbose_name_plural = "материалы"
