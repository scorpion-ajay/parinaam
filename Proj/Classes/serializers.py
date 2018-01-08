from rest_framework import serializers
from .models import Classes, Marks


class ClassesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classes
        fields = ('batch', 'discipline', 'subject', 'exam_name')
