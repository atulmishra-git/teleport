from rest_framework import serializers
from .models import Tracker


class TrackerSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    tracking_number = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(format='%Y-%m-%dT%H:%M:%S.%fZ', read_only=True)

    class Meta:
        model = Tracker
        fields = "__all__"

