from django.urls import path
from .views import AddUpdateModule

urlpatterns = [
    path('courses/modules/', AddUpdateModule.as_view(), name='add_update_modules'),
]