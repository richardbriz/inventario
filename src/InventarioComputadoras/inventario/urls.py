# inventario/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListaComputadoras.as_view(), name='lista_computadoras'),
    path('computadora/nueva/', views.CrearComputadora.as_view(), name='crear_computadora'),
    path('computadora/<int:pk>/editar/', views.EditarComputadora.as_view(), name='editar_computadora'),
    path('computadora/<int:pk>/eliminar/', views.EliminarComputadora.as_view(), name='eliminar_computadora'),
    path('computadora/<int:pk>/imprimir/', views.imprimir_computadora, name='imprimir_computadora'),  # Nueva ruta de impresión
]
