from django import forms
from .models import Denuncia

class ReportForm(forms.ModelForm):
    archivo = forms.FileField(required=False, help_text="Por favor, adjunte solo archivos en formato PDF, MP4, MP3, JPG, JPEG o PNG.")

    class Meta:
        model = Denuncia
        fields = [
            'hecho_denunciado',
            'tipificacion_denuncia',
            'nombre',
            'apellidos',
            'telefono',
            'correo',
            'dni',
            'vinculo',
            'captcha',
            'archivo'
        ]
        labels = {
            'hecho_denunciado': 'Hecho denunciado*',
            'tipificacion_denuncia': 'Tipificación denuncia*',
            'vinculo': 'Vínculo con esta administración*',
        }

    def clean_archivo(self):
        archivo = self.cleaned_data.get('archivo', None)
        if archivo:
            tipos_permitidos = ['application/pdf', 'video/mp4', 'audio/mpeg', 'image/jpeg', 'image/png']
            if archivo.content_type not in tipos_permitidos:
                raise forms.ValidationError(f"Tipo de archivo no permitido: {archivo.content_type}")
        return archivo

class SearchForm(forms.Form):
    numero_denuncia = forms.CharField(label='Número de denuncia', required=False)
    fecha_inicio = forms.DateField(label='Fecha de inicio', widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    fecha_fin = forms.DateField(label='Fecha de fin', widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    tipificacion_denuncia = forms.ChoiceField(label='Tipificación denuncia', choices=[('', '---')] + Denuncia.TIPIFICACION_CHOICES, required=False)
