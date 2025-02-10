from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.core.exceptions import ValidationError
import re
from django.core.validators import validate_email
from .models import UserData, RegisterUser
from .serializers import UserSerializer, RegisterUserSerializer
from rest_framework import viewsets


class RegisterUserViewSet(viewsets.ModelViewSet):
    queryset = RegisterUser.objects.all()
    serializer_class = RegisterUserSerializer


class UserViewSet(ViewSet):
    """
    A ViewSet for handling GET and POST requests for the User model.
    """

    def list(self, request):
        """Handles GET requests to retrieve all users."""
        users = UserData.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handles POST requests to create a new user."""
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class CheckEmailViewSet(ViewSet):
#     """
#     A ViewSet for handling GET requests to check if an email exists.
#     """

#     """Handles GET requests to check if an email exists."""

#     def list(self, request):
#         email = request.query_params.get("email")
#         print(email)
#         if email:
#             isAvailable = UserData.objects.filter(email=email).exists()
#             return Response({"isAvailable": isAvailable}, status=status.HTTP_200_OK)
#         return Response(
#             {"error": "Email parameter is required"}, status=status.HTTP_400_BAD_REQUEST
#         )


class CheckEmailViewSet(APIView):
    """
    A ViewSet for handling GET requests to check if an email exists.
    """

    def is_valid_email(self, email: str) -> bool:
        """
        Helper method to check if the email format is valid.
        """
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(email_regex, email) is not None

    def get(self, request):
        email = request.query_params.get("email")

        # Validate that the email is provided
        if not email:
            return Response(
                {"error": "Email parameter is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Validate email format
        if not self.is_valid_email(email):
            return Response(
                {"error": "Invalid email format"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Check if the email exists in the database
        is_available = not RegisterUser.objects.filter(email=email).exists()
        print(is_available)
        return Response({"isAvailable": is_available}, status=status.HTTP_200_OK)
