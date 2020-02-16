from django import forms
from .models import Pet


class AddPetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['dob'].label = 'Date of Birth'

    class Meta:
        model = Pet
        fields = ("name", "dob", "avatar", "typed")
