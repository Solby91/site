from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^apply', views.cupon_apply, name='apply')
]