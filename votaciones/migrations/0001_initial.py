# Generated manually to match Django 6.1.2.

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Edicion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=150)),
            ],
            options={
                "verbose_name": "edición",
                "verbose_name_plural": "ediciones",
            },
        ),
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=150)),
                (
                    "edicion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="categorias",
                        to="votaciones.edicion",
                    ),
                ),
            ],
            options={
                "verbose_name": "categoría",
                "verbose_name_plural": "categorías",
            },
        ),
        migrations.CreateModel(
            name="Votacion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=150)),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="votaciones",
                        to="votaciones.categoria",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Opcion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=150)),
                (
                    "votacion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="opciones",
                        to="votaciones.votacion",
                    ),
                ),
            ],
        ),
    ]
