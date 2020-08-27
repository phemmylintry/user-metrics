from django.urls import path
from . views import SendUserEmails

app_name = "metrics"

urlpatterns = [
    path('email_users/', SendUserEmails.as_view(), name='email')
]
