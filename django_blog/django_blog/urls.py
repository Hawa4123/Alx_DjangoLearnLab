from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # auth-related URLs (register, login, profile)
    # You can add blog home or posts URLs here later. For now a simple index:
    path('', TemplateView.as_view(template_name='blog/index.html'), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
