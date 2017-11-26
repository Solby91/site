from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show_catalog, name='catalog'),
    url(r'^(?P<slug>[-\w]+)/$', views.goods_slug, name='goods'),
]