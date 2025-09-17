from django.urls import path
from .views import BookList
from django.urls import path, include

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)), 
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # <- Add this line
]


