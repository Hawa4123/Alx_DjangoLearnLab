# advanced-api-project/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from api.views import YourModelViewSet  # adjust this import if needed

# Create DRF router for viewsets
router = DefaultRouter()
router.register(r'yourmodel', YourModelViewSet, basename='yourmodel')

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),

    # Include all API app URLs
    path('api/', include('api.urls')),

    # Token authentication endpoint
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    # Include DRF router URLs
    path('', include(router.urls)),
]
