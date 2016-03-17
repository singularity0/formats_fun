from django.conf.urls import url
from .views import convert_menu

urlpatterns = [
    url(r'^mp3/', convert_menu , name='converter'),
]
