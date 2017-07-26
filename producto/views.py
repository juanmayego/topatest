from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from producto.models import Producto

class ProductoList(ListView):
    model = Producto

class ProductoCreate(CreateView):
    model = Producto
    success_url = reverse_lazy('producto_list')
    fields = ['nombre', 'descripcion']

class ProductoUpdate(UpdateView):
    model = Producto
    success_url = reverse_lazy('producto_list')
    fields = ['nombre', 'descripcion']

class ProductoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy('producto_list')