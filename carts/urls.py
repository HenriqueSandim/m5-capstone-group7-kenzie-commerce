from django.urls import path
from rest_framework import views
from .views import CartView, CartDetailView

urlpatterns = [
    path("cart/", CartView.as_view()),
    path("cart/<int:id>/", CartDetailView.as_view()),
]
