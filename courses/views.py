from django.shortcuts import render
from .models import Course
from django.urls import reverse_lazy
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView
from .serializers import OwnerViewCourses


# Create your views here.

class OwnerCourseListView(ListAPIView):
    model = Course
    serializer_class = OwnerViewCourses

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerMixin(object):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user = qs.request.user)

class OwnerEditMixin(object):
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class OwnerCourseMixin(OwnerMixin):
    model = Course
    fields = ['subject', 'title', 'slug', 'overview']
    success_url = reverse_lazy('manage_course_list')

class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
    pass


