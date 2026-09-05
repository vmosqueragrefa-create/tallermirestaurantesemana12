class Venta:
    def __init__(self, id_usuario, id_producto, cantidad: int = 1):
        self.id_usuario = id_usuario
        # Asignamos primero el producto para que la validación de cantidad pueda consultar su stock
        self.id_producto = id_producto  
        self.cantidad = cantidad
        

    # --- Método estático de validación general ---
    @staticmethod
    def validar_numero_positivo(valor, nombre_campo="Valor"):
        """Valida que el dato ingresado sea un número estrictamente mayor a 0."""
        if not isinstance(valor, (int, float)) or isinstance(valor, bool):
            raise TypeError(f"El valor de '{nombre_campo}' debe ser un número (int o float).")
        if valor <= 0:
            raise ValueError(f"El valor de '{nombre_campo}' debe ser mayor a cero.")
        return True

    # --- Propiedad y Setter para Cantidad ---
    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):
        # 1. Validar que sea un número positivo
        self.validar_numero_positivo(valor, "Cantidad")
        
        # 2. Validar contra el stock del producto (si el objeto producto tiene atributo stock)
        if hasattr(self, 'producto') and self.producto and hasattr(self.producto, 'stock'):
            if valor > self.producto.stock:
                raise ValueError(
                    f"La cantidad solicitada ({valor}) supera el stock disponible ({self.producto.stock})."
                )
        
        self._cantidad = int(valor)

    # --- Propiedad y Setter para Precio Unitario ---
    @property
    def precio_unitario(self):
        return self._precio_unitario

    @precio_unitario.setter
    def precio_unitario(self, valor):
        self.validar_numero_positivo(valor, "Precio Unitario")
        self._precio_unitario = float(valor)

    # --- Método para calcular el total de la venta ---
    def calcular_total(self):
        return self.cantidad * self.precio_unitario

    # --- Representación a Diccionario para guardar en JSON ---
    def a_diccionario(self):
        return {
            "usuario_id": str(self.id_usuario),
            "producto_codigo": str(self.id_producto),
            "cantidad": str(self.cantidad),
        }

    # --- Alias to_dict para compatibilidad con archivo_servicio.py ---
    def to_dict(self):
        return self.a_diccionario()