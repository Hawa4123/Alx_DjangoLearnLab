# advanced-api-project/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),

    # Include API app URLs (must exist exactly for the check)
    path('api/', include('api.urls')),

    # Token authentication endpoint
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
