from django import forms
from .models import Divorcio, AsesoriaLegal

class SearchForm(forms.Form):
    # Campo de texto para la búsqueda
    query = forms.CharField(
        max_length=100,
        required=False,
        label='Buscar servicio',
        widget=forms.TextInput(attrs={'placeholder': 'Buscar...'})
    )
    # Opcional: Campo para elegir tipo de servicio
    tipo_servicio = forms.ChoiceField(
        choices=[('divorcio', 'Divorcio'), ('asesoria', 'Asesoría Legal')],
        required=False,
        label='Tipo de Servicio'
    )

# Formulario para el modelo Divorcio
class DivorcioForm(forms.ModelForm):
    class Meta:
        model = Divorcio
        fields = '__all__'  # Incluye todos los campos del modelo Divorcio

    # Validación personalizada (si es necesario)
    def clean_nombre_servicio(self):
        nombre = self.cleaned_data.get('nombre_servicio')
        if len(nombre) < 5:
            raise forms.ValidationError('El nombre del servicio debe tener al menos 5 caracteres.')
        return nombre

# Formulario para el modelo AsesoriaLegal
class AsesoriaLegalForm(forms.ModelForm):
    class Meta:
        model = AsesoriaLegal
        fields = '__all__'  # Incluye todos los campos del modelo AsesoriaLegal

    # Validación adicional en el campo especialidad
    def clean_especialidad(self):
        especialidad = self.cleaned_data.get('especialidad')
        if especialidad and len(especialidad) < 3:
            raise forms.ValidationError('La especialidad debe tener al menos 3 caracteres.')
        return especialidad
