from django import forms
from .models import Product

class RegisterForm(forms.Form):
    name = forms.CharField(
        error_messages={
            'required': 'Please enter the product'
        }, 
        max_length=64, label='product_name'
    )

    price = forms.IntegerField(
        error_messages={
            'required': 'Please enter the price of your product'
        }, label='product_price'
    )

    description = forms.CharField(
        error_messages={
            'required': 'Please enter the description of your product'
        }, label='description'
    )

    stock = forms.IntegerField(
        error_messages={
            'required': 'Please enter the stock of your product'
        }, label='product_stock'
    )

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        price = cleaned_data.get('price')
        description = cleaned_data.get('description')
        stock = cleaned_data.get('stock')

        if not(name and price and description and stock):
            self.add_error('name', 'no values')
            self.add_error('price', 'no values')