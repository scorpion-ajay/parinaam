from django.views import generic
from .models import Classes, Marks
from .forms import ClassesForm, MarksForm
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.

def index(request):
    classes = Classes.objects.all
    return render(request, 'Classes/index.html', {'classes': classes})


def marks(request, classes_id):
    classes = get_object_or_404(Classes, pk=classes_id)
    marks = classes.marks_set.all
    return render(request, 'Classes/marks.html', {'classes': classes, 'marks': marks})


def add_class(request):
    form = ClassesForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        classes = form.save(commit=False)
        classes.save()
        return render(request, 'Classes/marks.html', {'classes': classes})
    return render(request, 'Classes/classes_form.html', {'form': form})


def add_marks(request, classes_id):
    form = MarksForm(request.POST or None, request.FILES or None)
    classes = get_object_or_404(Classes, pk=classes_id)
    if form.is_valid():
       classes_marks = classes.marks_set.all()
       for s in classes_marks:
           if s.roll == form.cleaned_data.get('roll'):
               context = {
                   'classes': classes,
                   'form': form,
                   'error_message': 'you already added that roll number',
               }
               return render(request, 'Classes/marks_form.html', context)
       marks = form.save(commit=False)
       marks.classes = classes
       marks.roll = form.cleaned_data.get('roll')
       marks.marks_obt = form.cleaned_data.get('marks_obt')
       marks.save()
       return render(request, 'Classes/marks.html', {'classes': classes})
    context = {
        'classes': classes,
        'form': form,
    }
    return render(request, 'Classes/marks_form.html', context)

