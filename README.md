# Restaurante App - Semana 12

## Descripción

Restaurante App es una aplicación desarrollada en Python utilizando Programación Orientada a Objetos (POO). El sistema permite administrar productos, usuarios y ventas, manteniendo el control del stock y la persistencia de la información mediante archivos JSON.

En esta versión (Semana 12) se optimizó el rendimiento del sistema mediante el uso de colecciones auxiliares, mejorando las búsquedas y consultas frecuentes sin modificar las funcionalidades implementadas en semanas anteriores.

---

## Funcionalidades

- Registro de productos.
- Búsqueda de productos.
- Modificación de productos.
- Eliminación de productos.
- Registro de usuarios.
- Búsqueda de usuarios.
- Registro de ventas.
- Consulta de ventas por usuario.
- Control automático del stock.
- Persistencia de datos en archivos JSON.

---

## Estructura del proyecto

```
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md
```

---

## Mejoras implementadas (Semana 12)

Se incorporaron estructuras auxiliares utilizando colecciones de Python para optimizar el rendimiento del sistema.

### Colecciones principales

Se conservaron las listas principales para almacenar y recorrer la información:

- Lista de productos.
- Lista de usuarios.
- Lista de ventas.

### Colecciones auxiliares

Se implementaron diccionarios para mejorar las búsquedas frecuentes:

- **productos_por_codigo**
  - Permite encontrar un producto utilizando su código sin recorrer toda la lista.

- **usuarios_por_id**
  - Permite localizar un usuario mediante su identificación de forma inmediata.

- **ventas_por_usuario**
  - Permite consultar todas las ventas realizadas por un usuario sin recorrer completamente la lista de ventas.

---

## Sincronización de los índices

Los índices auxiliares se actualizan automáticamente cuando:

- Se registra un nuevo producto.
- Se registra un nuevo usuario.
- Se registra una nueva venta.

Al iniciar la aplicación, los índices se reconstruyen automáticamente después de cargar la información almacenada en los archivos JSON.

---

## Colecciones utilizadas

- **list**
  - Productos
  - Usuarios
  - Ventas

- **dict**
  - productos_por_codigo
  - usuarios_por_id
  - ventas_por_usuario

No fue necesario utilizar **set**, ya que el sistema no requería validaciones adicionales de pertenencia o unicidad distintas a las resueltas mediante diccionarios.

---

## Persistencia de datos

Toda la información se almacena en formato JSON.

Archivos utilizados:

- productos.json
- usuarios.json
- ventas.json

Los datos permanecen almacenados aun después de cerrar la aplicación.

---

## Ejecución

1. Abrir el proyecto en Visual Studio Code.
2. Ejecutar el archivo:

```
main.py
```

3. Utilizar el menú principal para administrar productos, usuarios y ventas.

---

## Pruebas realizadas

Se verificó el correcto funcionamiento de las siguientes operaciones:

- Registro de productos.
- Registro de usuarios.
- Búsqueda de productos por código.
- Búsqueda de usuarios por identificación.
- Registro de ventas.
- Actualización automática del stock.
- Consulta de ventas por usuario.
- Reconstrucción de los índices al iniciar el programa.
- Persistencia correcta de los datos en archivos JSON.

---

## Tecnologías utilizadas

- Python 3
- Programación Orientada a Objetos (POO)
- Archivos JSON
- Colecciones (`list` y `dict`)

---

## Autor

Victor Mosquera Grefa

Programación Orientada a Objetos