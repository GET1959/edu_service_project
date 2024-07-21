from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from lms.models import Section, Material
from quiz.models import Quizzes, Question, CurrentAnswer, Answer
from users.models import User


class QuizTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@sky.pro")
        self.material = Material.objects.create(
            title="test_material",
            content="content of test_material",
        )
        self.quiz = Quizzes.objects.create(
            title="test_quiz",
            material=self.material
        )
        self.question = Question.objects.create(
            quiz=self.quiz,
            title="test_que_1"
        )
        self.answer = Answer.objects.create(
            question=self.question,
            answer_text="answer_1",
            is_right=True
        )
        self.createanswer = CurrentAnswer.objects.create(
            question=self.question,
            answer_text="answer_2"
        )


        self.client.force_authenticate(user=self.user)

    def test_quiz(self):
        url = reverse("quiz:quiz")
        response = self.client.get(url)
        data = response.json()[0]
        print(data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.quiz.title)

    def test_quizquestion(self):
        url = reverse("quiz:question", args=("test_quiz",))
        response = self.client.get(url)
        data = response.json()[0]
        print(data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.question.title)

    def test_createanswer_false(self):
        url = reverse("quiz:test", args=(self.question.pk,))
        data = {"answer_text": "answer_2"}
        response = self.client.post(url, data)
        data = response.json()#[0]
        print(data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("message"), "Ответ неверный, попробуйте еще раз")

    def test_createanswer_true(self):
        url = reverse("quiz:test", args=(self.question.pk,))
        data = {"answer_text": "answer_1"}
        response = self.client.post(url, data)
        data = response.json()#[0]
        print(data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("message"), "Ответ верный")
