from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)