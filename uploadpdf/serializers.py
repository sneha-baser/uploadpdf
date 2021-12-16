from rest_framework import serializers
from .models import uploadfile
from .models import uploadxmlfile


class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = uploadfile
        fields = '__all__'
class XmlFileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = uploadxmlfile
        fields = '__all__'
