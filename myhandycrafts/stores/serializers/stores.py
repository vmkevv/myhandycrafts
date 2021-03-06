"""Store serializer."""

# Django REST Framework
from rest_framework import serializers

# Models
from myhandycrafts.stores.models import Store

# Django
from django.utils.translation import ugettext_lazy as _

# Serializers
from myhandycrafts.users.serializers import UserShortDetailSerializer
from myhandycrafts.maps.serializers import MunicipalityListSerializer
# from myhandycrafts.stores.serializers.storemedias import StoreMediaModelSerializer
from myhandycrafts.stores.serializers.storemedias import StoreMediaModelSerializer



class GPSSerializer(serializers.Serializer):
    """Gps Serializer"""
    latitude=serializers.CharField()
    longitude=serializers.CharField()



class StoreModelSerializer(serializers.ModelSerializer):
    """Store model serializer"""
    gps = GPSSerializer(many=False,allow_null=True)

    class Meta:
        model = Store
        fields = (
                'id',
                'user',
                'municipality',
                'name',
                'description',
                'location',
                'gps',
                'reputation',
                'publications',
                'visits',
                'created_at',
                'updated_at',
        )
        read_only_fields = (
            'reputation',
            'publications',
            'visits',
            'created_at',
            'updated_at',
        )

    def validate_user(self,data):
        user = self.context['user']
        if not user.is_staff:
            return user
        return data


class StoreDetailModelSerializer(serializers.ModelSerializer):
    user = UserShortDetailSerializer(many=False)
    municipality = MunicipalityListSerializer(many=False)
    storemedias = StoreMediaModelSerializer(many=True)
    gps = GPSSerializer(many=False)

    class Meta:
        model = Store
        fields = (
                'id',
                'user',
                'municipality',
                'name',
                'description',
                'location',
                'gps',
                'storemedias',
                'reputation',
                'publications',
                'visits',
                'created_at',
                'updated_at',
        )