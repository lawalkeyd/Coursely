from django.shortcuts import render
from rest_framework import serializers
from .models import Content, Course, Module, File
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .serializers import FileSerializer, ModuleSerializer, CourseSerializer, ContentSerializer


class ListCreateCourseView(ListCreateAPIView):
    model = Course
    serializer_class = CourseSerializer

    def get_queryset(self):
        user = self.request.user
        return user.courses_created.all()

class EditCourseView(RetrieveUpdateDestroyAPIView):
    model = Course
    serializer_class = CourseSerializer

    def get_queryset(self):
        user = self.request.user
        return user.courses_created.all()

class ListCreateModuleView(ListCreateAPIView):
    model = Module
    serializer_class = ModuleSerializer

    def get_queryset(self):
        user = self.request.user
        return Module.objects.filter(course__owner = user)     

class EditModuleView(RetrieveUpdateDestroyAPIView):
    model = Module
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Module.objects.filter(course__owner = user)       



class AddFileView(CreateAPIView):
    model = Content
    serializer_class = ContentSerializer
