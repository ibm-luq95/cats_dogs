from django.urls import path, include
from .views import (HomeView, SingleView, OwnerView, CatsView, DogsView)



urlpatterns = [
    path('', HomeView.as_view(), name="home-page"),
    path("pet/<int:pk>", SingleView.as_view(), name="single-page"),
    path("owner/<int:pk>", OwnerView.as_view(), name="owner-page"),
    path("cats/", CatsView.as_view(), name="cats-page"),
    path("dogs/", DogsView.as_view(), name="dogs-page"),
]