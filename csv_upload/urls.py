from django.urls import path
from .views import upload_file, file_list, search_products

urlpatterns = [
    path('upload/', upload_file, name='upload_file'),  # Upload CSV Page
    path('files/', file_list, name='file_list'),  # Show Processed Data
    path('search/', search_products, name='search_products'),  # Search Feature
]
