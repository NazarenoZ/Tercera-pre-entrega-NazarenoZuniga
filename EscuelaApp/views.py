from django.shortcuts import render, redirect
from EscuelaApp.models import Curso, Alumno, Profesor, EscuelaApp
from EscuelaApp.forms import CursoFormulario, AlumnosFormulario, ProfesoresFormulario
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages

# Create your views here.
def inicio(request):
    return render(request, "padre.html")

def alta_curso(request,nombre):
    curso = Curso(nombre=nombre , camada=234512)
    curso.save()
    texto = f"Se guardo en la BD el curso: {curso.nombre} {curso.camada}"
    return HttpResponse(texto)

def ver_cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def alumnos(request):
    return render(request, "alumnos.html")

def curso_formulario(request):
    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST)
        if mi_formulario.is_valid():
            try:
                datos = mi_formulario.cleaned_data
                nombre = datos.get("nombre")
                camada = datos.get("camada")
                fecha_inicio = datos.get("fecha_inicio")
                fecha_fin = datos.get("fecha_fin")
                curso = Curso(nombre=nombre, camada=camada, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin)
                curso.save()
                return redirect("home")  
            except Exception as e:
                return HttpResponse(f"Error al guardar el curso: {e}")
    else:
        mi_formulario = CursoFormulario()
    return render(request, "formulario.html", {"form": mi_formulario})
def buscar_curso(request):
    return render(request, "buscar_curso.html")

def buscar(request):
    nombre = request.GET.get("nombre")
    if nombre:
        cursos = Curso.objects.filter(nombre__icontains=nombre)
        return render(request, "resultado_busqueda.html", {"cursos": cursos})
    else:
        return render(request, "mensaje_error.html", {"mensaje": "Ingrese el nombre del curso"})


def profesores(request):
    
    return render(request, "profesores.html")

def profesores_formulario(request):
    if request.method == "POST":
        mi_formulario = ProfesoresFormulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profesor = Profesor(nombre=datos["nombre"], apellido=datos["apellido"], curso=datos["curso"])
            profesor.save()
            return redirect("home")
    else:
        mi_formulario = ProfesoresFormulario()
    return render(request, "formulario.html", {"form": mi_formulario})

def agregar_alumno(request):
    if request.method == "POST":
        form = AlumnosFormulario(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            nombre = datos.get("nombre")
            apellido = datos.get("apellido")
            curso = datos.get("curso")
            edad = datos.get("edad")
            alumno = Alumno(nombre=nombre, apellido=apellido, curso=curso, edad=edad)
            alumno.save()
            return redirect('confirmacion_alumno') 
        else:
            messages.error(request, '¡Hubo un problema con los datos del formulario! Por favor, revisa los campos.')
    else:
        form = AlumnosFormulario()
    return render(request, 'alumnos.html', {'form': form})

def agregar_profesor(request):
    if request.method == "POST":
        form = ProfesoresFormulario(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            nombre = datos.get("nombre")
            apellido = datos.get("apellido")
            curso = datos.get("curso")
            especialidad = datos.get("especialidad")
            profesor = Profesor(nombre=nombre, apellido=apellido, curso=curso, especialidad=especialidad)
            profesor.save()
            return redirect('confirmacion_profesor')  
        else:
            messages.error(request, '¡Hubo un problema con los datos del formulario! Por favor, revisa los campos.')
    else:
        form = ProfesoresFormulario()
    return render(request, 'profesores.html', {'form': form})

def elimina_curso(request , id ):
    curso = Curso.objects.get(id=id)
    curso.delete()

    curso = Curso.objects.all()

    return render(request , "cursos.html" , {"cursos":curso})




def editar(request , id):

    curso = Curso.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = CursoFormulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos["nombre"]
            curso.camada = datos["camada"]
            curso.save()

            curso = Curso.objects.all()

            return render(request , "cursos.html" , {"cursos":curso})


        
    else:
        mi_formulario = CursoFormulario(initial={"nombre":curso.nombre , "camada":curso.camada})
    
    return render( request , "editar_curso.html" , {"mi_formulario": mi_formulario , "curso":curso})
def home(request):
    historia_escuela = "La EscuelaApp fue fundada en Allen, Río Negro, Argentina, en 1976 por una familia de campo que llego al sur desde el norte con mucha ambision por tener su propia escuela y asi armar su historia..."
    return render(request, "home.html", {"historia_escuela": historia_escuela})

def registro_escuela(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        direccion = request.POST.get("direccion")
        numero_de_telefono = request.POST.get("numero_de_telefono")
        
        escuela = EscuelaApp(nombre=nombre, direccion=direccion, numero_de_telefono=numero_de_telefono)
        escuela.save()
        
        return render(request, "confirmacion_registro.html")
    else:
        return render(request, "registro_escuela.html")
    

def confirmacion_profesor(request):
    return render(request, 'confirmacion_profesor.html')

def confirmacion_alumno(request):
    return render(request, 'confirmacion_alumno.html')