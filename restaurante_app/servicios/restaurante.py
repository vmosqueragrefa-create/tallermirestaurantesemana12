from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class Restaurante:
    """Administra productos, usuarios y ventas."""

    def __init__(self) -> None:
        self.productos: list[Producto] = []
        self.usuarios: list[Usuario] = []
        self.ventas: list[Venta] = []

        # Índices auxiliares
        self.productos_por_codigo = {}
        self.usuarios_por_id = {}
        self.ventas_por_usuario = {}

    # ==========================
    # PRODUCTOS
    # ==========================

    def registrar_producto(self, producto: Producto) -> bool:

        if producto.codigo in self.productos_por_codigo:
            return False

        self.productos.append(producto)
        self.productos_por_codigo[producto.codigo] = producto

        return True

    def buscar_producto(self, codigo: str) -> Producto | None:

        codigo = codigo.strip().upper()

        return self.productos_por_codigo.get(codigo)

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        stock: int
    ) -> bool:

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        producto.nombre = Producto.validar_nombre(nombre)
        producto.categoria = Producto.validar_categoria(categoria)
        producto.precio = Producto.validar_precio(precio)
        producto.stock = Producto.validar_stock(stock)

        return True

    def eliminar_producto(self, codigo: str) -> bool:

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        self.productos.remove(producto)
        del self.productos_por_codigo[producto.codigo]

        return True

    def listar_productos(self) -> list[Producto]:
        return self.productos

    # ==========================
    # USUARIOS
    # ==========================

    def registrar_usuario(self, usuario: Usuario) -> bool:

        if usuario.identificacion in self.usuarios_por_id:
            return False

        self.usuarios.append(usuario)
        self.usuarios_por_id[usuario.identificacion] = usuario

        return True

    def buscar_usuario(
        self,
        identificacion: str
    ) -> Usuario | None:

        identificacion = identificacion.strip()

        return self.usuarios_por_id.get(identificacion)

    def listar_usuarios(self) -> list[Usuario]:
        return self.usuarios

    # ==========================
    # VENTAS
    # ==========================

    def vender_producto(
        self,
        codigo_producto: str,
        identificacion_usuario: str,
        cantidad: int
    ) -> bool:

        usuario = self.buscar_usuario(
            identificacion_usuario
        )

        producto = self.buscar_producto(
            codigo_producto
        )

        if usuario is None:
            return False

        if producto is None:
            return False

        if cantidad <= 0:
            return False

        if producto.stock < cantidad:
            return False

        producto.vender(cantidad)

        venta = Venta(
            usuario.identificacion,
            producto.codigo,
            cantidad
        )

        self.ventas.append(venta)

        if usuario.identificacion not in self.ventas_por_usuario:
            self.ventas_por_usuario[usuario.identificacion] = []

        self.ventas_por_usuario[usuario.identificacion].append(venta)

        return True

    def listar_ventas(self) -> list[Venta]:
        return self.ventas

    def consultar_ventas_usuario(
        self,
        identificacion: str
    ) -> list[Venta]:

        return self.ventas_por_usuario.get(
            identificacion,
            []
        )