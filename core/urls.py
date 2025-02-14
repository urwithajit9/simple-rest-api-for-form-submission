from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet,
    CheckEmailViewSet,
    RegisterUserViewSet,
    RegisterUserSearchView,
)

# Define the router and register the viewset
router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"registeruser", RegisterUserViewSet, basename="registeruser")


urlpatterns = [
    path("", include(router.urls)),  # Include router URLs
    path("check-email/", CheckEmailViewSet.as_view(), name="check-email"),
    path("search-users/", RegisterUserSearchView.as_view(), name="user-search"),
]

# /api/registeruser/

# GET	/registeruser/	List all registeruser
# POST	/registeruser/	Create a new registeruser
# GET	/registeruser/{id}/	registeruser
# PUT	/registeruser/{id}/	registeruser
# DELETE	/registeruser/{id}/	Delete an employee
