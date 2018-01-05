from django.conf.urls import url
from . import views

app_name = 'Classes'

urlpatterns = [
    # /Classes/
    url(r'^$', views.index, name='index'),

    # /Classes/<classes_id>
    url(r'^(?P<classes_id>[0-9]+)/$', views.marks, name='marks'),

    # /add-class/
    url(r'^add-class/$', views.add_class, name='add-class'),

    # /add-marks/
    url(r'^(?P<classes_id>[0-9]+)/add-marks/$', views.add_marks, name='add-marks'),
]