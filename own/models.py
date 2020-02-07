from django.db import models

# Create your models here.
from django.db import models



class Quiz1(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(verbose_name='description', null=True)
    # created_date = models.DateField(auto_now=True)
    url = models.URLField(verbose_name='url', null=True)

class Question1(models.Model):
    quiz = models.ForeignKey(Quiz1, on_delete=models.CASCADE)
    question = models.TextField(verbose_name='question', null=False)
    choice1 = models.TextField(verbose_name='question1', null=False)
    choice2 = models.TextField(verbose_name='question2', null=False)
    choice3 = models.TextField(verbose_name='question3', null=False)
    choice4 = models.TextField(verbose_name='question4', null=False)
    answer = models.CharField(max_length=10)