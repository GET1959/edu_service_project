from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from quiz.models import Quizzes, Question, Answer, CurrentAnswer
from quiz.serializers import QuizSerializer, RandomQuestionSerializer, QuestionSerializer, CreateAnswerSerializer


class Quiz(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('material',)


class RandomQuestion(APIView):
    serializer_class = QuestionSerializer
    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)


class QuizQuestion(APIView):
    serializer_class = QuizSerializer

    def get(self, request, format=None, **kwargs):
        quiz = Question.objects.filter(quiz__title=kwargs['topic'])
        serializer = QuestionSerializer(quiz, many=True)
        return Response(serializer.data)


class CreateAnswer(APIView):
    serializer_class = CreateAnswerSerializer

    def post(self, request, pk, *args, **kwargs):
        question = Question.objects.get(pk=pk)
        right_answer = Answer.objects.get(question_id=pk, is_right=True)
        current_answer = CurrentAnswer.objects.create(
            user=self.request.user,
            question=question,
            answer_text=self.request.data.get("answer_text"),
            is_right=(str(self.request.data.get("answer_text")) == str(right_answer))
        )

        if str(current_answer) == str(right_answer):
            message = 'Ответ верный'
        else:
            message = 'Ответ неверный, попробуйте еще раз'

        return Response({'message': message})
