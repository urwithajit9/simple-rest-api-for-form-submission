from django.contrib import admin
from .models import UserData, RegisterUser

# Register your models here.


@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "email",
        "date_of_birth",
        "age",
        "gender",
        "isTermsAccepted",
        "isPrivacyPolicyAccepted",
        "privacyLevel",
    ]


@admin.register(RegisterUser)
class RegisterUserAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "email",
        "password",
        "phone_number",
        "salary",
    ]
