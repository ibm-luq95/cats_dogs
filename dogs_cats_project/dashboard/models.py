from django.db import models
from users.models import Owner


class Pet(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()
    avatar = models.ImageField(upload_to="avatars/")
    typed = models.CharField(max_length=5, choices=(("C", "Cats"), ("D", "Dogs")))
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, blank=True, null=True)
