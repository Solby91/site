from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<category_slug>[-\w]+)/$', views.GoodsList, name='GoodsByCategory'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.GoodPage, name='PageWithGood'),
    url(r'^$', views.GoodsList, name='CategoryList'),
]