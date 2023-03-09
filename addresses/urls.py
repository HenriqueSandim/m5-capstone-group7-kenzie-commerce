from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("users/", views.AddressView.as_view()),
    path("users/<int:pk>/", views.AddressDetailView.as_view()),
]