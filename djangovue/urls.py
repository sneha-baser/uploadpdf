from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from uploadpdf import views

router = DefaultRouter()

router.register('upload', views.FileUploadViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]