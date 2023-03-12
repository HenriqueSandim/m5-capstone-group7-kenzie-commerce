from django.urls import include, path

from .views import UsersViews, UserManageViews
from rest_framework_simplejwt import views as jwt_view

urlpatterns = [
    path("users/", UsersViews.as_view()),
    path("users/<str:user_id>/", UserManageViews.as_view()),
    path("login/", jwt_view.TokenObtainPairView.as_view()),
    path('login/refresh/', jwt_view.TokenRefreshView.as_view()),
]
