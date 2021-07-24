from django.urls import path
from .views import OwnerCourseListView, OwnerEditView

urlpatterns = [
    path('courses', OwnerCourseListView.as_view(), name='instructor_courses'),
    path('course/<pk>', OwnerEditView.as_view(), name='instructor_view_update_course'),
]