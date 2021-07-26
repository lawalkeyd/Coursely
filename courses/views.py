from django.shortcuts import render
from rest_framework import serializers
from .models import Content, Course, Module, File
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import FileSerializer, ModuleSerializer, CourseSerializer


class ListCreateCourseView(CreateAPIView):
    model = Course
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner = qs.request.user)   

class EditCourseView(RetrieveUpdateDestroyAPIView):
    model = Course
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner = qs.request.user)   

class ListCreateModuleView(CreateAPIView):
    model = Module
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(course_owner = qs.request.user)   

class EditModuleView(RetrieveUpdateDestroyAPIView):
    model = Module
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(course_owner = qs.request.user)         



class AddFileView(CreateAPIView):
    model = File
    serializer_class = FileSerializer
