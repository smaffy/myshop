from django import forms
from localflavor.ee.forms import EEZipCodeField
from .models import Order


class OrderCreateForm(forms.ModelForm):
    postal_code = EEZipCodeField

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
