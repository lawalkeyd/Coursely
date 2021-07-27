from django.urls import path
from .views import AddFileView, ListCreateModuleView, ListCreateCourseView, EditCourseView, EditModuleView

urlpatterns = [
    path('', ListCreateCourseView.as_view(), name='add_list_course'),
    path('<pk>', EditCourseView.as_view(), name='edit_course'),
    path('module/', ListCreateModuleView.as_view(), name='add_list_modules'),
    path('module/<pk>', EditModuleView.as_view(), name='edit_module'),
    path('content/add/', AddFileView.as_view(), name='add_module_content'),
]