from django.shortcuts import render
from rest_framework import permissions
from .models import Course, Module, File, Video, Image, Text
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .serializers import FileSerializer, ModuleSerializer, CourseSerializer, VideoSerializer, ImageSerializer, 


class ListCreateCourseView(ListCreateAPIView):
    model = Course
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return user.courses_created.all()

class EditCourseView(RetrieveUpdateDestroyAPIView):
    model = Course
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return user.courses_created.all()

class ListCreateModuleView(ListCreateAPIView):
    model = Module
    serializer_class = ModuleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Module.objects.filter(course__owner = user)     

class EditModuleView(RetrieveUpdateDestroyAPIView):
    model = Module
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Module.objects.filter(course__owner = user)       


class AddFileView(CreateAPIView):
    model = File
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Module.objects.filter(course__owner = user)    

class AddFileView(CreateAPIView):
    model = File
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Module.objects.filter(course__owner = user)  

class AddFileView(CreateAPIView):
    model = File
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Module.objects.filter(course__owner = user)                  

