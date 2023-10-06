from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('mkuapi/', include('mkuapi.urls')),
    path('admin/', admin.site.urls),
]
