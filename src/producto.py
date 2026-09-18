class Producto:

    def __init__(self,
                 codigo: str,
                 nombre: str,
                 categoria: str,
                 precio_unitario: float,
                 cantidad: int):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio_unitario = precio_unitario
        self.cantidad = cantidad

    def calcular_valor_total_stock(self) -> float:
        return self.precio_unitario * self.cantidad

    def a_diccionario(self) -> dict:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio_unitario": self.precio_unitario,
            "cantidad": self.cantidad,
            "valor_total_stock": self.calcular_valor_total_stock()
        }