from django import forms
from .models import Classes,Marks


class ClassesForm(forms.ModelForm):

    # class  meta is used to define anything that is not a form field
    class Meta:
        model = Classes
        fields = ['batch', 'discipline', 'subject', 'exam_name']


class MarksForm(forms.ModelForm):

    class Meta:
        model = Marks
        fields = ['classes', 'roll', 'marks_obt']
