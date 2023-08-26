from rest_framework import serializers
from restapi.models import  users,dataset

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields ="__all__"

class dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = dataset
        fields ="__all__"