class Venta:
    """Representa una venta realizada por un usuario."""

    def __init__(
        self,
        usuario_id: str,
        producto_codigo: str,
        cantidad: int
    ) -> None:

        if cantidad <= 0:
            raise ValueError(
                "La cantidad debe ser mayor que cero."
            )

        self.usuario_id = usuario_id.strip()
        self.producto_codigo = producto_codigo.strip().upper()
        self.cantidad = cantidad

    def to_dict(self) -> dict:
        """Convierte la venta en un diccionario."""

        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad
        }

    def mostrar_informacion(self) -> str:
        return (
            f"Usuario: {self.usuario_id} | "
            f"Producto: {self.producto_codigo} | "
            f"Cantidad: {self.cantidad}"
        )

    def __str__(self) -> str:
        return self.mostrar_informacion()