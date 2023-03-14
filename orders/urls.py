from django.urls import path
from . import views

urlpatterns = [
    path("orders/<int:pk>", views.OrderProductsView.as_view()),
    # path("orders/<int:pk>/", views.OrderProductsDetailView.as_view()),
]
