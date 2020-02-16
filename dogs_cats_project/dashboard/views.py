from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DeleteView
from .forms import AddPetForm
from .models import Pet, Owner
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.

class DashboardView(ListView):
    template_name = "dashboard/dashboard.html"
    model = Pet
    context_object_name = 'pet_list'
    ordering = ['-date_created']

    def get_queryset(self):
        own = self.request.user
        owner = Owner.objects.get(username=own)
        return Pet.objects.filter(owner=owner)


class UpdatePetView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Pet
    template_name = "dashboard/edit_pet.html"
    fields = ("name", "dob", "avatar", "typed")
    success_url = reverse_lazy('dashboard-home')
    success_message = "Updated Successfully!"
    pk_url_kwarg = 'pk'

    def test_func(self):
        pet = self.get_object()
        if self.request.user == pet.owner:
            return True
        return False


class CreatePetView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "dashboard/add_pet.html"
    model = Pet
    fields = ("name", "dob", "avatar", "typed")
    success_url = reverse_lazy('dashboard-home')
    success_message = "Pet Created Successfully!"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class DeletePetView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    template_name = "dashboard/delete_pet.html"
    model = Pet
    success_url = reverse_lazy('dashboard-home')
    success_message = "Deleted Successfully! "

    def test_func(self):
        pet = self.get_object()
        if self.request.user == pet.owner:
            return True
        return False
