from django.db import models
from django.urls import reverse


# Create your models here.
class Classes(models.Model):
    batch = models.CharField(max_length=100, null=True)
    discipline = models.CharField(max_length=100, null=True)
    subject = models.CharField(max_length=100, null=True)
    exam_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.discipline + '-' + self.batch + '-' + self.subject + '-' + self.exam_name


class Marks(models.Model):
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)
    roll = models.IntegerField()
    marks_obt = models.IntegerField()

    def __str__(self):
        return str(self.roll) + '-' + str(self.marks_obt)
