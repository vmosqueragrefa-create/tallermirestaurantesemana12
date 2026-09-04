from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante import Restaurante
from pathlib import Path

def mostrar_menu() -> None:
    print("\n====================================")
    print("      RESTAURANTE APP - SEMANA 11")
    print("====================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Registrar usuario")
    print("7. Listar usuarios")
    print("8. Vender producto")
    print("9. Consultar ventas de un usuario")
    print("10. Salir")
    print("====================================")


def registrar_producto(
    restaurante: Restaurante,
    archivo: ArchivoServicio
) -> None:

    try:
        codigo = input("Código: ")
        nombre = input("Nombre: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))

        producto = Producto(
            codigo,
            nombre,
            categoria,
            precio,
            stock
        )

        if restaurante.registrar_producto(producto):

            archivo.guardar_productos(
                restaurante.listar_productos()
            )

            print("\nProducto registrado correctamente.")

        else:
            print("\nYa existe un producto con ese código.")

    except ValueError as error:
        print(f"\n{error}")


def listar_productos(restaurante: Restaurante) -> None:

    productos = restaurante.listar_productos()

    if not productos:
        print("\nNo existen productos.")
        return

    print("\n====== PRODUCTOS ======")

    for producto in productos:
        print(producto)


def buscar_producto(restaurante: Restaurante) -> None:

    codigo = input("\nCódigo: ")

    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("\nProducto no encontrado.")
    else:
        print(producto)


def actualizar_producto(
    restaurante: Restaurante,
    archivo: ArchivoServicio
) -> None:

    codigo = input("\nCódigo del producto: ")

    if restaurante.buscar_producto(codigo) is None:
        print("\nProducto no encontrado.")
        return

    try:

        nombre = input("Nuevo nombre: ")
        categoria = input("Nueva categoría: ")
        precio = float(input("Nuevo precio: "))
        stock = int(input("Nuevo stock: "))

        if restaurante.actualizar_producto(
            codigo,
            nombre,
            categoria,
            precio,
            stock
        ):

            archivo.guardar_productos(
                restaurante.listar_productos()
            )

            print("\nProducto actualizado correctamente.")

    except ValueError as error:
        print(error)


def eliminar_producto(
    restaurante: Restaurante,
    archivo: ArchivoServicio
) -> None:

    codigo = input("\nCódigo: ")

    if restaurante.eliminar_producto(codigo):

        archivo.guardar_productos(
            restaurante.listar_productos()
        )

        print("\nProducto eliminado.")

    else:
        print("\nProducto no encontrado.")


def registrar_usuario(
    restaurante: Restaurante,
    archivo: ArchivoServicio
) -> None:

    try:

        identificacion = input("Identificación: ")
        nombre = input("Nombre: ")

        usuario = Usuario(
            identificacion,
            nombre
        )

        if restaurante.registrar_usuario(usuario):

            archivo.guardar_usuarios(
                restaurante.listar_usuarios()
            )

            print("\nUsuario registrado.")

        else:

            print("\nEse usuario ya existe.")

    except ValueError as error:
        print(error)


def listar_usuarios(restaurante: Restaurante) -> None:

    usuarios = restaurante.listar_usuarios()

    if not usuarios:
        print("\nNo existen usuarios.")
        return

    print("\n====== USUARIOS ======")

    for usuario in usuarios:
        print(usuario)
def vender_producto(
    restaurante: Restaurante,
    archivo: ArchivoServicio
) -> None:

    codigo = input("\nCódigo del producto: ")
    usuario = input("Identificación del usuario: ")

    try:
        cantidad = int(input("Cantidad: "))

        if restaurante.vender_producto(
            codigo,
            usuario,
            cantidad
        ):

            archivo.guardar_productos(
                restaurante.listar_productos()
            )

            archivo.guardar_ventas(
                restaurante.listar_ventas()
            )

            print("\nVenta registrada correctamente.")

        else:
            print(
                "\nNo fue posible realizar la venta."
            )

    except ValueError:
        print("\nLa cantidad debe ser un número entero.")


def consultar_ventas_usuario(
    restaurante: Restaurante
) -> None:

    identificacion = input(
        "\nIdentificación del usuario: "
    )

    ventas = restaurante.consultar_ventas_usuario(
        identificacion
    )

    if not ventas:
        print("\nEl usuario no registra ventas.")
        return

    print("\n======= VENTAS =======")

    for venta in ventas:
        print(venta)


def main() -> None:

    ruta_datos = Path(__file__).resolve().parent / "datos"
    archivo = ArchivoServicio(str(ruta_datos))
    restaurante = Restaurante()

    
# Reconstrucción de índices 


    restaurante.productos_por_codigo = {
    producto.codigo: producto
    for producto in restaurante.productos
}

    restaurante.usuarios_por_id = {
    usuario.identificacion: usuario
    for usuario in restaurante.usuarios
}

    restaurante.ventas_por_usuario = {}

    for venta in restaurante.ventas:
        
     if venta.usuario_id not in restaurante.ventas_por_usuario:
        restaurante.ventas_por_usuario[venta.usuario_id] = []

        restaurante.ventas_por_usuario[
        venta.usuario_id: str
    ].append(venta)

    print("\n====================================")
    print("      RESTAURANTE APP")
    print("====================================")

    while True:

        mostrar_menu()

        opcion = input(
            "\nSeleccione una opción: "
        )

        if opcion == "1":
            registrar_producto(
                restaurante,
                archivo
            )

        elif opcion == "2":
            listar_productos(restaurante)

        elif opcion == "3":
            buscar_producto(restaurante)

        elif opcion == "4":
            actualizar_producto(
                restaurante,
                archivo
            )

        elif opcion == "5":
            eliminar_producto(
                restaurante,
                archivo
            )

        elif opcion == "6":
            registrar_usuario(
                restaurante,
                archivo
            )

        elif opcion == "7":
            listar_usuarios(restaurante)

        elif opcion == "8":
            vender_producto(
                restaurante,
                archivo
            )

        elif opcion == "9":
            consultar_ventas_usuario(
                restaurante
            )

        elif opcion == "10":
            print("\nPrograma finalizado.")
            break

        else:
            print("\nOpción inválida.")


if __name__ == "__main__":
    main()