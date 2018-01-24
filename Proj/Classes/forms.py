from django import forms
from django.contrib.auth.models import User
from .models import Classes, Marks


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class ClassesForm(forms.ModelForm):

    class Meta:
        model = Classes
        fields = ['batch', 'discipline', 'subject', 'exam_name']


class MarksForm(forms.ModelForm):

    class Meta:
        model = Marks
        fields = ['roll', 'marks_obt']


class AddClasses(forms.Form):
    num = forms.IntegerField(label='Add number of classes to be added..')
