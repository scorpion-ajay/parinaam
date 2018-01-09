from django import forms
from .models import Classes, Marks


class ClassesForm(forms.ModelForm):

    class Meta:
        model = Classes
        fields = ['batch', 'discipline', 'subject', 'exam_name']


class MarksForm(forms.ModelForm):

    class Meta:
        model = Marks
        fields = ['roll', 'marks_obt']
