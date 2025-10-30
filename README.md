# Gestión de Voluntarios y Eventos

## Descripción
Aplicación web desarrollada en Django para gestionar voluntarios y eventos de una ONG.
Permite:
- Crear, editar y eliminar voluntarios y eventos.
- Asociar voluntarios a eventos (Many-to-Many).
- Visualizar listas y detalles de registros.
- Formularios con ayuda (help_text) para guiar al usuario.
- Seguridad mediante {% csrf_token %} en todos los formularios.

Este proyecto fue desarrollado como ejercicio grupal para optimizar el trabajo en equipo.

## Tecnologías
- Backend: Python, Django
- Base de datos: MySQL
- Frontend: HTML, Bootstrap 5

## Instalación y Ejecución

- Clonar repositorio:
git clone https://github.com/Edrojuz/Gestion_ONG_django.git

- Crear y activar entorno virtual:
python -m venv entorno_django
# Windows
`entorno_django\Scripts\activate`

- Instalar dependencias:
`pip install -r requirements.txt`

- Migrar la base de datos:
`python manage.py makemigrations`
`python manage.py migrate`

- Ejecutar servidor:

`python manage.py runserver`

- Página principal: http://127.0.0.1:8000/

## Modelos Principales
class Voluntario(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha = models.DateField()
    voluntarios = models.ManyToManyField(Voluntario, related_name="eventos")

    def __str__(self):
        return self.titulo


Voluntario: Persona registrada para ayudar.

Evento: Actividad de la ONG con voluntarios asociados.

## Funcionalidades
- CRUD completo para voluntarios y eventos.
- Detalles individuales de registros y de eventos.
- Asociaciones Many-to-Many entre voluntarios y eventos.
- Validaciones y help_text en formularios.
- Seguridad CSRF.

## Uso
- Crear voluntario: /App_ONG/crear_voluntario/
- Crear evento: /App_ONG/crear_evento/
- Listar registros: /App_ONG/lista/
- Actualizar o eliminar desde los botones de la lista.

  ## 🧩 Mejoras Recientes

## 🔹 Validación de Fechas en Eventos
Se implementó una validación en el formulario `EventoForm` que **impide crear o actualizar eventos con fechas anteriores a la actual**.  
Esto evita errores de planificación y mantiene la coherencia de los registros.

## Integrantes Grupo 3:
- Patricia Vidal
- Jasmin Salvador
- Tatu Vergara
- Eduardo Rojas
