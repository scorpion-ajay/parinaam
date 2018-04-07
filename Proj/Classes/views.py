from django.views.generic import View
from django.contrib.auth.decorators import login_required
from .models import Classes, Marks
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.forms.models import modelformset_factory
from .forms import ClassesForm, MarksForm, UserForm, AddClasses
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect

app_name = 'Classes'


def home(request):
    return render(request, 'Classes/register.html')


def my_login(request):
    return render(request, 'classes/registration_form.html', {})


def my_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Classes:index'))


@login_required
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


def add_classes(request, num):
    para = int('0' + num)
    ClassesFormSet = modelformset_factory(Classes, form=ClassesForm, extra=para)
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
    return render(request, 'Classes/formset.html', {'formset': formset})


def add_marks(request, classes_id, num):
    para = int('0'+num)
    MarksFormSet = modelformset_factory(Marks, form=MarksForm, extra=para)
    formset = MarksFormSet(request.POST or None, request.FILES or None, queryset=Marks.objects.none())
    classes = get_object_or_404(Classes, pk=classes_id)
    if request.method == 'POST':
        if formset.is_valid():
            for f in formset:
                cd = f.cleaned_data
                roll = cd.get('roll')
                marks_obt = cd.get('marks_obt')
                Marks.objects.create(
                    classes=classes,
                    roll=roll,
                    marks_obt=marks_obt,
                )
            return HttpResponseRedirect(reverse('Classes:marks', args=(classes_id,)))
    return render(request, 'Classes/formset.html', {'formset': formset})


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


def delete_classes(request, classes_id):
    classes = Classes.objects.get(pk=classes_id)
    classes.delete()
    return HttpResponseRedirect(reverse('Classes:index'))


def delete_marks(request, classes_id, marks_id):
    marks = Marks.objects.get(pk=marks_id)
    marks.delete()
    return HttpResponseRedirect(reverse('Classes:marks', args=(classes_id,)))


class UserFormView(View):
    form_class = UserForm
    template_name = 'Classes/registration_form.html'

    # displays blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalised) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # return User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('Classes:index'))
        return render(request, self.template_name, {'form': form})