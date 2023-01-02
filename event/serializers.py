from rest_framework import serializers

from event.models import Client


class LittleDataClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name']


class AllDataClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
