from django.contrib import admin
from django.conf.urls import url, include
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Classes/', include('Classes.urls')),

    # social login with google and github
    url(r'^auth/', include('social_django.urls', namespace='social')),  # <- Here
]
