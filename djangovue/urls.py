from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from uploadpdf import views
from django.conf import settings
from django.conf.urls.static import static
router = DefaultRouter()

router.register('upload', views.FileUploadViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)