from rest_framework import serializers
from .models import *


class RoleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Role
        fields = (
            "id",
            "user_type",
            "role",
            "role_name",
            "status",
            "modified_on"
        )

    def create(self, validated_data):
        instance = Role(**validated_data)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.user_type = validated_data.get("user_type", instance.user_type)
        instance.role = validated_data.get("role", instance.role)
        instance.role_name = validated_data.get("role_name", instance.role_name)
        instance.status = validated_data.get("status", instance.status)
        instance.modified_on = validated_data.get("modified_on", instance.modified_on)
        instance.save()
        return instance
    

class UserSerializer(serializers.ModelSerializer):
    role = serializers.PrimaryKeyRelatedField(required=False, queryset=Role.objects.all(), allow_null=True)
    role_data = RoleSerializer(required=False, allow_null=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "password",
            "mobile",
            "role",
            "role_data",
            "name",
            "status",
            "picture",
            "country",
            "current_years",
            "is_admin",
            "is_active",
            "created_on",
        )
        read_only_fields = ["id", "created_on"]

    def create(self, validated_data):
        instance = User(**validated_data)
        instance.set_password(validated_data.get("password"))
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.name = validated_data.get("name", instance.name)
        instance.email = validated_data.get("email", instance.email)
        instance.mobile = validated_data.get("mobile", instance.mobile)
        instance.role = validated_data.get("role", instance.role)
        instance.country = validated_data.get("country", instance.country)
        instance.current_years = validated_data.get("current_years", instance.current_years)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.save()
        return instance

    def to_internal_value(self, data):
        if 'role_data' in data:
            data['role_data'] = None
        return super(UserSerializer, self).to_internal_value(data)