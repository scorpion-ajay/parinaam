from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    phone = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Classes(models.Model):
    # user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
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
