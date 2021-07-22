from django.urls import path
from .views import OwnerCourseListView

urlpatterns = [
    path('instructors/courses', OwnerCourseListView.as_view(), name='instructor_courses')
]