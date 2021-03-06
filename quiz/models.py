import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    
    question_text = models.CharField(max_length=200)
    create_question_by_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    ans = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    point = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


class User(models.Model):
   
    username = models.CharField(max_length=200)
    user_point = models.IntegerField(default=0)
    
    def __str__(self):
        return self.username



