from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from beauty_city.views import render_index

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('booking/', include('booking.urls')),
    path('', render_index, name='index'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)