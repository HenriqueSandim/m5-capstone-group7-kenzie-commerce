from django.urls import path
from rest_framework import views
from .views import CartView, CartDetailView

urlpatterns = [
    path("cart/", views.CartView.as_view()),
    path("cart/<int:id>/", views.CartDetailView.as_view()),
]
