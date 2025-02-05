from rest_framework import serializers
from .models import UserData, RegisterUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = [
            "id",
            "name",
            "email",
            "date_of_birth",
            "age",
            "gender",
            "isTermsAccepted",
            "isPrivacyPolicyAccepted",
            "privacyLevel",
        ]  # Include 'id' for easy identification


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterUser
        fields = [
            "id",
            "name",
            "email",
            "password",
            "phone_number",
            "salary",
        ]  # Include 'id' for easy identification
