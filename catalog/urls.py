from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.category_list, name='MainCatalog'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.category_list, name='CategoryList'),
    url(r'^(?P<category_slug>[-\w]+)/(?P<slug>[-\w]+)/$', views.good_page, name='GoodPage'),
]