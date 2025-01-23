from django.db import models


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
