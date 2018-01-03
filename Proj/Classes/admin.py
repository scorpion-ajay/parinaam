from django.contrib import admin
from . models import Classes, Marks, ExamName

# Register your models here.
admin.site.register(Classes)
admin.site.register(ExamName)
admin.site.register(Marks)
