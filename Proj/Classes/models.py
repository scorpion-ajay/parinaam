from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, default=12)
    name = models.CharField(max_length=1000, blank=True)
    phone = models.CharField(max_length=15,null=True, blank=True)

    def __str__(self):
        return self.name


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Classes(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE,default=12)
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
