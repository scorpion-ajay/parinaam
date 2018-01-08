from django.conf.urls import url
from . import views

app_name = 'Classes'

urlpatterns = [
    # /Classes/
    url(r'^$', views.index, name='index'),

    # /Classes/<classes_id>
    url(r'^(?P<classes_id>[0-9]+)/$', views.marks, name='marks'),

    # /Classes/add-class/
    url(r'^add-class/$', views.add_class, name='add-class'),

    # /Classes/add-marks/
    url(r'^(?P<classes_id>[0-9]+)/add-marks/$', views.add_marks, name='add-marks'),

    # /Classes/delete-class/
    url(r'^(?P<classes_id>[0-9]+)/delete-class/$', views.delete_classes, name='delete-class'),

    # /Classes/delete-marks/
    url(r'^(?P<classes_id>[0-9]+)/delete-marks/(?P<marks_id>[0-9]+)/$', views.delete_marks, name='delete-marks'),

    # /Classes/<classes_id>/update-class/
    url(r'^(?P<classes_id>[0-9]+)/update-class/$', views.update_class, name='update-class'),

    # /Classes/<classes_id>/update/<marks_id>/
    url(r'^(?P<classes_id>[0-9]+)/update-marks/(?P<marks_id>[0-9]+)/$', views.update_marks, name='update-marks'),

    # /Classes/update-classes/
    url(r'^update-classes/$', views.update_classes, name='update-classes'),

    # /Classes/<classes_id>/update-marks/
    url(r'^(?P<classes_id>[0-9]+)/update-all-marks/$', views.update_all_marks, name='update-all-marks'),
]