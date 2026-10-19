# Votaciones Festival

<p align="center">
  <img src="static/img/logo.png" alt="Logo Votaciones Festival" width="220" />
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img alt="Django" src="https://img.shields.io/badge/Django-4.2-092E20?style=for-the-badge&logo=django&logoColor=white" />
  <img alt="MySQL" src="https://img.shields.io/badge/MySQL-8.0-4479A1?style=for-the-badge&logo=mysql&logoColor=white" />
  <img alt="Bootstrap" src="https://img.shields.io/badge/Bootstrap-5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white" />
</p>

Sistema web para gestionar votaciones de un festival, desarrollado con Django. Permite organizar ediciones, categorías, votaciones y opciones para que los usuarios puedan explorar y participar en la elección de sus favoritos.

## ✨ Descripción

Este proyecto está pensado como una plataforma de votación para eventos culturales o musicales. La aplicación incluye:

- listado de categorías disponibles
- detalle de cada votación
- registro e inicio de sesión de usuarios
- cierre de sesión
- estructura modular para manejar ediciones, votaciones y opciones
- interfaz visual con plantillas y estilos propios del proyecto

## 🏗️ Tecnologías

- Python 3.10+
- Django 4.2
- MySQL
- HTML5 / CSS3
- Bootstrap
- SQLite para entorno local de desarrollo (incluido por defecto en la estructura del proyecto)

## 📁 Estructura del proyecto

```text
votaciones-festival/
├── .env.example
├── .gitignore
├── README.md
├── manage.py
├── requirements.txt
├── db.sqlite3
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── votaciones/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── fixtures/
│   ├── forms.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates/
│   ├── layouts/
│   ├── public/
│   ├── reference/
│   ├── registration/
│   └── ...
├── static/
│   ├── css/
│   └── img/
├── referencia/
│   └── prototipo_original/
└── .venv/
```

## ✅ Requisitos

Antes de iniciar, asegúrate de tener instalado:

- Python 3.10 o superior
- pip
- MySQL Server
- virtualenv (opcional, recomendado)

## 🚀 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/JJMR07/votaciones-festival.git
cd votaciones-festival
```

2. Crea y activa un entorno virtual:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Configura las variables de entorno:

Copia el archivo de ejemplo:

```bash
copy .env.example .env
```

O en Linux/macOS:

```bash
cp .env.example .env
```

Edita el archivo `.env` con tus credenciales locales:

```env
DJANGO_SECRET_KEY=tu_clave_secreta
DJANGO_DEBUG=True

DB_NAME=festival_votaciones
DB_USER=root
DB_PASSWORD=tu_password
DB_HOST=127.0.0.1
DB_PORT=3306
```

5. Crea la base de datos en MySQL si aún no existe:

```sql
CREATE DATABASE festival_votaciones;
```

6. Ejecuta las migraciones:

```bash
python manage.py migrate
```

7. (Opcional) Crea un superusuario para acceder al panel de administración:

```bash
python manage.py createsuperuser
```

## ▶️ Ejecución

Inicia el proyecto con:

```bash
python manage.py runserver
```

Luego abre tu navegador en:

```text
http://127.0.0.1:8000/
```

## 🧭 Rutas principales

- `/` — página de inicio
- `/categorias/` — listado de categorías
- `/categorias/<id>/votaciones/` — votaciones por categoría
- `/votaciones/<id>/` — detalle de una votación
- `/registro/` — registro de usuarios
- `/iniciar-sesion/` — inicio de sesión
- `/cerrar-sesion/` — cierre de sesión
- `/admin/` — panel administrativo de Django

## 🗂️ Modelo de datos

La aplicación principal define este conjunto de modelos:

- `Edicion`
- `Categoria`
- `Votacion`
- `Opcion`

Estos modelos permiten estructurar una votación por edición y categoría, con múltiples opciones por cada concurso o categoría.

## 📌 Notas importantes

- El archivo `.env` no debe subirse al repositorio.
- Para que funcione la conexión a MySQL, es necesario tener el cliente de MySQL configurado en el entorno local.
- El proyecto está configurado para Colombia con la zona horaria `America/Bogota`.

## 🏷️ Licencia

Este repositorio no especifica una licencia en el archivo actual, por lo que se recomienda revisar la política de uso antes de compartirlo o desplegarlo en un entorno de producción.

## 👤 Autor

Proyecto desarrollado para una plataforma de votaciones del festival, gestionado en este repositorio de GitHub.

<p align="center">
  <img src="static/img/music.png" alt="Decoración festival" width="320" />
</p>
