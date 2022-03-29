from rest_framework import viewsets
from .models import uploadfile, uploadxmlfile , uploadcsvfile, Configuration
from .serializers import FileUploadSerializer, XmlFileUploadSerializer, CsvFileUploadSerializer
from xml.dom import minidom
from rest_framework.pagination import PageNumberPagination


class PostPagination(PageNumberPagination):
    page_size = 10


class FileUploadViewset(viewsets.ModelViewSet):
    queryset = uploadfile.objects.all() 
    serializer_class = FileUploadSerializer
    # pagination_class = PostPagination
class XmlFileUploadViewset(viewsets.ModelViewSet):
    queryset = uploadxmlfile.objects.all()
    serializer_class = XmlFileUploadSerializer
class CsvFileUploadViewset(viewsets.ModelViewSet):
    queryset = uploadcsvfile.objects.all()
    serializer_class = CsvFileUploadSerializer
    
