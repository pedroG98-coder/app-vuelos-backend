#=============== Dockerfile Backend Django ===============

# Usamos una imagen base de Python3.8
FROM python:3.8

# Establecemos variables de entorno.
ENV APP_VUELOS=/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Establecemos el directorio de trabajo dentro del contenedor.
WORKDIR $APP_VUELOS

# Actualizamos pip e instalamos dependencias
RUN pip install --upgrade pip 
COPY ./requirements.txt $APP_VUELOS
RUN pip install -r requirements.txt

# Copiamos todo el contenido del directorio actual al directorio de trabajo en el contenedor.
COPY . $APP_VUELOS

# Exponemos el puerto 8000
EXPOSE 8000

# Ejecutamos makemigrations
RUN python manage.py makemigrations

# Ejecutamos Migraciones
RUN python manage.py migrate

# Recolectamos los archivos estáticos de la aplicación.
#RUN python manage.py collectstatic --noinput --clear

# Comando por defecto para ejecutar
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]