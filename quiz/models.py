from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from lms.models import Material

NULLABLE = {"blank": True, "null": True}


class Quizzes(models.Model):
    title = models.CharField(max_length=255, default=_("quiz_0"), verbose_name=_("Quiz title"))
    material = models.ForeignKey(Material, default=1, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")
        ordering = ["id"]


class Updated(models.Model):
    date_updated = models.DateTimeField(verbose_name=_("Last Updated"), auto_now=True)

    class Meta:
        abstract = True


class Question(Updated):

    quiz = models.ForeignKey(Quizzes, related_name='question', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))
    is_active = models.BooleanField(default=True, verbose_name=_("Active Status"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ["id"]


class Answer(Updated):
    question = models.ForeignKey(Question, related_name='answer', on_delete=models.DO_NOTHING)
    answer_text = models.CharField(max_length=255, verbose_name=_("Answer Text"))
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ["id"]


class CurrentAnswer(Updated):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
        verbose_name="Пользователь", help_text="Укажите Пользователя"
    )
    question = models.ForeignKey(Question, related_name='cur_answer', on_delete=models.DO_NOTHING)
    answer_text = models.CharField(max_length=255, **NULLABLE, verbose_name=_("Answer Text"))
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text

    class Meta:
        verbose_name = _("Test")
        verbose_name_plural = _("Tests")
        ordering = ["id"]
