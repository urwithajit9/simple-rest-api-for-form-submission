from rest_framework import serializers
from .models import UserData


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
