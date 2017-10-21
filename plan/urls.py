from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home_page'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register/yplan/', views.yearplan, name='yearplan'),
]
