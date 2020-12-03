from rest_framework import serializers 
from .models import Menu

class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model   = Menu
        fields  = ["category","name","breakfast","lunch","dinner","takeout","price","allergy"]

