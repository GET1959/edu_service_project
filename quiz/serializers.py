from rest_framework import serializers

from quiz.models import Quizzes, Question, Answer


class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quizzes
        fields = ['material', 'title', 'question']


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['id', 'answer_text', 'is_right',]


class CreateAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['id', 'answer_text', 'is_right',]


class RandomQuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)
    # answer = serializers.StringRelatedField(many=True)

    class Meta:
        model = Question
        fields = ['title', 'answer',]


class QuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)
    quiz = QuizSerializer(read_only=True)

    class Meta:
        model = Question
        fields = ['quiz', 'title', 'answer',]
