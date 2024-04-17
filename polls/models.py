import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200, default='default_question_text')
    pub_date = models.DateTimeField("date published", default=timezone.now)
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=1)  # Suponiendo que el ID de la primera pregunta sea 1
    choice_text = models.CharField(max_length=200, default='default_value_here')
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text