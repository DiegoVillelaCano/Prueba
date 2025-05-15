from flask import Flask
from flask import render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

# Inicializo mi aplicación Flask
app = Flask(__name__)

# Configuro la conexión a la base de datos PostgreSQL que tengo en Supabase
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres.ytitdntuyxxxnrrohebe:DiegoVillelaCanoProject@aws-0-us-east-2.pooler.supabase.com:5432/postgres"

# Desactivo el seguimiento de modificaciones de SQLAlchemy porque no lo necesito y consume más recursos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializo SQLAlchemy con la app
db = SQLAlchemy(app)

# Defino el modelo 'Producto' que representa la tabla 'Prueba' en la base de datos
class Producto(db.Model):
    __tablename__ = 'Prueba'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)
    precio = db.Column(db.Numeric, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)

# Ruta principal que muestra todos los productos en la tabla
@app.route('/')
def index():
    productos = Producto.query.all()  # Obtengo todos los productos
    return render_template("productos/index.html", productos=productos)  # Renderizo el HTML y paso los productos

# Ruta para eliminar un producto por su ID
@app.route('/eliminar/<int:id>')
def eliminar(id):
    producto = Producto.query.get_or_404(id)  # Si no encuentra el producto, lanza error 404
    db.session.delete(producto)               # Lo elimino de la base de datos
    db.session.commit()                       # Confirmo los cambios
    return redirect(url_for('index'))         # Redirijo a la página principal

# Ruta para guardar un producto (tanto nuevo como editado)
@app.route('/guardar', methods=['POST'])
def guardar():
    id = request.form['id']
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    precio = request.form['precio']
    cantidad = request.form['cantidad']

    errores = []
 # Validación de campos obligatorios
    if not nombre or not descripcion or not precio or not cantidad:
        errores.append("Todos los campos deben estar completos.")
    if precio and float(precio) <= 0:
        errores.append("El precio debe ser mayor a 0.")
    if cantidad and int(cantidad) <= 0:
        errores.append("La cantidad debe ser mayor a 0.")

    if errores:
        productos = Producto.query.all()
        return render_template("productos/index.html", productos=productos, errores=errores,
                               modal_abierto=True, producto_form={"id": id, "nombre": nombre, "descripcion": descripcion,
                                                                  "precio": precio, "cantidad": cantidad})

    if id:# Edición
        producto = Producto.query.get(id)
        producto.nombre = nombre
        producto.descripcion = descripcion
        producto.precio = precio
        producto.cantidad = cantidad
    else: # Nuevo producto
        producto = Producto(nombre=nombre, descripcion=descripcion, precio=precio, cantidad=cantidad)
        db.session.add(producto)

    db.session.commit()
    return redirect(url_for('index'))
    
@app.route('/buscar', methods=['GET'])# Buscar producto
def buscar():
    id = request.args.get('buscar_id', '').strip()

    if not id.isdigit():
        return "Error: El ID debe ser un número entero.", 400
    producto = Producto.query.get(int(id))
    if not producto:
        return render_template("productos/index.html", productos=[], mensaje=f"No se encontró el producto con ID {id}")
    return render_template("productos/index.html", productos=[producto], mensaje=f"Mostrando producto con ID {id}")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
