from django import forms
from django.contrib.auth.models import User
from .models import Classes, Marks, Profile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['name', 'phone']


class ClassesForm(forms.ModelForm):

    class Meta:
        model = Classes
        fields = ['batch', 'discipline', 'subject', 'exam_name']


class MarksForm(forms.ModelForm):

    class Meta:
        model = Marks
        fields = ['roll', 'marks_obt']
