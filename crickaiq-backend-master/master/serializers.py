from rest_framework import serializers
from .models import *


class CountrySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Country
        fields = (
            "id",
            "object_id",
            "long_name",
            "abbreviation",
            "image_url",
            "link_code",
            "created_on",
            "modified_on"
        )

    def create(self, validated_data):
        instance = Country(**validated_data)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.object_id = validated_data.get("object_id", instance.object_id)
        instance.long_name = validated_data.get("long_name", instance.long_name)
        instance.abbreviation = validated_data.get("abbreviation", instance.abbreviation)
        instance.image_url = validated_data.get("image_url", instance.image_url)
        instance.link_code = validated_data.get("link_code", instance.link_code)
        instance.modified_on = validated_data.get("modified_on", instance.modified_on)
        instance.save()
        return instance