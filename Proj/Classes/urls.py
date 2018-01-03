from django.conf.urls import url, include
from . import views

app_name = 'Classes'

urlpatterns = [
    # /Classes/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /Classes/<pk>
    # url(r'^<pk>/', views.detail, name='detail')
]