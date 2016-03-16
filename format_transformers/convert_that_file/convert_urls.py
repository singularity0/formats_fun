from django.conf.urls import url
from .views import convert_mp3

urlpatterns = [
    url(r'^mp3/', convert_mp3 , name='converter'),
]
