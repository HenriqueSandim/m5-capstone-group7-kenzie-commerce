from django.urls import path
from rest_framework import views
from .views import CartView

urlpatterns = [
    path("cart/", CartView.as_view()),
    # path("cart/<str:product_id>/", CartDetailView.as_view()),
]
