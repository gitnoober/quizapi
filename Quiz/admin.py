from django.contrib import admin
from django.db.models import fields
from . import models

# Register your models here.

@admin.register(models.Category)
class CatAdmin(admin.ModelAdmin):
    list_display = [
        'name',

    ]


@admin.register(models.Quizzes)
class QuizAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'expiry_date',
        'active',
    ]

class AnswerInLineModel(admin.TabularInline):
    model = models.Answer
    fields = [
        'answer_text',
        'is_right',
    ]



@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'quiz',
    ] # when we build a question we will only see a title and a quiz
    list_display = [
        'title',
        'quiz',
        'date_updated',
    ]

    inlines = [
        AnswerInLineModel,
    ]

    # on the question page we are going to use an inline and we are also going to insert the answers

@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'question',
        'answer_text',
        'is_right'
    ]



