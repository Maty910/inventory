# import módulo de sqlite3
import sqlite3 

# import módulo de os
import os

BASE_DIR = os.path.dirname(
  os.path.abspath(__file__)
)

# Ruta a la base de datos
db_route = os.path.join(BASE_DIR, "inventario.db")

# Función para crear la tabla productos de la base de datos
def db_crear_tabla_productos():
  try:
    conexion = sqlite3.connect(db_route)
    cursor = conexion.cursor()
    sql = """CREATE TABLE IF NOT EXISTS "productos" (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre TEXT NOT NULL,
  descripcion TEXT,
  cantidad INTEGER NOT NULL DEFAULT 0,
  precio REAL NOT NULL,
  categoria TEXT NOT NULL
  )"""
    cursor.execute(sql)
    conexion.commit()
  except Exception as error:
    print(f"Error al crear la tabla: {error}")
  finally:
    conexion.close()

# Función para insertar datos en la tabla productos de la base de datos
def bd_insert_prod(nombre, descripcion, cantidad, precio, categoria):
  status = False
  try:
    conexion = sqlite3.connect(db_route)
    cursor = conexion.cursor()
    sql = """INSERT INTO productos
  ("nombre", "descripcion", "cantidad", "precio", "categoria")
  VALUES
  (?, ?, ?, ? , ?)"""
    cursor.execute(sql, (nombre, descripcion, cantidad, precio, categoria))
    if cursor.rowcount == 1:
      status = True
    conexion.commit()
  except Exception as error:
    print(f"Error al insertar producto en la tabla: {error}")
  finally:
    conexion.close()
    return status

# Función para leer los datos de la tabla productos
def bd_leer_prod():
  lista_productos = []
  try:
    conexion = sqlite3.connect(db_route)
    cursor = conexion.cursor()
    sql = """SELECT * FROM productos"""
    cursor.execute(sql)
    lista_productos = cursor.fetchall()
  except Exception as error:
    print(f"Error al leer los productos de la tabla: {error}")
  finally:
    conexion.close()
  return lista_productos

# Función para leer productos por nombre
def bd_leer_prod_nombre(nombre):
  lista_productos = []
  try:
    conexion = sqlite3.connect(db_route)
    cursor = conexion.cursor()
    sql = """SELECT * FROM productos WHERE nombre LIKE ?"""
    cursor.execute(sql, ("%" + nombre + "%",))
    lista_productos = cursor.fetchall()
  except Exception as error: 
    print(
      f"Error encontrado al crear la tabla: {error}"
    )
  finally:
    conexion.close()
  return lista_productos

# Función para buscar un producto por su id de la tabla de la base de datos.
def bd_leer_prod_id(id):
  producto = None
  try:
    conexion = sqlite3.connect(db_route)
    cursor = conexion.cursor()
    sql = """SELECT * FROM productos WHERE id = ?"""
    cursor.execute(sql, (id,))
    producto = cursor.fetchone()
  except Exception as error:
    print(f"Error enctrado al leer el registro según su id: {error}")
  finally:
    conexion.close()
    return producto
  
# Función para modificar el precio de un producto a partir de su id
def bd_actualizar_precio(id, precio):
  status = False
  try: 
    conexion = sqlite3.connect(db_route)
    cursor = conexion.cursor()
    sql = """UPDATE productos SET precio = ? WHERE id = ?"""
    cursor.execute(sql, (precio, id))
    conexion.commit()
    if cursor.rowcount > 0:
      status = True
  except Exception as error: 
    print(f"Error encontrado al modificar el precio según su id: {error}")
  finally:
    conexion.close()
  return status

# Función para modificar todos los campos de un producto de la base de datos.
def bd_actualizar_prod(id, nombre, descripcion, cantidad, precio, categoria):
    status = False
    try:
        conexion = sqlite3.connect(db_route)
        cursor = conexion.cursor()
        sql = """UPDATE productos 
                 SET nombre = :nombre, descripcion = :descripcion, cantidad = :cantidad, precio = :precio, categoria = :categoria
                 WHERE id = :id"""
        cursor.execute(sql, {
            "id": id,
            "nombre": nombre,
            "descripcion": descripcion,
            "cantidad": cantidad,
            "precio": precio,
            "categoria": categoria,
        })
        conexion.commit()
        if cursor.rowcount > 0:
            status = True
    except Exception as error:
        print(f"Error al modificar los registros del producto: {error}")
    finally:
        conexion.close()
    return status

# Función para eliminar un registro de la tabla de la base de datos según su id.
def bd_eliminar_prod(id):
  status = False
  try: 
    conexion = sqlite3.connect(db_route)
    cursor = conexion.cursor()
    sql = """DELETE FROM productos WHERE id = ?"""
    cursor.execute(sql, (id,))
    conexion.commit()
    if cursor.rowcount > 0:
      status = True
  except Exception as error:
    print(f"Error al eliminar el registro: {error}")
  finally:
    conexion.close()
    return status   

# Función para leer el sock 
def bd_leer_bajo_stock(stock):
  conexion = sqlite3.connect(db_route)
  cursor = conexion.cursor()
  sql = """SELECT * FROM productos WHERE cantidad < ?"""
  cursor.execute(sql, (stock,))
  lista_productos = cursor.fetchall()
  conexion.close()
  return lista_productos

# Función para insertar datos en la tabla productos.
def bd_inicializar_tabla_prod(lista_productos):
  status = False 
  try:
    conexion = sqlite3.connect(db_route)
    cursor = conexion.cursor()
    sql = """INSERT INTO productos
    ("nombre", "descripcion", "cantidad", "precio", "categoria")
    VALUES
    (?, ?, ?, ?, ?)"""
    cursor.executemany(sql, lista_productos)
    if cursor.rowcount == len(lista_productos):
      status = True
    conexion.commit()
  except Exception as error:
    print(f"Error encontrado en inicializar la tabla: {error}")
  finally:
    conexion.close()
    return status    