from django.urls import path, include
from .views import (DashboardView, UpdatePetView, CreatePetView, DeletePetView)




urlpatterns = [
   path("", DashboardView.as_view(), name="dashboard-home"),
   path("add", CreatePetView.as_view(), name="dashboard-add-pet"),
   path("edit/<int:pk>", UpdatePetView.as_view(), name="dashboard-edit-pet"),
   path("delete/<int:pk>", DeletePetView.as_view(), name="dashboard-delete-pet"),
]