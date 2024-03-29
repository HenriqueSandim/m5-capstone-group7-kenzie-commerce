from django.urls import path
from .views import ProductView, ProductDetailView

urlpatterns = [
    path("products/", ProductView.as_view()),
    path("products/<str:product_id>/", ProductDetailView.as_view()),
]
