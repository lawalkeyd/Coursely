from rest_framework import serializers
from courses.models import Course


class OwnerViewCourses(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('subject', 'title', 'slug', 'overview')
