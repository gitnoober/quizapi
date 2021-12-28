# Generated by Django 3.2.10 on 2021-12-28 12:11

import Quiz.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0002_auto_20211227_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizzes',
            name='date_created',
            field=Quiz.models.CustomDateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='quizzes',
            name='expiry_date',
            field=Quiz.models.CustomDateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='quizzes',
            name='live_date',
            field=Quiz.models.CustomDateTimeField(null=True),
        ),
    ]