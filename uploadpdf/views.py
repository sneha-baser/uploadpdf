from rest_framework import viewsets
from .models import uploadfile
from .serializers import FileUploadSerializer


class FileUploadViewset(viewsets.ModelViewSet):
    queryset = uploadfile.objects.all()
    serializer_class = FileUploadSerializer
