# advanced-api-project/urls.py
from django.contrib import admin
from django.urls import path, include  # must import include
from rest_framework.authtoken.views import obtain_auth_token

# The only urlpatterns list
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # <- must exist exactly like this
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

