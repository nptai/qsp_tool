from django.conf.urls import url
from . import views

app_name = 'pages'

urlpatterns = [
    url(r'^$', views.home_page),
    url(r'^upload_image', views.upload_image),
    url(r'^page_create/', views.page_create, name='create'),
    url(r'^(?P<title>[\w-]+)/$', views.page_detail),
]
