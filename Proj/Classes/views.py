from django.shortcuts import render
from .models import Classes


# Create your views here.
def index(request):
    all_classes = Classes.objects.all()
    context = {'all_classes': all_classes}
    return render(request, 'Classes/index.html', context)
