
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('tutorial/', include('tutorial.urls')),
    path('donate/', include('donate.urls')),
]
