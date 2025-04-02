from django.contrib import admin
from django.urls import path, include

api_routers = [
    path('v1/', include('api_v1.urls'))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_routers)),
]
