from django.contrib import admin
from . models import Classes, Marks, Profile

# Register your models here.
admin.site.register(Classes)
admin.site.register(Marks)
admin.site.register(Profile)
