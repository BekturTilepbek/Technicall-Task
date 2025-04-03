from django.urls import path, include

from api_v1.views.custom_user import RegisterAPIView

app_name = "api_v1"

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register')
]
