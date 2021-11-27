from rest_framework import serializers
from .models import uploadfile


class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = uploadfile
        fields = '__all__'