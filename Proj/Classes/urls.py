from django.conf.urls import url
from . import views

app_name = 'Classes'

urlpatterns = [
    # /Classes/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /Classes/<pk>
    url(r'^(?P<pk>[0-9]+)/$', views.MarksView.as_view(), name='marks'),

    # /Classes/<pk>/add-Class
    url(r'^classes/add/$', views.ClassesCreate.as_view(), name='add-classes')
]