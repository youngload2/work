from django.views.generic import ListView, DetailView, CreateView

from django.shortcuts import render, redirect

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import viewsets

from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied

from .models import *
from .serializers import *
from .forms import *

from django.core.paginator import Paginator

# Create your views here.

def index(request):
    return render(
        request,
        'erp/index.html',
    )

class CoaList(ListView):
    model = Coa

    paginate_by = 20

    template_name = 'erp/coa_list.html'
    context_object_name = 'coa_list'

    def get_queryset(self):
        coa_list = Coa.objects.order_by('id') 
        return coa_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 10
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        return context
class CoaDetail(DetailView):
    model = Coa

def create_coa(request):
    if request.method == 'POST':
        form = CoaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/coa/')
    else:
        form = CoaForm()

    return render(request, 'erp/form_create.html', {'form': form})

def update_coa(request, pk):
    coa = get_object_or_404(Coa, pk=pk)

    if request.method == 'POST':
        form = CoaForm(request.POST, instance=coa)

        if form.is_valid():
            form.save()
            return redirect('/coa/', pk=coa.pk)
        else:
            return redirect('/coa/')
    else:
        form = CoaForm(instance=coa)

    return render(request, 'erp/form_update.html', {'form': form})

def delete_coa(request, pk):
    coa = get_object_or_404(Coa, pk=pk)
    if request.user.is_authenticated:
        coa.delete()
        return redirect('/coa/')
    else:
        raise PermissionDenied

class ProductList(ListView):
    model = Product

    paginate_by = 20

    template_name = 'erp/product_list.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        product_list = Product.objects.order_by('id') 
        return product_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 10
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        return context

class ProductDetail(DetailView):
    model = Product

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/product/')
    else:
        form = ProductForm()

    return render(request, 'erp/form_create.html', {'form': form})

def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect('/product/', pk=product.pk)
        else:
            return redirect('/product/')
    else:
        form = ProductForm(instance=product)

    return render(request, 'erp/form_update.html', {'form': form})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    # if request.user.is_authenticated:
    product.delete()
    return redirect('/product/')
    # else:
    #     raise PermissionDenied

class CoaViewSet(viewsets.ModelViewSet):
    queryset = Coa.objects.all()
    serializer_class = CoaSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
