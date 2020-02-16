from django.shortcuts import render
from django.views.generic import (TemplateView, DetailView, ListView)
from dashboard.models import Pet, Owner


class HomeView(ListView):
    template_name = "frontend/home.html"
    context_object_name = "all_pets"
    model = Pet
    ordering = ['-id']


class SingleView(DetailView):
    template_name = "frontend/single.html"
    model = Pet


class OwnerView(DetailView):
    template_name = "frontend/owner.html"
    model = Owner


class CatsView(ListView):
    template_name = "frontend/cats.html"
    model = Pet
    context_object_name = "all_cats_pets"

    def get_queryset(self):
        return Pet.objects.filter(typed="C")


class DogsView(ListView):
    template_name = "frontend/dogs.html"
    model = Pet
    context_object_name = "all_dogs_pets"

    def get_queryset(self):
        return Pet.objects.filter(typed="D")
