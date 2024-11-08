# inventario/views.py
from django import forms
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Computadora
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import get_object_or_404, render

def imprimir_computadora(request, pk):
    computadora = get_object_or_404(Computadora, pk=pk)

    return render(request, 'imprimir_computadora.html', {'computadora': computadora})
class ListaComputadoras(ListView):
    model = Computadora
    template_name = 'lista_computadoras.html'
    context_object_name = 'computadoras'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(responsable__icontains=query) |
                Q(marca__icontains=query) |
                Q(modelo__icontains=query) |
                Q(numero_serie__icontains=query)
            )
        return queryset

class CrearComputadora(CreateView):
    model = Computadora
    fields = ['responsable','marca', 'modelo', 'numero_serie', 'fecha_compra','licencia', 'estado']
    template_name = 'formulario_computadora.html'
    success_url = reverse_lazy('lista_computadoras')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['fecha_compra'].widget = forms.DateInput(attrs={'type': 'date'})
        return form

class EditarComputadora(UpdateView):
    model = Computadora
    fields = ['responsable','marca', 'modelo', 'numero_serie', 'fecha_compra','licencia', 'estado']
    template_name = 'formulario_computadora.html'
    success_url = reverse_lazy('lista_computadoras')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['fecha_compra'].widget = forms.DateInput(attrs={'type': 'date'})
        return form

class EliminarComputadora(DeleteView):
    model = Computadora
    template_name = 'confirmar_eliminar.html'
    success_url = reverse_lazy('lista_computadoras')
