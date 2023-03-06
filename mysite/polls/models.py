from datetime import datetime, timezone
from django.db import models
from django.contrib import admin

# Create your models here.


class Role(models.Model):
    role_name = models.CharField(max_length=10)
    description = models.CharField(max_length=50)
    
class User(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_now_add=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
        
class Candidate(models.Model):
    cadidate_name = models.CharField(max_length=200)
    cv = models.CharField(max_length=500)
    email = models.CharField(max_length=50) 

class Election(models.Model):
    election_title= models.CharField(max_length=200);
    start_date = models.DateTimeField('date stated')
    end_date = models.DateTimeField('date end')

class Vote(models.Model):
    cadidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    campaignRhetoric = models.CharField(max_length=200)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)