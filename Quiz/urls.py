from django.urls import path
from .views import geeks_view,QuizQuestion
app_name = 'Quiz'

urlpatterns = [
    path('' , geeks_view ,name='quiz'),
    path('q/<str:topic>/', QuizQuestion.as_view(), name='questions' ),


]

# path('' , QuizUpdated.as_view() , name='QuizUpdated'),
