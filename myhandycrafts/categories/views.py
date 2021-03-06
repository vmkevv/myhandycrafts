"""Category views."""

# Django REST Framework
from rest_framework import mixins,viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Permisions
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny

# Serilizers
from myhandycrafts.categories.serializers import (
    CategoryModelSerializer,
    CategoryListSerializer,
)



# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
# from django_filters.rest_framework import DjangoFilterBackend

# Models
from myhandycrafts.categories.models import Category

# Pagination
from myhandycrafts.utils.pagination import MyHandycraftsPageNumberPagination


# time
from django.utils import timezone

class CategoryAdminViewSet( mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    """Category view set."""

    serializer_class = CategoryModelSerializer
    pagination_class = MyHandycraftsPageNumberPagination
    # filter name
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('name','count_post','count_craftman','created_at',)
    # filter_fields = ('name')

    queryset = Category.objects.filter(active=True)
    permission_classes = [IsAdminUser]


    def perform_destroy(self, instance):
        instance.active=False
        instance.deleted_at = timezone.now()
        instance.save()
        """assing polices"""



class CategoryListViewSet(mixins.ListModelMixin,
                          viewsets.GenericViewSet):
    serializer_class = CategoryListSerializer
    # pagination_class = MyHandycraftsPageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('name', 'count_post', 'count_craftman', 'created_at',)
    # filter_fields = ('name')

    queryset = Category.objects.filter(active=True)

class CategoryViewSet(
                        mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    """Category view set."""

    serializer_class = CategoryModelSerializer
    pagination_class = MyHandycraftsPageNumberPagination
    # filter name
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('name',
                       'count_post',
                       'count_craftman',
                       'created_at',)
    # filter_fields = ('name')

    queryset = Category.objects.filter(active=True)



