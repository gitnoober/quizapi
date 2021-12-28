import re
from django import http
from django.db.models import query
from django.db.models.query import QuerySet
from django.http import request, response
from django.shortcuts import render
from django.utils.translation import activate
from rest_framework import generics
from rest_framework import serializers
from rest_framework.serializers import Serializer
from .models import Question, Quizzes
from .serializers import QuizSerializer, RandomQuestionSerializer , QuestionSerializer
from rest_framework.views import APIView

from django.db.models import Q
from datetime import datetime
from django.http import HttpResponse

from rest_framework import viewsets
from django.http import JsonResponse
import json
from rest_framework.response import Response
# Create your views here.

    
def geeks_view(request):

    obj_all = Quizzes.objects.all()

    past = []
    live = []
    upcoming = []

    for obj in obj_all:
        now = datetime.now()
        date_now = now.replace(tzinfo=None)
        exp_date = obj.expiry_date.replace(tzinfo=None)
        start_date = obj.live_date.replace(tzinfo=None)
        if date_now >= exp_date:
            past.append(obj.title)
        elif date_now >= start_date and date_now <= exp_date:
            live.append(obj.title)
        else:
            upcoming.append(obj.title)

    dic = {'past':past , 'live':live , 'upcoming':upcoming}

    return HttpResponse(json.dumps(dic))
    

# class geeks_view(APIView):

#     def get(self , request ):
#         obj_all = Quizzes.objects.all()

#         past = []
#         live = []
#         upcoming = []

#         for obj in obj_all:
#             now = datetime.now()
#             date_now = now.replace(tzinfo=None)
#             exp_date = obj.expiry_date.replace(tzinfo=None)
#             start_date = obj.live_date.replace(tzinfo=None)
#             if date_now >= exp_date:
#                 # past.append(obj.title)
#                 past.append(obj)
#             elif date_now >= start_date and date_now <= exp_date:
#                 # live.append(obj.title)
#                 live.append(obj)
#             else:
#                 # upcoming.append(obj.title)
#                 upcoming.append(obj)

#         dic = {"past":past , "live":live , "upcoming":upcoming}
        

#         serializer = QuizSerializer(past, many=True)

#         return Response(serializer.data )




class QuizQuestion(APIView):

    def get(self , request , format=None , **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic'])
        serializer = QuestionSerializer(question , many=True)
        return Response(serializer.data)

