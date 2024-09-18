from rest_framework import serializers
from django.utils.text import slugify
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(
        read_only=True
    )
    slug = serializers.SlugField(
        read_only=True,
    )
    class Meta:
        model = Customer
        fields = "__all__"

