from django.conf.urls import url
from . import views

app_name = 'home_page'

urlpatterns = [
    url(r'^', views.home),
]
