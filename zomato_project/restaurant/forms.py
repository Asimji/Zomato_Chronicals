from django import forms
from .models import *

class DishForm(forms.ModelForm):
    class Meta:
        model=Dish
        fields=['dish_name','price']
