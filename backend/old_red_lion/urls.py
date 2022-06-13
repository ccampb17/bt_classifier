from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from classifiers.views import classifiers
from upload.views import image_upload

urlpatterns = [
    path("upload", image_upload, name="upload"),
    path("classifiers", classifiers, name="classifiers"),
    path('admin/', admin.site.urls),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
