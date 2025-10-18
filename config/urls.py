from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('animais/', include(('animais.urls', 'animais'), namespace='animais')),
    path('fazendas/', include(('fazendas.urls', 'fazendas'), namespace='fazendas')),
    path('', include(('rumix.urls', 'rumix'), namespace='rumix')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
