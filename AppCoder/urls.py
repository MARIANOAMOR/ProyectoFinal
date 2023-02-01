from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView
#from .views import buscarCliente


urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('acercade', views.acercade, name="Acercade"), #esta era nuestra primer view
    path('reparaciones', views.reparaciones, name="Reparaciones"),
    ###### CLIENTES ##############
    path('gestionDeClientes', views.clientes, name="Clientes"),
    path('registrarCliente/', views.registrarCliente), #lo uso cuando apreto el boton de guardar cliente nuevo
    path('gestionDeProveedores', views.proveedores, name="Proveedores"),
    path('repuestos', views.repuestos, name="Repuestos"),
    path('buscarCliente/',views.buscarCliente),

    path('leerClientes', views.leerClientes, name = "LeerClientes"),
    
    path('eliminarCliente/<codigo>', views.eliminarCliente, name = "eliminarCliente"),
    path('edicionCliente/<codigo>', views.edicionCliente, name = "editarCliente"),
    path('editarCliente/', views.editarCliente),

    path('reparacion/list', views.ReparacionList.as_view(), name='List'),
    ######## PROVEEDORES ###########
    path('buscarProveedor/',views.buscarProveedor),
    path('registrarProveedor/', views.registrarProveedor), #lo uso cuando apreto el boton de guardar un proveedor nuevo
    path('gestionDeProveedores', views.proveedores, name="Proveedores"),
    path('eliminarProveedor/<codigo>', views.eliminarProveedor, name = "eliminarProveedor"),
    path('edicionProveedor/<codigo>', views.edicionProveedor, name = "editarProveedor"),
    path('editarProveedor/', views.editarProveedor),
    ######## REPUESTOS ###########
    path('buscarRepuesto/',views.buscarRepuesto),
    path('registrarRepuesto/', views.registrarRepuesto), #lo uso cuando apreto el boton de guardar un repuesto nuevo
    path('gestionDeRepuestos', views.repuestos, name="Repuestos"),
    path('eliminarRepuesto/<codigo>', views.eliminarRepuesto, name = "eliminarRepuesto"),
    path('edicionRepuesto/<codigo>', views.edicionRepuesto, name = "editarRepuesto"),
    path('editarRepuesto/', views.editarRepuesto),
    # login y registro
    path('login', views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name='EditarPerfil')


    

]

