from os import name
from typing import Optional
from rest_framework import serializers
from .models import Module, Text, Video, Image, File, Course



class CourseSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    slug = serializers.CharField(read_only=True, required = False)

    class Meta:
        model = Course
        fields = '__all__'
        



class TextSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Text
        fields = '__all__'
        read_only_fields = ('created', 'updated')
        

class VideoSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Video
        fields = '__all__'
        read_only_fields = ('created', 'updated')

class ImageSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Image
        fields = '__all__'
        read_only_fields = ('created', 'updated')

class FileSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = File
        fields = '__all__'
        read_only_fields = ('created', 'updated')

class ModuleSerializer(serializers.ModelSerializer):
    text = TextSerializer(many=True, required=False)
    images = ImageSerializer(many=True, required=False)
    videos = VideoSerializer(many=True, required=False)
    files = FileSerializer(many=True, required=False)
    
    class Meta:
        model = Module
        fields = '__all__'
      
    def create(self, validated_data):
        text = validated_data.pop('text', None)
        images = validated_data.pop('images', None)
        videos = validated_data.pop('videos', None)
        files = validated_data.pop('files', None)
        module = Module.objects.create(**validated_data)
        if text:
            for data in text:
                Text.objects.create(module=module, **data)
        if videos:
            for data in text:
                Video.objects.create(module=module, **data)                
        if images:
            for data in text:
                Image.objects.create(module=module, **data)
        if files:
            for data in text:
                File.objects.create(module=module, **data)
        return module

# class ContentSerializer(serializers.RelatedField):
#     module = ModuleSerializer()

#     class Meta:
#         model = Content
#         fields = '__all__'
