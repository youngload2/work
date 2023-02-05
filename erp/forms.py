from django import forms
from .models import *

class CoaForm(forms.ModelForm):
    class Meta :
        model = Coa
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta :
        model = Product
        fields = '__all__'