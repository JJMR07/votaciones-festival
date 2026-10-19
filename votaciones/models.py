from django.db import models


class Edicion(models.Model):
    nombre = models.CharField(max_length=150)

    class Meta:
        verbose_name = "edición"
        verbose_name_plural = "ediciones"

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    edicion = models.ForeignKey(
        Edicion,
        on_delete=models.CASCADE,
        related_name="categorias",
    )
    nombre = models.CharField(max_length=150)

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"

    def __str__(self):
        return self.nombre


class Votacion(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name="votaciones",
    )
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre


class Opcion(models.Model):
    votacion = models.ForeignKey(
        Votacion,
        on_delete=models.CASCADE,
        related_name="opciones",
    )
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre
