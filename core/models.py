from django.db import models
from django.core.validators import MinLengthValidator


class UserData(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(default="2000-02-07")
    age = models.PositiveIntegerField()
    gender = models.CharField(
        max_length=10, choices=[("male", "Male"), ("female", "Female")], default="male"
    )
    isTermsAccepted = models.BooleanField(default=False)
    isPrivacyPolicyAccepted = models.BooleanField(default=False)
    privacyLevel = models.CharField(
        max_length=10,
        choices=[
            ("public", "Public"),
            ("private", "Private"),
            ("protected", "Protected"),
        ],
        default="public",
    )

    def __str__(self):
        return self.name


# this is not real user registration
# but just to do CRUD operation from front end.
class RegisterUser(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(
        max_length=128,
        validators=[MinLengthValidator(6)],
    )
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name
