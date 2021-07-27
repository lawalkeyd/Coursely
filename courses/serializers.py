from os import name
from rest_framework import serializers
from .models import Module, Text, Video, Image, File, Content, Course
from django.apps import apps

class CourseSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Course
        fields = '__all__'

class ModuleSerializer(serializers.ModelSerializer):
    #contents = serializers.PrimaryKeyRelatedField(many=True, queryset=Content.objects.all())

    class Meta:
        model = Module
        fields = '__all__'
      
class ContentSerializer(serializers.ModelSerializer):
    module = ModuleSerializer()
    class Meta:
        model = Content
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


