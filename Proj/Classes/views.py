from django.views import generic
from .models import Classes, Marks
from django.urls import reverse
from django.forms.models import modelformset_factory
from .forms import ClassesForm, MarksForm
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

app_name = 'Classes'


# Create your views here.
def index(request):
    classes = Classes.objects.all().order_by('discipline')
    return render(request, 'Classes/index.html', {'classes': classes})


def update_class(request, classes_id):
    classes = get_object_or_404(Classes, pk=classes_id)
    form = ClassesForm(request.POST or None, instance=classes)
    if form.is_valid():
        classes = form.save(commit=False)
        classes.save()
        return HttpResponseRedirect(reverse('Classes:index'))
    return render(request, 'Classes/classes_form.html', {'form': form})


def update_classes(request):
    ClassesFormset = modelformset_factory(Classes, form=ClassesForm, extra=0)
    classes_qs = Classes.objects.all().order_by('batch')
    formset = ClassesFormset(request.POST or None, queryset=classes_qs)
    if formset.is_valid():
        instances = formset.save(commit=False)
        for instance in instances:
            instance.save()
        return HttpResponseRedirect(reverse('Classes:index'))
    return render(request, 'Classes/formset.html', {'formset': formset})


def add_classes(request):
    ClassesFormSet = modelformset_factory(Classes, form=ClassesForm, extra=2)
    formset = ClassesFormSet(request.POST or None, request.FILES or None, queryset=Classes.objects.none())
    if request.method == 'POST':
        if formset.is_valid():
            for f in formset:
                cd = f.cleaned_data
                batch = cd.get('batch')
                discipline = cd.get('discipline')
                subject = cd.get('subject')
                exam_name = cd.get('exam_name')
                Classes.objects.create(
                    batch=batch,
                    discipline=discipline,
                    subject=subject,
                    exam_name=exam_name,
                )
            return HttpResponseRedirect(reverse('Classes:index'))
    return render(request, 'Classes/formset.html',{'formset': formset})


def update_all_marks(request, classes_id):
    MarksFormset = modelformset_factory(Marks, form=MarksForm, extra=0)
    myclass = Classes.objects.get(pk=classes_id)
    marks_qs = Marks.objects.filter(classes=myclass).order_by('roll')
    formset = MarksFormset(request.POST or None, queryset=marks_qs)
    if formset.is_valid():
        instances = formset.save(commit=False)
        for instance in instances:
            instance.save()
        return HttpResponseRedirect(reverse('Classes:marks', args=(classes_id,)))
    return render(request, 'Classes/formset.html', {'formset': formset})


def update_marks(request, classes_id, marks_id):
    marks = get_object_or_404(Marks, pk=marks_id)
    form = MarksForm(request.POST or None, instance=marks)
    if form.is_valid():
        marks_form = form.save(commit=False)
        marks_form.save()
        return HttpResponseRedirect(reverse('Classes:marks', args=(classes_id,)))
    return render(request, 'Classes/marks_form.html', {'form': form})


def marks(request, classes_id):
    classes = get_object_or_404(Classes, pk=classes_id)
    marks_qs = Marks.objects.all().filter(classes=classes_id).order_by('roll')
    return render(request, 'Classes/marks.html', {'classes': classes, 'marks_qs': marks_qs})


def add_class(request):
    form = ClassesForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        classes = form.save(commit=False)
        classes.save()
        return HttpResponseRedirect(reverse('Classes:index'))
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
       return HttpResponseRedirect(reverse('Classes:marks', args=(classes_id,)))
    context = {
        'classes': classes,
        'form': form,
    }
    return render(request, 'Classes/marks_form.html', context)


def delete_classes(request, classes_id):
    classes = Classes.objects.get(pk=classes_id)
    classes.delete()
    return HttpResponseRedirect(reverse('Classes:index'))


def delete_marks(request, classes_id, marks_id):
    marks = Marks.objects.get(pk=marks_id)
    marks.delete()
    return HttpResponseRedirect(reverse('Classes:marks', args=(classes_id,)))
