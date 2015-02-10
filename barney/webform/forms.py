from django import forms


class OrderForm(forms.Form):
    address = forms.CharField(label='Address', max_length=256)
    plan = forms.CharField(label='Plan Name', max_length=75)
    # id = forms.CharField()