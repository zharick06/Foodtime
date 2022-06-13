from dataclasses import field, fields
from django import forms
from .models import *

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'

class MeseroForm(forms.ModelForm):
    class Meta:
        model = Mesero
        fields =  '__all__'

class RestauranteForm(forms.ModelForm):
    class Meta:
        model = Restaurante
        fields =  '__all__'

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ["nombre", "valor", "categoria", "descripcion", "foto"]

class MesasForm(forms.ModelForm):
    class Meta:
        model = Mesas
        fields = ["nombre"]

class OfertaForm(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = ["descripcion", "pago"]

