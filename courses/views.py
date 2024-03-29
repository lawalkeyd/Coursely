from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import permissions, serializers
from .models import Course, Module, File, Video, Image, Text
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .serializers import FileSerializer, ModuleSerializer, CourseSerializer, VideoSerializer, ImageSerializer, TextSerializer

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
    lookup_field = 'slug'

    def get_queryset(self):
        user = self.request.user
        return user.courses_created.all()
    

class ListCreateModuleView(ListCreateAPIView):
    model = Module
    serializer_class = ModuleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self, slug=None):
        user = self.request.user
        return Module.objects.filter(course__owner = user, course__slug=slug)     

class EditModuleView(RetrieveUpdateDestroyAPIView):
    model = Module
    serializer_class = ModuleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Module.objects.filter(course__slug=self.kwargs['slug'], pk=self.kwargs['pk'])
        return queryset                   



class AddFileView(CreateAPIView):
    model = File
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Module.objects.filter(course__owner = user)  

class AddImageView(CreateAPIView):
    model = Image
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Module.objects.filter(course__owner = user)      

class AddVideoView(CreateAPIView):
    model = Video
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Module.objects.filter(course__owner = user)  

class AddTextView(CreateAPIView):
    model = Text
    serializer_class = TextSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Module.objects.filter(course__owner = user)                              
        