# App de extracción de contenido de archivos PDF

## Descripción

Esta aplicación permite a los usuarios crear una cuenta para obtener la funcionalidad de extraer el contenido de un documento en formato PDF, convertirlo en audio, y guardar tanto los documentos como los audios generados en su cuenta.

## Integrantes

- Edy Jiménez
- Patricio Paredes
- Jonathan Sefla

## Instalación y Ejecución

Sigue estos pasos para instalar y ejecutar la aplicación:

1. **Clonar el repositorio desde GitHub**: Este es el primer paso para obtener una copia local del proyecto. Puedes hacerlo utilizando el comando `git clone <URL del repositorio>` en tu terminal.

2. **Instalar las dependencias**: El proyecto requiere ciertas bibliotecas de Python para funcionar correctamente. Estas dependencias están listadas en el archivo `requirements.txt`. Puedes instalarlas usando el comando `pip install -r requirements.txt`.

3. **Configurar la base de datos PostgreSQL**: Django viene con SQLite por defecto, pero en este caso, estamos usando PostgreSQL. Necesitarás realizar algunos pasos adicionales para configurarlo:

   3.1. **Crear una nueva base de datos en PostgreSQL**: Puedes hacer esto utilizando las herramientas de línea de comandos de PostgreSQL o una interfaz gráfica como pgAdmin.

   3.2. **Modificar la configuración de la base de datos en `settings.py`**: En este archivo, debes actualizar la configuración de la base de datos con los detalles de tu base de datos PostgreSQL recién creada.

4. **Realizar las migraciones**: Antes de poder ejecutar el servidor, necesitas crear las tablas en tu base de datos. Django facilita esto con su sistema de migraciones. Puedes hacer esto con los comandos `python manage.py makemigrations` y `python manage.py migrate`.

5. **Ejecutar el servidor**: Ahora estás listo para ejecutar el servidor. Puedes hacer esto con el comando `python manage.py runserver`. Ahora deberías poder acceder a la aplicación en tu navegador web en `http://localhost:8000`.


