from django import forms
from .models import Voluntario, Evento
from datetime import date

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
    widget=forms.CheckboxSelectMultiple,
    required=False,
    )

    class Meta:
        model = Evento
        fields = ['titulo', 'descripcion', 'fecha', 'voluntarios']
        widgets = {'fecha': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-control', 'min': date.today().isoformat(),})}
        help_texts = {
            'fecha': 'Seleccione la fecha del evento usando el calendario.',
        }

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        if fecha and fecha < date.today():
            raise forms.ValidationError("La fecha del evento no puede ser anterior a hoy.")
        return fecha