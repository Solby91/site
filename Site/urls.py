from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from about.views import show_about
from contacts.views import show_contacts
from delivery.views import show_delivery
from payment.views import show_payment
from main.views import show_main


urlpatterns = [
    url(r'^cupons/', include('cupons.urls', namespace='cupon')),
    url(r'^order/', include('orders.urls', namespace='orders')),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^catalog/', include('catalog.urls', namespace='catalog')),
    url(r'^payment/', show_payment, name='ShowPayment'),
    url(r'^delivery/', show_delivery, name='ShowDelivery'),
    url(r'^contacts/', show_contacts, name='ShowContacts'),
    url(r'^about/', show_about, name='ShowAbout'),
    url(r'^admin/', admin.site.urls),
    url(r'^$', show_main, name='MainPage'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
