from django.views import generic
from .models import Classes
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'Classes/index.html'

    context_object_name = 'all_classes'

    def get_queryset(self):
        return Classes.objects.all()


class MarksView(generic.DetailView):
    model = Classes
    template_name = 'Classes/marks.html'


class ClassesCreate(CreateView):
    model = Classes
    fields = ['batch','discipline','subject','exam_name']
