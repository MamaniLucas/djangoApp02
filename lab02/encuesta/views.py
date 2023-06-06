from django.shortcuts import render

# Create your views here.


# Create your views here.

#REquest El objeto de solicitud utilizado para generar esta respuesta.

def index(request):
    context = {
        'titulo': "Formulario",
    }
    return render(request, 'encuesta/formulario.html', context)
#Un diccionario de valores para agregar al contexto de la plantilla. 
# Por defecto, este es un diccionario vacío. Si se puede llamar a
# un valor en el diccionario, la vista lo llamará justo antes 
# de representar la plantilla

def enviar(request):
    context={
        'titulo': "Respuesta",
        'nombre': request.POST['nombre'],
        'clave': request.POST['password'],
        'educacion': request.POST['educacion'],
        'nacionalidad': request.POST['nacionalidad'],
        'idiomas': request.POST.getlist('idiomas'),
        'correo': request.POST['email'],
        'website': request.POST['sitioweb'],


    }
    return render(request, 'encuesta/respuesta.html', context)

#Ejercicio
def calcular(request):
    
    context = {
        'titulo': "Formulario",
        #'Valor 1': request.POST['num1'],
       # 'Valor 1': request.POST['num2'],
        
    }    
    c=''
    try:
         if request.method=="POST":
                
                n1=eval(request.POST.get('num1'))
                n2=eval(request.POST.get('num2'))
                opr=request.POST.get('opcion')
                if opr=="sum":
                    c=n1+n2
                elif opr=="res":
                    c=n1-n2
                elif opr=="mul":
                    c=n1*n2
                elif opr=="div":
                    c=n1/n2;     
                
                
    except:
        c="invalid .."
        print(c)
        
        return render(request, 'encuesta/datos.html', {'c':c}, context)
   

    
    

