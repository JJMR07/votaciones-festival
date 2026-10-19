from django.urls import path

from . import views

app_name = "votaciones"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("categorias/", views.categorias, name="categorias"),
    path(
        "categorias/<int:categoria_id>/votaciones/",
        views.votaciones_por_categoria,
        name="votaciones_por_categoria",
    ),
    path("votaciones/<int:votacion_id>/", views.detalle_votacion, name="detalle_votacion"),
    path("registro/", views.registro, name="registro"),
    path("iniciar-sesion/", views.iniciar_sesion, name="iniciar_sesion"),
    path("cerrar-sesion/", views.cerrar_sesion, name="cerrar_sesion"),
]
