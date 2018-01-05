from django.db import models
from django.urls import reverse


# Create your models here.
class Classes(models.Model):
    batch = models.CharField(max_length=100, default='2k15')
    discipline = models.CharField(max_length=100, default='IT')
    subject = models.CharField(max_length=100, default='data structures')
    exam_name = models.CharField(max_length=100, default='Sessional-1')

    def __str__(self):
        return self.discipline + '-' + self.batch + '-' + self.subject + '-' + self.exam_name


class Marks(models.Model):
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)
    roll = models.CharField(max_length=100)
    marks_obt = models.CharField(max_length=100)

    def __str__(self):
        return self.roll + '-' + self.marks_obt
