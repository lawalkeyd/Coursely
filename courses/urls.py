from django.urls import path
from .views import OwnerCourseListView

urlpatterns = [
    path('instructors/courses', OwnerCourseListView, name='instructor_courses')
]