from rest_framework import serializers
from .models import Course


class OwnerViewCourses(serializers.ModelSerializer):
    class Meta:
        model = Course
