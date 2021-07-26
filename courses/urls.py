from django.urls import path
from .views import AddContentView, AddUpdateModule

urlpatterns = [
    path('modules/', AddUpdateModule.as_view(), name='add_update_modules'),
    path('content/add/', AddContentView.as_view(), name='add_module_content'),
]