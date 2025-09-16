from django.urls import path
from .views import BookList
from django.urls import path, include

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # <- Add this line
]

