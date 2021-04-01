from rest_framework import serializers
from ..models import ProtocoloDetails

class ProtocoloDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProtocoloDetails
        fields = '__all__'
