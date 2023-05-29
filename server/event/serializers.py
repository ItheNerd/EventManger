from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["event_name", "date", "time", "location", "image"]
        extra_kwargs = {"image": {"required": False}}  # Make the image field optional
