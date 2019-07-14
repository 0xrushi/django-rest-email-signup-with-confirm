from rest_framework import serializers
from .models import  StickerData

class StickerSerializer(serializers.ModelSerializer):
    class Meta():
        model = StickerData
        fields = "__all__"
