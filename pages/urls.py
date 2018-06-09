from django.conf.urls import url
from . import views

app_name = 'pages'

urlpatterns = [
    url(r'^create/$', views.page_create, name='create'),
    url(r'^list/$', views.page_list, name='list'),
    url(r'^edit/(?P<header_title>.*)/$', views.page_edit, name='edit'),
    url(r'^preview/(?P<shop>.*)/(?P<header_title>.*)/$', views.page_preview, name='preview'),
    url(r'^upload_image', views.upload_image),
]