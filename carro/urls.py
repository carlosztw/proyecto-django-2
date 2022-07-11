from django.urls import path

from .import views
app_name="carro"

urlpatterns = [
    path("agregar/<int:id_producto>/", views.agregar_producto_carro, name="agregar"),
    path("eliminar/<int:id_producto>/", views.eliminar_producto_carro, name="eliminar"),
    path("restar/<int:id_producto>/", views.restar_producto_carro, name="restar"),
    path("limpiar/", views.limpiar_carro, name="limpiar"),
]