# Django Bootstrap Starter Kit


Use this repository as Django project template::

    django-admin startproject --template https://github.com/ciur/django-bootstrap-project-template/archive/master.zip <projectname>

Watch [Django Lessons screencast](https://django-lessons.com/lesson/lesson-25-new-django-project-template-template-argument) about --template argument of django-admin command.



## Installation

1. Clonar repositorio: `git clone https://github.com/your/repository.git`
2. Instalar dependencias: `pip install -r requirements.txt`

## Usage
1. Crear un entorno virtual: `python3 -m venv vuelos_venv`
2. Activar entorno virtual: `source venv/bin/activate`
3. Correr el servidor de Django: `python manage.py runserver`


# Docker Desktop

1. Instalar Docker Desktop: `https://www.docker.com/products/docker-desktop/`
2. Entramos a la carpeta:  `cd VUELOS/`
3. Creamos la imagen: `docker-compose build`
4. Corremos la imagen creada: `docker-compose up`