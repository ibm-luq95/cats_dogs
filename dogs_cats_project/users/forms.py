from .models import Owner
from django.contrib.auth.forms import UserCreationForm

class OwnerCreationForm(UserCreationForm):

    class Meta:
        model = Owner
        fields = ('first_name', 'last_name', 'username', 'email')