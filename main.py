from src.persistencia import cargar_inventario, guardar_inventario
from src.producto import Producto

RUTA_DATOS = "data/inventario.json"


def mostrar_menu():
    print("\n=================================================")
    print("     SISTEMA DE GESTIÓN DE INVENTARIO (SENA)     ")
    print("=================================================")
    print("1. Listar productos")
    print("2. Registrar nuevo producto")
    print("3. Calcular valor total del inventario global")
    print("4. Salir")


def registrar_producto(inventario: list):
    print("\n--- REGISTRO DE NUEVO PRODUCTO ---")
    codigo = input("Ingrese el código del producto: ").strip()

    for item in inventario:
        if item["codigo"].upper() == codigo.upper():
            print("Error: Ya existe un producto con ese código.")
            return

    nombre = input("Ingrese el nombre del producto: ").strip()
    categoria = input("Ingrese la categoría del producto: ").strip()

    try:
        precio = float(input("Ingrese el precio unitario del producto (COP): "))
        cantidad = int(input("Ingrese la cantidad en stock del producto: "))
    except ValueError:
        print("Error: Precio y cantidad deben ser números válidos.")
        return

    nuevo_producto = Producto(codigo, nombre, categoria, precio, cantidad)
    inventario.append(nuevo_producto.a_diccionario())

    if guardar_inventario(RUTA_DATOS, inventario):
        print("Producto registrado exitosamente y guardado en el JSON.")

def listar_productos(inventario: list):
    print("\n--- LISTA DE PRODUCTOS ---")
    if not inventario:
        print("No hay productos registrados.")
        return

    print(
        f"{'CÓDIGO':<10} | {'NOMBRE':<20} | {'CATEGORÍA':<15} | {'PRECIO':<12} {'CANT.':<6}"
    )
    print("-" * 75)
    for p in inventario:
        print(
            f"{p['codigo']:<10} | {p['nombre']:<20} | {p['categoria']:<15} | {p['precio_unitario']:<11,.2f} {p['cantidad']:<6}"
        )

def calcular_total_global(inventario: list):
     total = sum(p.get("valor_total_stock", 0) for p in inventario)
     print(
          f"\nEl total acumulado del inventario es: {total:,.2f} COP"
     )

def main():
    inventario = cargar_inventario(RUTA_DATOS)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ").strip()
        if opcion == "1":
             listar_productos(inventario)
        elif opcion == "2":
              registrar_producto(inventario)
        elif opcion == "3":
              calcular_total_global(inventario)
        elif opcion == "4":
               print("\nSaliendo del sistema. ¡Datos asegurados!")
               break
        else:
             print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()