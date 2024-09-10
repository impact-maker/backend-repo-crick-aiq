from rest_framework import serializers
from .models import *
from account.models import User
from account.serializers import UserSerializer


class PredictionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(required=False, queryset=User.objects.all(), allow_null=True)
    user_data = UserSerializer(required=False, allow_null=True)
    
    class Meta:
        model = Prediction
        fields = (
            "user",
            "user_data",
            "country_b",
            "format",
            "match_date",
            "banner_picture",
            "result",
            "status",
            "created_on",
            "modified_on"
        )

    def create(self, validated_data):
        instance = Prediction(**validated_data)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.user = validated_data.get("user", instance.user)
        instance.country_b = validated_data.get("country_b", instance.country_b)
        instance.format = validated_data.get("format", instance.format)
        instance.match_date = validated_data.get("match_date", instance.match_date)
        instance.banner_picture = validated_data.get("banner_picture", instance.banner_picture)
        instance.result = validated_data.get("result", instance.result)
        instance.status = validated_data.get("status", instance.status)
        instance.modified_on = validated_data.get("modified_on", instance.modified_on)
        instance.save()
        return instance
    

class AnalysisSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(required=False, queryset=User.objects.all(), allow_null=True)
    user_data = UserSerializer(required=False, allow_null=True)
    
    class Meta:
        model = Prediction
        fields = (
            "user",
            "user_data",
            "result",
            "type",
            "created_on",
            "modified_on"
        )

    def create(self, validated_data):
        instance = Prediction(**validated_data)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.user = validated_data.get("user", instance.user)
        instance.result = validated_data.get("result", instance.result)
        instance.type = validated_data.get("type", instance.type)
        instance.modified_on = validated_data.get("modified_on", instance.modified_on)
        instance.save()
        return instance