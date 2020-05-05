"""Store url."""

# Django
from django.urls import include, path
# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import StoreViewSet,StoreMediaViewSet

router = DefaultRouter()
router.register(r'stores', StoreViewSet, basename='stores')
router.register(r'storemedias', StoreMediaViewSet, basename='storemedias')

urlpatterns = [
    path('', include(router.urls)),
]
