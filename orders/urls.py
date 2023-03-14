from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("orders/<int:pk>", views.OrderProductsView.as_view()),
    # path("orders/<int:pk>/", views.OrderProductsDetailView.as_view()),
]