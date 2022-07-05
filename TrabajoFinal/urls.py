from django.contrib import admin
from django.urls import path, include

#para las imagenes
from django.conf import settings
from django.conf.urls.static import static
from AppCoder import urls
from AppCoder import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AppCoder.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)