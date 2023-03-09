from django.urls import include, path

# from .views import 
from .views import UsersViews

urlpatterns = [
    path("users/", UsersViews.as_view()),
]