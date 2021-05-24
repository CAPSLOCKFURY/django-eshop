from .models import Product
from django.forms import ModelForm, TextInput, NumberInput


class ProductAddForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'category']

        widgets = {
            "title": TextInput(attrs={"placeholder": 'Название'}),
            "description": TextInput(attrs={"placeholder": 'Описание'}),
            "price": NumberInput()
        }
