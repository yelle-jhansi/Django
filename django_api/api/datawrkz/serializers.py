from rest_framework import serializers
from .models import JsonData


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JsonData
        fields = ("Date", "High")