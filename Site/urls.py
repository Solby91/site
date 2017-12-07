from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^order/', include('orders.urls', namespace='orders')),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^catalog/', include('catalog.urls', namespace='catalog')),
    url(r'^admin/', admin.site.urls),
]
