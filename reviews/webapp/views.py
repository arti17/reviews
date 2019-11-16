from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from webapp.forms import ProductForm
from webapp.models import Product


class IndexView(ListView):
    template_name = 'product/index.html'
    context_object_name = 'products'
    model = Product
    ordering = ['name']


class ProductCreateView(CreateView):
    template_name = 'product/create_product.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('webapp:index')


class ProjectDetailView(DetailView):
    template_name = 'product/product_detail.html'
    model = Product
    context_key = 'product'


class ProductUpdateView(UpdateView):
    model = Product
    class_form = ProductForm
    template_name = 'product/update_product.html'
    context_object_name = 'product'
    fields = ['name', 'category', 'description', 'photo']

    def get_success_url(self):
        return reverse('webapp:index')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('webapp:index')
