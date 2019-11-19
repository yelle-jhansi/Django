from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import JsonData
from .serializers import JsonDataSerializer


class ListJsonDataView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = JsonData.objects.all()
    serializer_class = JsonDataSerializer
