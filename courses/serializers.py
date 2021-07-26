from os import name
from rest_framework import serializers
from .models import Module, Text, Video, Image, File, Content
from django.apps import apps

class AddUpdateModuleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'


class AddTextSerializers(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = '__all__'
        read_only_fields = ('created', 'updated')

class AddVideoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Video
        read_only_fields = ('created', 'updated')

class AddImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Image
        read_only_fields = ('created', 'updated')

class AddFileSerializers(serializers.ModelSerializer):
    class Meta:
        model = File
        read_only_fields = ('created', 'updated')


class AddContentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=20)
    module_id = serializers.IntegerField()
    image = AddImageSerializers(required=False)
    file = AddFileSerializers(required = False)
    video = AddVideoSerializers(required = False)
    text = AddTextSerializers(required=False)

    class Meta:
        model = Content
        fields = '__all__'

    def create(self, validated_data):
        model_name = validated_data.pop('name')
        module_id = validated_data.pop('module_id')
        item= apps.get_model(app_label='courses', model_name=model_name).objects.create(**validated_data)
        module = Module.objects.get(id=module_id)
        t = Content(module=module, item=item)
        t.save()
        return t


