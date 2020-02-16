from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import OwnerCreationForm


def register(request):

    if request.method == "POST":
        register_form = OwnerCreationForm(request.POST)
        if register_form.is_valid():
            owner = register_form.save()
            owner.is_staff = True
            owner.save()
            messages.success(request, f"Your Account Created, you can login")
            return redirect("login")
    else:
        register_form = OwnerCreationForm()
        return render(request, 'users/register.html', context={"form": register_form})
    

