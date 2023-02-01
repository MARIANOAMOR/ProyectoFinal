from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
from AppCoder.models import Reparacion, Cliente, Proveedor, Repuesto, Avatar
from django.db.models import Q  #Lo uso para el buscador
from AppCoder.forms import ReparacionFormulario, ClienteFormulario, UserRegisterForm, UserEditForm

#Para el login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def clientes(request):
      cliente=Cliente.objects.all()
      return render(request, "AppCoder/gestionDeClientes.html", {"cliente":cliente})

def registrarCliente(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    telefono = request.POST['txtTelefono']
    email = request.POST['txtEmail']         
    direccion = request.POST['txtDireccion']
    observaciones = request.POST['txtObservaciones']
    cliente = Cliente.objects.create(codigo =codigo, nombre=nombre, apellido=apellido, telefono=telefono, email=email, direccion=direccion, observaciones=observaciones)
    messages.success(request, '¡Cliente registrado!')
    return redirect('/AppCoder/gestionDeClientes')

def edicionCliente(request, codigo):
    cliente = Cliente.objects.get(codigo=codigo)
    return render(request, "AppCoder/edicionCliente.html", {"cliente": cliente})
   

def editarCliente(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    telefono = request.POST['txtTelefono']
    email = request.POST['txtEmail']         
    direccion = request.POST['txtDireccion']
    observaciones = request.POST['txtObservaciones']
    cliente = Cliente.objects.get(codigo=codigo)
    cliente.nombre = nombre
    cliente.apellido = apellido
    cliente.telefono = telefono
    cliente.email = email
    cliente.direccion = direccion
    cliente.observaciones = observaciones    
    cliente.save()
    messages.success(request, '¡Cliente actualizado!')
    return redirect('/AppCoder/gestionDeClientes')

def leerClientes(request):
      clientes = Cliente.objects.all() #trae todos los clientes
      contexto= {"clientes":clientes} 
      return render(request, "AppCoder/leerClientes.html",contexto)

def eliminarCliente(request, codigo):
    cliente = Cliente.objects.get(codigo=codigo)
    cliente.delete()
    messages.success(request, '¡Cliente eliminado!')
    return redirect('/AppCoder/gestionDeClientes')

@login_required
def buscarCliente(request):        
    if request.GET["nombre"]:
        nombre = request.GET['nombre']
        cliente = Cliente.objects.filter(nombre__icontains=nombre)    
        return render(request, "AppCoder/cliente.html",{"cliente":cliente})

    else:
        respuesta = "No enviaste nada"
    return render(request,"AppCoder/inicio.html",{"respuesta":respuesta})

################################################################     Proveedores  ################################
def registrarProveedor(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    telefono = request.POST['txtTelefono']
    email = request.POST['txtEmail']         
    direccion = request.POST['txtDireccion']
    observaciones = request.POST['txtObservaciones']
    proveedor = Proveedor.objects.create(codigo =codigo, nombre=nombre, telefono=telefono, email=email, direccion=direccion, observaciones=observaciones)
    messages.success(request, '¡Provedor registrado!')
    return redirect('/AppCoder/gestionDeProveedores')

def proveedores(request):
      proveedor=Proveedor.objects.all()
      return render(request, "AppCoder/gestionDeProveedores.html", {"proveedor":proveedor})

def edicionProveedor(request, codigo):
    proveedor = Proveedor.objects.get(codigo=codigo)
    return render(request, "AppCoder/edicionProveedor.html", {"proveedor": proveedor})

def editarProveedor(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    telefono = request.POST['txtTelefono']
    email = request.POST['txtEmail']         
    direccion = request.POST['txtDireccion']
    observaciones = request.POST['txtObservaciones']
    proveedor = Proveedor.objects.get(codigo=codigo)
    proveedor.nombre = nombre
    proveedor.telefono = telefono
    proveedor.email = email
    proveedor.direccion = direccion
    proveedor.observaciones = observaciones    
    proveedor.save()
    messages.success(request, '¡Proveedor actualizado!')
    return redirect('/AppCoder/gestionDeProveedores')

def eliminarProveedor(request, codigo):
    proveedor = Proveedor.objects.get(codigo=codigo)
    proveedor.delete()
    messages.success(request, '¡Proveedor eliminado!')
    return redirect('/AppCoder/gestionDeProveedores')

@login_required
def buscarProveedor(request):
        
    if request.GET["nombre"]:
        nombre = request.GET['nombre']
        proveedor = Proveedor.objects.filter(nombre__icontains=nombre)
        
        return render(request, "AppCoder/proveedor.html",{"proveedor":proveedor})

    else:
        respuesta = "No enviaste nada"
    return render(request,"AppCoder/inicio.html",{"respuesta":respuesta})

################################################################     Repuestos  ################################
def registrarRepuesto(request):
    codigo = request.POST['txtCodigo']
    numero_de_parte = request.POST['txtNumero_de_parte']
    descripcion = request.POST['txtDescripcion']
    precio_de_costo = request.POST['txtPrecio_de_costo']         
    stock = request.POST['txtStock']
    proveedor = request.POST['txtProveedor']
    observaciones = request.POST['txtObservaciones']
    repuesto = Repuesto.objects.create(codigo =codigo, numero_de_parte=numero_de_parte, descripcion=descripcion, precio_de_costo=precio_de_costo, stock=stock, proveedor = proveedor, observaciones=observaciones)
    messages.success(request, '¡Repuesto registrado!')
    return redirect('/AppCoder/gestionDeRepuestos')

def repuestos(request):
      repuesto = Repuesto.objects.all()
      return render(request, "AppCoder/gestionDeRepuestos.html", {"repuesto":repuesto})

def edicionRepuesto(request, codigo):
    repuesto = Repuesto.objects.get(codigo=codigo)
    return render(request, "AppCoder/edicionRepuesto.html", {"repuesto": repuesto})

def editarRepuesto(request):
    codigo = request.POST['txtCodigo']
    numero_de_parte = request.POST['txtNumero_de_parte']
    descripcion = request.POST['txtDescripcion']
    precio_de_costo = request.POST['txtPrecio_de_costo']         
    stock = request.POST['txtStock']
    proveedor = request.POST['txtProveedor']
    observaciones = request.POST['txtObservaciones']
    repuesto = Repuesto.objects.get(codigo=codigo)
    repuesto.numero_de_parte = numero_de_parte
    repuesto.descripcion = descripcion
    repuesto.precio_de_costo = precio_de_costo
    repuesto.stock = stock
    repuesto.proveedor = proveedor
    repuesto.observaciones = observaciones    
    repuesto.save()
    messages.success(request, '¡Repuesto actualizado!')
    return redirect('/AppCoder/gestionDeRepuestos')

def eliminarRepuesto(request, codigo):
    repuesto = Repuesto.objects.get(codigo=codigo)
    repuesto.delete()
    messages.success(request, '¡Repuesto eliminado!')
    return redirect('/AppCoder/gestionDeRepuestos')

@login_required
def buscarRepuesto(request):
        
    if request.GET["numero_de_parte"]:
        numero_de_parte = request.GET['numero_de_parte']
        repuesto = Repuesto.objects.filter(numero_de_parte__icontains=numero_de_parte)        
        return render(request, "AppCoder/repuestos.html",{"repuesto":repuesto})
    else:
        respuesta = "No enviaste nada"
    return render(request,"AppCoder/inicio.html",{"respuesta":respuesta})

def reparacion(request):

      reparacion =  Reparacion(nombre="Desarrollo web", camada="19881")
      reparacion.save()
      documentoDeTexto = f"--->Reparacion: {reparacion.nombre}   Camada: {reparacion.camada}"
      return HttpResponse(documentoDeTexto)

def acercade(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "AppCoder/acercade.html", {"url":avatares[0].imagen.url})

def reparaciones(request):

      if request.method == 'POST':

            miFormulario = ReparacionFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  reparacion = Reparacion (nombre=informacion['reparacion'], camada=informacion['camada']) 

                  reparacion.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= ReparacionFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/reparaciones.html", {"miFormulario":miFormulario})

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class ReparacionList(ListView):
    model = Reparacion
    template_name = "AppCoder/reparaciones_list.html"

class ReparacionDetalle(DetailView):
    model = Reparacion
    template_name = "AppCoder/reparacion_detalle.html"

class ReparacionCreacion(CreateView):
    model = Reparacion
    success_url = "/AppCoder/reparacion/list"
    fields = ['nombre', 'camada']

class ReparacionUpdate(UpdateView):
    model = Reparacion
    success_url = "/AppCoder/reparacion/list"
    fields = ['nombre', 'camada']

class ReparacionDelete(DeleteView):
    model = Reparacion
    success_url = "/AppCoder/reparacion/list"


# Vista de login
def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "AppCoder/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppCoder/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "AppCoder/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "AppCoder/login.html", {"form": form})

def register(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,"AppCoder/inicio.html",{"mensaje":"Usuario Creado :)"})
    else:
        form = UserRegisterForm()
        #form = UserCreationForm()
    return render(request,"AppCoder/registro.html",{"form":form})


@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request,"AppCoder/inicio.html", {"url":avatares[0].imagen.url})
    #return render(request, "AppCoder/inicio.html")

# Vista de editar el perfil
@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "AppCoder/inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "AppCoder/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})
