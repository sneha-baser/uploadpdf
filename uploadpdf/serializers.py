from rest_framework import serializers
from .models import uploadfile
from .models import uploadxmlfile
from .models import uploadcsvfile
from .models import Configuration

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = uploadfile 
        fields = '__all__'
class XmlFileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = uploadxmlfile
        fields = '__all__'
class CsvFileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = uploadcsvfile
        fields = '__all__'
