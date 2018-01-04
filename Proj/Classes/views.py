from django.views import generic
from .models import Classes, Marks


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'Classes/index.html'

    context_object_name = 'all_classes'

    def get_queryset(self):
        return Classes.objects.all()