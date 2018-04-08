from django.conf.urls import url, include
from . import views

app_name = 'Classes'

urlpatterns = [
    # /login
    url(r'^login/$', views.UserFormView.as_view(), name='login'),

    # logout
    url(r'^logout/$', views.my_logout, name='logout'),

    url(r'^start/$', views.home, name='home'),

    # /Classes/
    url(r'^$', views.index, name='index'),

    # /Classes/<classes_id>
    url(r'^(?P<classes_id>[0-9]+)/$', views.marks, name='marks'),

    # /Classes/add-classes/
    url(r'^add-classes/(?P<num>[0-9]+)/$', views.add_classes, name='add-classes'),

    # /Parinaam/dev/
    url(r'^dev/$', views.developers, name='developers'),

    # /Parinaam/profile/
    url(r'^profile/$', views.set_profile, name='setProfile'),

    # /Classes/add-marks/
    url(r'^(?P<classes_id>[0-9]+)/(?P<num>[0-9]+)/$', views.add_marks, name='add-marks'),

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