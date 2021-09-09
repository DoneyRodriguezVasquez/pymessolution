from django import forms
from .models import Contactos


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contactos
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su email',
                    'id': 'email',
                    'name': 'email',
                    'required': 'required',
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre',
                    'id': 'nombre',
                    'name': 'nombre',
                    'required': 'required',
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su teléfono',
                    'id': 'telefono',
                    'name': 'telefono',
                    'required': 'required',
                }
            ),
            'mensaje': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su mensaje',
                    'id': 'mensaje',
                    'name': 'mensaje',
                    'rows': '5',
                    'required': 'required',
                }
            ),
        }