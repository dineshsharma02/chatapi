from django.shortcuts import render
from .serializers import GenericFileUploadSerializer
from rest_framework.viewsets import ModelViewSet
from .models import GenericFileUpload
# Create your views here.

class GenericFileUploadView(ModelViewSet):
    class Meta:
        serializer_class = GenericFileUploadSerializer
        queryset = GenericFileUpload.objects.all()
        


