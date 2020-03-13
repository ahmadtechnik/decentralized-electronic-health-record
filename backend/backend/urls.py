from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('records/', include('records.urls')),
    path('admin/', admin.site.urls),
]
