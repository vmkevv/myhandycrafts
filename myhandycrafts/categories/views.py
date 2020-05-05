"""Category views."""

# Django REST Framework
from rest_framework import mixins,viewsets

# Permisions
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny

# Serilizers
from myhandycrafts.categories.serializers import CategoryModelSerializer


# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
# from django_filters.rest_framework import DjangoFilterBackend

# Models
from myhandycrafts.categories.models import Category

# time
from django.utils import timezone

class CategoryViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    """Category view set."""

    serializer_class = CategoryModelSerializer
    # filter name
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('name','created_at',)
    # filter_fields = ('name')

    queryset = Category.objects.filter(is_deleted=False)

    def get_permissions(self):
        """Assing permision base on action."""
        permissions = []
        if self.action in ['create','update']:
            permissions.append(IsAdminUser)
        else:
            permissions.append(AllowAny)
        return [permission() for permission in permissions]

    def perform_destroy(self, instance):
        instance.is_deleted=True
        instance.deleted_at = timezone.now()
        instance.save()



