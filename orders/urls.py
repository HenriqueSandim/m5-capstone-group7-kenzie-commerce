from django.urls import path
from . import views

urlpatterns = [
    path("orders/", views.OrderProductsView.as_view()),
    path("orders/<str:order_id>/", views.OrderProductsDetailView.as_view()),
]
