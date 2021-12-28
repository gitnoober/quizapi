
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import Quizzes
from datetime import datetime

@shared_task
def add(x, y):
    return x + y


# @shared_task
# def updatedb(self):
#     now = datetime.now()
#     obj = Quizzes
#     print(dir(obj))

# @app.task(bind=True)
@shared_task
def hello_world():
    print('Hello world!')

@shared_task
def updatedb():
    _len = Quizzes.objects.all()

    for idx, i in enumerate(_len):
        obj = list(Quizzes.objects.filter(id=idx+1))[0]
        now = datetime.now()
        date_now = now.replace(tzinfo=None)
        exp_date = obj.expiry_date.replace(tzinfo=None)
        if date_now > exp_date:
            obj.active = False
            obj.save()
        
        # print(obj.active)

    
