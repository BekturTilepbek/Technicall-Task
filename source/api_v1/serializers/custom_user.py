from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from rest_framework import serializers

from accounts.models import MODERATOR, Moderator, Client
from accounts.validators import validate_username, validate_password

User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password", "email", "role", "is_active", "created_at", "updated_at"]
        read_only_fields = ["is_active", "created_at", "updated_at"]

    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
            email=validated_data["email"],
            role=validated_data["role"]
        )
        user.set_password(validated_data["password"])
        user.save()

        if user.role == MODERATOR:
            Moderator.objects.create(user=user)
        else:
            Client.objects.create(user=user)
        return user


    def validate_username(self, value):
        try:
            validate_username(value)
        except ValidationError as e:
            print(e.messages)
            raise serializers.ValidationError(e.messages)

        return value

    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)

        return value

