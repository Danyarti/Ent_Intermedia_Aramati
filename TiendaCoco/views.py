from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import Tienda
from .forms import productoform

# Create your views here.
def tienda_index (request: HttpRequest) -> HttpResponse:
    if request.GET.get('producto', False):
        producto= request.GET.get('producto')
        tienda=Tienda.objects.filter(producto__icontains=producto)
    else:
        tienda= Tienda.objects.all()
    return render (request, "tienda-index.html", {"tienda": tienda})

def nuevo_producto (request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        newproductform=productoform(request.POST)
        if not newproductform.is_valid():
            return render(
                request, "nuevo_form.html",
                {"error":"DEBE COMPLETAR TODOS LOS CAMPOS",
                "form":newproductform},
            )
        new_product = Tienda(**newproductform.cleaned_data)
        new_product.save()

        return redirect('tienda-index')
        
    else:
        return render(request, "nuevo_form.html", {"form": productoform()})

def search_product (request: HttpRequest) -> HttpResponse:
    return render (request, "search_producto.html", {"tienda": Tienda})
