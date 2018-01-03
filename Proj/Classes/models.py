from django.db import models


# Create your models here.
class Classes(models.Model):
    batch = models.CharField(max_length=100)
    discipline = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.discipline + '-' + self.batch


class Marks(models.Model):
    my_class = models.ForeignKey(Classes, on_delete=models.CASCADE)
    marks1 = models.CharField(max_length=100,default='NA')
    marks2 = models.CharField(max_length=100,default='NA')
    marks3 = models.CharField(max_length=100,default='NA')
