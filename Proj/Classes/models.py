from django.db import models


# Create your models here.
class Classes(models.Model):
    batch = models.CharField(max_length=100)
    discipline = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.discipline + '-' + self.batch + '-' + self.subject


class ExamName(models.Model):
    my_class = models.ForeignKey(Classes, on_delete=models.CASCADE)
    exam_name = models.CharField(max_length=100, default='Sessional-1')


class Marks(models.Model):
    this_exam = models.ForeignKey(Classes, on_delete=models.CASCADE)
    # student_name = models.CharField(max_length=100, default='example : ajay verma')
    roll = models.CharField(max_length=100, default='ex : 2601')
    marks_obt = models.CharField(max_length=100, default='ex : 50')
