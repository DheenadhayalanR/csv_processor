from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin
    path('', include('csv_upload.urls')),  # Include CSV Upload URLs
]
