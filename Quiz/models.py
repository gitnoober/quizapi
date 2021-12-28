from django.contrib.admin.decorators import action
from django.db import models
from django.utils.translation import gettext_lazy as _ #identify what might need to be translated
# Create your models here.

class CustomDateTimeField(models.DateTimeField):
    def value_to_string(self, obj):
        val = self.value_from_object(obj)
        if val:
            val.replace(microsecond=0)
            return val.isoformat()
        return ''


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class QuizManager(models.Manager):
    def active(self):
        return super().get_queryset().filter(active = True)

    def expired(self):
        return super().get_queryset().filter(active = False)




class Quizzes(models.Model):

    class Meta:
        verbose_name = _('Quiz')
        verbose_name_plural = _('Quizzes')
        ordering = ['id']

    title = models.CharField(max_length=255 , default=_('New Quiz') , verbose_name=_("Quiz Title"))
    category = models.ForeignKey(Category , default=1 , on_delete=models.DO_NOTHING) # foreign key to category table , on_delete = do nothing because we simply do not want the category to be deleted
    date_created = CustomDateTimeField(auto_now_add=True) # automatically generated
    live_date = CustomDateTimeField(null=True)
    expiry_date = CustomDateTimeField(null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    objects = models.Manager()
    QuizManager = QuizManager()

    

class Updated(models.Model):
    date_updated = models.DateTimeField(
        verbose_name=_("Last Updated") ,auto_now=True) # when we update the item , it will update the date time field
    
    class Meta:
        abstract = True 
        

class Question(Updated): # extending from this abstract class

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ['id']

    SCALE = (
        (0, _('Fundamental')),
        (1, _('Beginner')),
        (2, _('Intermediate')),
        (3, _('Advanced')),
        (4, _('Expert')),
    )

    TYPE = (
        (0, _('Multiple Choice')),
        (1, _('Open Text')),
    )
    
    quiz = models.ForeignKey(Quizzes , related_name='question' , on_delete=models.DO_NOTHING)
    technique = models.IntegerField(choices= TYPE , default=0 , verbose_name=_("Type of Question"))
    title = models.CharField(max_length=255 , verbose_name=_('Title'))
    difficulty = models.IntegerField(choices=SCALE , default=0, verbose_name=_('Difficulty'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))
    is_active = models.BooleanField(default=False , verbose_name=_("Active Status")) # turn on and off the question

    def __str__(self):
        return self.title




class Answer(Updated): # extending from this abstract class


    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ['id']

        
    question = models.ForeignKey(Question , related_name='answer' , on_delete=models.DO_NOTHING)
    answer_text = models.CharField(max_length=255 , verbose_name=_("Answer Text")) # multiple answers here recorded via the id of the question , and one of those will be flagged as right
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text

    


