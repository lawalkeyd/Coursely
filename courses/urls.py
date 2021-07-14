from django.urls import path
from .views import ManageCourseListView

urlpatterns = [
    path('/instructors/courses', ManageCourseListView, name='instructor_courses')
]