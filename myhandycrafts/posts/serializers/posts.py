""""Post serialisers."""

# Django REST Framework
from rest_framework import serializers

# models
from myhandycrafts.posts.models import Post


class PostModelSerializer(serializers.ModelSerializer):
    """Post Model Serializer."""
    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'title',
            'description',
            'price',
            'cuantitie',
            'state',
            'created_at',
            'updated_at',
        )