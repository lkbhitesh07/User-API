from .models import CustomUser
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = [
            'id', 
            'first_name', 
            'last_name', 
            'company_name', 
            'age', 
            'city', 
            'state', 
            'zip', 
            'email', 
            'web'
            ]

class RestrictedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = [
            'id', 
            'first_name', 
            'last_name', 
            'company_name', 
            'age', 
            'city', 
            'state', 
            'zip', 
            'email', 
            'web'
            ]
        read_only_fields = ('id', 
            'company_name', 
            'city', 
            'state', 
            'zip', 
            'email', 
            'web')