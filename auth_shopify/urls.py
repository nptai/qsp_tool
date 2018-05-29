from django.conf.urls import url
from . import views

app_name = 'auth_shopify'

urlpatterns = [
    url(r'^install', views.install),
    url(r'^connect', views.connect),
]
