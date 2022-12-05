from django.urls import path

from TiendaCoco import views

urlpatterns = [
    path("", views.tienda_index, name="tienda-index"),
    path("new", views.nuevo_producto, name="tienda-form"),
    path("search", views.search_product, name="tienda-search"),
]