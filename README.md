#  Aplicación de Inventario (Python + SQLite)

Esta es una aplicación de consola desarrollada en Python que permite gestionar un inventario de productos utilizando una base de datos SQLite.

## ✅ Funcionalidades

- Registrar productos con los siguientes campos:
  - Nombre
  - Descripción
  - Cantidad (entero positivo)
  - Precio (solo enteros, sin decimales)
  - Categoría

- Listar todos los productos del inventario.
- Modificar datos de un producto existente.
- Eliminar productos.
- Buscar productos por nombre.
- Generar un reporte de productos con **bajo stock**.

## 🧱 Estructura del proyecto

```bash
inventario/
├── inventario.db         # Base de datos SQLite
├── main.py               # Archivo principal (menú y flujo de la app)
├── db_methods.py         # Funciones para interactuar con la base de datos
├── validations.py        # Funciones para validar entradas del usuario
└── README.md             # Este archivo
