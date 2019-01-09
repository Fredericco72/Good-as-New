from django import forms

from .models import furniture

class furnitureForm(forms.ModelForm):
    
    class Meta:
        model = furniture
        fields = ('category','name','description','purchase_customer_id','purchase_price','sale_price')