from django.urls import path
from .views import ListCreateModuleView, ListCreateCourseView, EditCourseView, EditModuleView, AddFileView, AddImageView, AddTextView, AddVideoView

urlpatterns = [
    path('', ListCreateCourseView.as_view(), name='add_list_course'),
    path('<slug>', EditCourseView.as_view(), name='edit_course'),
    path('<slug>/module/', ListCreateModuleView.as_view(), name='add_list_modules'),
    path('<slug>/module/<pk>', EditModuleView.as_view(), name='edit_module'),
    path('module/add_content/text', AddTextView.as_view(), name='add_text'),
    path('module/add_content/video', AddVideoView.as_view(), name='add_video'),
    path('module/add_content/file', AddFileView.as_view(), name='add_file'),
    path('module/add_content/image', AddImageView.as_view(), name='add_image'),

]