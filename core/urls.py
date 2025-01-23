from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CheckEmailViewSet

# Define the router and register the viewset
router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
# router.register(r"check-email", CheckEmailViewSet.as_view(), basename="check-email")

urlpatterns = [
    path("", include(router.urls)),  # Include router URLs
    path("check-email/", CheckEmailViewSet.as_view(), name="check-email"),
]
