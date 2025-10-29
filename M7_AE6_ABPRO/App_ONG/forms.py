from django import forms
from .models import Voluntario, Evento

class VoluntarioForm(forms.ModelForm):
    class Meta:
        model = Voluntario
        fields = ['nombre', "email", 'telefono']
        help_texts = {
            'email': 'Ingresa un correo válido, por ejemplo: usuario@dominio.com',
            'telefono': 'Ingresa el teléfono con código de país, por ejemplo: +56912345678',
        }

        
class EventoForm(forms.ModelForm):
    voluntarios = forms.ModelMultipleChoiceField(
    queryset=Voluntario.objects.all(),
    widget=forms.CheckboxSelectMultiple  
    )

    class Meta:
        model = Evento
        fields = ['titulo', 'fecha', 'voluntarios']