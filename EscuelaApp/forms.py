from django import forms
from EscuelaApp.models import Curso, Alumno, Profesor, EscuelaApp

class CursoFormulario(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'camada', 'fecha_inicio', 'fecha_fin']
        widgets = {'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
                   'fecha_fin': forms.DateInput(attrs={'type': 'date'})}

class AlumnosFormulario(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'curso', 'edad'] 
      
class ProfesoresFormulario(forms.ModelForm):
    class Meta: 
        model = Profesor
        fields = ['nombre', 'apellido', 'curso', 'especialidad']
        

class EscuelaAppForm(forms.ModelForm):
    class Meta:
        model = EscuelaApp
        fields = ['nombre', 'direccion', 'numero_de_telefono']