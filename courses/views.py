from django.shortcuts import render
from rest_framework import serializers
from .models import Content, Module
from rest_framework.generics import CreateAPIView
from .serializers import AddContentSerializer, AddUpdateModuleSerializers



class AddUpdateModule(CreateAPIView):
    model = Module
    serializer_class = AddUpdateModuleSerializers
    queryset = Module.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(course_owner = qs.request.user)    

class AddContentView(CreateAPIView):
    model = Content
    serializer_class = AddContentSerializer
