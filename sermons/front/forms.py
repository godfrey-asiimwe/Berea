from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your forms here.
from .models import subscribe


class ContactForm(forms.ModelForm):
    class Meta:
        model = subscribe
        fields = ("email",)
