from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from filebrowser.sites import site

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),  # Grappelli подключён первым
    path('admin/filebrowser/', site.urls),  # Filebrowser после Grappelli
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('posts/', include('posts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
