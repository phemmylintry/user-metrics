from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', admin.site.urls),
    path('send_email/', include('metrics.urls', namespace='metrics'))
]
