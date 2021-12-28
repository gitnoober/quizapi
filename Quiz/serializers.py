from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Question, Quizzes , Answer
from rest_framework.views import APIView
from datetime import datetime



class QuizSerializer(serializers.ModelSerializer):

    class Meta:

        model = Quizzes
        fields = [
            'live_date',
            'expiry_date',
            'title',
        ] # collecting just the title and push it to the front-end



class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = [
            'id',
            'answer_text',
            'is_right',
        ]

class RandomQuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True , read_only= True)

    class Meta:

        model = Question
        fields = [
            'title' , 'answer'
        ]

class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True , read_only= True)
    quiz = QuizSerializer(read_only= True)
    

    class Meta:

        model = Question
        fields = [
            'quiz','title' , 'answer'
        ]