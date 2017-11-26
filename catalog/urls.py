from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='catalog'),
    url(r'^(?P<slug>[-\w]+)/$', views.show_catalog, name='category'),
    url(r'^(?P<slug>[-\w]+)/$', views.GoodsList, name='GoodsList'),
]