from rest_framework import serializers
from .models import RemindMeLater

class RemindMeLaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RemindMeLater
        fields = '__all__'