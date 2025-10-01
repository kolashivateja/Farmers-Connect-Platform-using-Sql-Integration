from django import forms
from .models import order,product

class Formorder(forms.ModelForm):
    STATUS_CHOICE=[
        ('pending','pending'),
        ('out for delivery','out for delivery'),
        ('deliverd','delivered'),
        ('canceled','canceled'),
    ]
    status=forms.ChoiceField(choices=STATUS_CHOICE, required=False)
    class Meta:
        model = order
        fields =['status']
class FormProduct(forms.ModelForm):
    STATUS_CHOICE=[
        ('Available','Available'),
        ('out of Stock','Out of Stock'),
        ('limited stock','limited stock'),
        ('few left harry up','few Left hurry up'),
        ('product sale closed','product sale closed'),
    ]
    price=forms.DecimalField(required=False)
    status=forms.ChoiceField(choices=STATUS_CHOICE, required=False)
    class Meta:
        model = product
        fields =['price','status']