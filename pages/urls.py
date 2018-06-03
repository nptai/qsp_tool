from django.conf.urls import url
from . import views

app_name = 'pages'

urlpatterns = [
    url(r'^page_create/', views.page_create, name='create'),
    url(r'^(?P<shop>.*)/(?P<header_title>.*)/$', views.page_detail),
    url(r'^upload_image', views.upload_image),
]