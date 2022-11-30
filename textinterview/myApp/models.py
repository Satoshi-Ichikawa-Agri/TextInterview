""" Models
"""
from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=50)
    question_content = models.CharField(max_length=100)
    answer = models.CharField(max_length=4000)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_content
