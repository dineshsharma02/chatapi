from .models import GenericFileUpload
from rest_framework import serializers
class GenericFileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenericFileUpload
        fields = "__all__"