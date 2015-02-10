from django import forms
from webform.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address', 'plan']
