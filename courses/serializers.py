from rest_framework import serializers
from .models import Module 

class AddUpdateModuleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'
        