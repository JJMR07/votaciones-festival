from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST

from .forms import RegistroUsuarioForm
from .models import Categoria, Edicion, Votacion


def inicio(request):
    ediciones = Edicion.objects.prefetch_related(
        "categorias__votaciones__opciones"
    ).all()
    categorias_destacadas = Categoria.objects.select_related("edicion").all()[:4]
    return render(
        request,
        "public/inicio.html",
        {"ediciones": ediciones, "categorias_destacadas": categorias_destacadas},
    )


def categorias(request):
    categorias_registradas = Categoria.objects.select_related("edicion").prefetch_related(
        "votaciones"
    )
    return render(
        request,
        "public/categorias.html",
        {"categorias": categorias_registradas},
    )


def votaciones_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    votaciones = categoria.votaciones.prefetch_related("opciones").all()
    return render(
        request,
        "public/votaciones.html",
        {"categoria": categoria, "votaciones": votaciones},
    )


def detalle_votacion(request, votacion_id):
    votacion = get_object_or_404(
        Votacion.objects.select_related("categoria__edicion").prefetch_related("opciones"),
        pk=votacion_id,
    )
    return render(request, "public/detalles-votacion.html", {"votacion": votacion})


def registro(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, "Tu cuenta fue creada correctamente.")
            return redirect("votaciones:inicio")
    else:
        form = RegistroUsuarioForm()

    return render(request, "registration/registro.html", {"form": form})


class InicioSesionView(LoginView):
    template_name = "registration/login.html"
    next_page = reverse_lazy("votaciones:inicio")


iniciar_sesion = InicioSesionView.as_view()


@require_POST
def cerrar_sesion(request):
    logout(request)
    messages.info(request, "Has cerrado sesión.")
    return redirect("votaciones:iniciar_sesion")
