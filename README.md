Manual de Usuario.

Aplicación de Inventario de Productos.

 Esta aplicacion web permite gestionar un inventario de productos con una base de datos en la nube
 utilizando Supabase. Fue desarrollada con Flask y SQLAlchemy.
 
 Requisitos previos:
 - Tener Python instalado.
 - Instalar las siguientes dependencias en Visual Studio Code o en el entorno deseado:

   pip install flask

   pip install flask-sqlalchemy

   pip install jinja2

   pip install flask sqlalchemy psycopg2-binary

    pip list   # Para verificar la instalacion
   
 Ejecucion local (Visual Studio Code o terminal):
 1. Navegar a la carpeta del proyecto.
 2. Ejecutar: python app.py
 3. Abrir un navegador en: http://127.0.0.1:5000/

 Base de Datos:
 No es necesario instalar nada adicional ya que se usa Supabase como backend remoto. La
 conexion ya esta configurada en app.py.
 

 Uso de la aplicacion:
 - Pantalla principal muestra la lista de productos registrados.
 - Puedes agregar nuevos productos usando el boton "Ingresar nuevo producto".
 - Puedes editar o eliminar productos existentes con los botones correspondientes.
 
 Formulario:
 - Nombre: Nombre del producto.
 - Descripcion: Breve detalle del producto.
 - Precio: Costo del producto (en numeros decimales).
 - Cantidad: Numero de unidades disponibles.

Botones:
- Confirmar: Guarda o actualiza el producto.
-  Cancelar: Cierra el formulario sin guardar.
  
 La aplicacion usa Bootstrap para el diseño visual y Jinja2 como motor de plantillas.
 
 Desarrollador: Diego Villela Cano
