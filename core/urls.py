from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CheckEmailViewSet, RegisterUserViewSet

# Define the router and register the viewset
router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"registeruser", RegisterUserViewSet, basename="registeruser")
# router.register(r"check-email", CheckEmailViewSet.as_view(), basename="check-email")

urlpatterns = [
    path("", include(router.urls)),  # Include router URLs
    path("check-email/", CheckEmailViewSet.as_view(), name="check-email"),
]

# /api/registeruser/

# GET	/registeruser/	List all registeruser
# POST	/registeruser/	Create a new registeruser
# GET	/registeruser/{id}/	registeruser
# PUT	/registeruser/{id}/	registeruser
# DELETE	/registeruser/{id}/	Delete an employee
