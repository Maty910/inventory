from db_methods import *
from validations import (
  pedir_texto_no_vacio,
  pedir_entero,
  pedir_opcion,
  pedir_nombre_unico,
  pedir_numero_positivo,
)

def main():
  while True:
    # Imprimimos el menú de opciones
    mostrarMenu()
    # El usuario ingresa su opción
    opcion = getOpcion()

    match opcion:
      case "1":
        ingresarProd()
      case "2":
        mostrarProd()
      case "3":
        buscarProd()
      case "4":
        actualizarProd()
      case "5":
        eliminarProd()
      case "6":
        bajoStock()
      case "7":
        print("Opción 7 seleccionada: Saliendo del programa.")
        print("\n Gracias por utilizar el programa. ¡Nos vemos! \n Podés encontrar otros de mis trabajos en: https://github.com/Maty910 \n" )
        break
      case _:
        print("Opción no válida. Por favor, ingrese una opción válida.")

# -------------------------------------------------

def mostrarMenu():
  print(""" \
  Menu de opciones: \n  \
  1. Ingresar producto \n  \
  2. Mostrar productos \n  \
  3. Buscar producto \n  \
  4. Modificar producto \n  \
  5. Eliminar producto \n  \
  6. Bajo Stock \n  \
  7. Salir"
  """)

def ingresarProd():
  print("Opción 1 seleccionada: Ingresar producto")
  lista_nombre = [p[1] for p in bd_leer_prod()]
  
  nombre = pedir_nombre_unico("Ingrese el nombre del producto: ", lista_nombre)
  descripcion = pedir_texto_no_vacio("Ingrese la descripción del producto: ")
  cantidad = pedir_entero("Ingrese la cantidad del producto: ", minimo=0)
  precio = pedir_numero_positivo("Ingrese el precio del producto: $")
  categoria = pedir_texto_no_vacio("Ingrese la categoría del producto: ")

  status = bd_insert_prod(nombre, descripcion, cantidad, precio, categoria)

  if status:
      print("Producto insertado correctamente en base de datos.")
  else: 
      print("Error al insertar el producto en base de datos.")

def mostrarProd():
  lista_productos = bd_leer_prod()

  print("Opción 2 seleccionada: Mostrar productos")
  if not lista_productos:
    print("No hay productos ingresados.")
    return
  
  print("Productos ingresados:")
  for producto in lista_productos:
    id_prod, nombre_prod, descripcion_prod, cantidad_prod, precio_prod, categoria_prod = producto

    print(f"\nID: {id_prod}\nNombre: {nombre_prod}\nDescripción: {descripcion_prod}\nCantidad: {cantidad_prod}\nPrecio: ${precio_prod}\nCategoría: {categoria_prod}\n")

def buscarProd():
  nombre = pedir_texto_no_vacio("Ingrese el nombre dle producto que desea buscar: ")

  lista_productos = bd_leer_prod_nombre(nombre)

  if not lista_productos:
    print("No hay productos ingresados para buscar. Por favor, primeo ingrese un producto.")
  else: 
    for producto in lista_productos:
      id_prod, nombre_prod, descripcion_prod, cantidad_prod, precio_prod, categoria_prod = producto
    print(f"\nID: {id_prod}\nNombre: {nombre_prod}\nDescripción: {descripcion_prod}\nCantidad: {cantidad_prod}\nPrecio: ${precio_prod}\nCategoría: {categoria_prod}\n")


def actualizarProd():
    id = pedir_entero("Ingrese el ID del producto que desea actualizar: ")
    producto_actual = bd_leer_prod_id(id)

    if not producto_actual:
        print("No se encontró un producto con ese ID.")
        return

    id_prod, nombre_actual, descripcion_actual, cantidad_actual, precio_actual, categoria_actual = producto_actual

    print("Dejá vacío para mantener el valor actual.")

    nombre_nuevo = input(f"Nombre [{nombre_actual}]: ").strip() or nombre_actual
    descripcion_nueva = input(f"Descripción [{descripcion_actual}]: ").strip() or descripcion_actual

    cantidad_nueva = input(f"Cantidad [{cantidad_actual}]: ").strip()
    if cantidad_nueva == "":
        cantidad_nueva = cantidad_actual
    else:
        try:
            cantidad_nueva = int(cantidad_nueva)
            if cantidad_nueva < 0:
                print("La cantidad debe ser un número entero positivo.")
                return
        except ValueError:
            print("Cantidad inválida. Debe ser un número entero.")
            return

    precio_nuevo = input(f"Precio [{precio_actual}]: ").strip()
    if precio_nuevo == "":
        precio_nuevo = precio_actual
    else:
        try:
            precio_nuevo = float(precio_nuevo)
            if precio_nuevo < 0:
                print("El precio debe ser positivo.")
                return
        except ValueError:
            print("Precio inválido. Debe ser un número.")
            return

    categoria_nueva = input(f"Categoría [{categoria_actual}]: ").strip() or categoria_actual

    status = bd_actualizar_prod(id, nombre_nuevo, descripcion_nueva, cantidad_nueva, precio_nuevo, categoria_nueva)

    if status:
        print("Registro actualizado correctamente.")
    else:
        print("Error al actualizar el registro.")

def eliminarProd():
  id = pedir_entero("Ingrese le ID del producto que desea eliminar: ")

  status = bd_eliminar_prod(id)

  if status: 
    print("Registro eliminado correctamente.")
  else:
    print("Error al eliminar el resgistro.")

def bajoStock():
  # El usuario ingresa el umbral de mínimo stock
    stock = pedir_entero("Ingrese el mínimo stock: ", minimo=0)

    lista_bajo_stock = bd_leer_bajo_stock(stock)

    if not lista_bajo_stock:
      print("No hay productos con bajo stock.")
    else:
      print("Productos con bajo stock: ")
      for producto in lista_bajo_stock:
        print(producto)

# ---------------------------------------------------------

def getOpcion():
  opcion = input("Ingrese su opción:").strip()
  return opcion

# ---------------------------------------------------------

if __name__  == "__main__":
  db_crear_tabla_productos()
  main()