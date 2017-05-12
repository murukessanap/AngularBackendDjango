from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^postJSON$', views.postJSON, name='postJSON'),
    url(r'^$', views.index, name='index')
]