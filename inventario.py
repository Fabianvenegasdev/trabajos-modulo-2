import csv

# Diccionario inicial del inventario
inventario = {}

def agregar_producto(nombre: str, cantidad: int, precio: float, categoria: str):
    """
    Agrega un producto al inventario si no existe ya.
    Valida que la cantidad y el precio sean positivos.
    """
    if nombre in inventario:
        print("El producto ya está en el inventario.")
        return

    if cantidad < 0 or precio < 0:
        print("Cantidad o precio no pueden ser negativos.")
        return

    inventario[nombre] = {
        'cantidad': cantidad,
        'precio': precio,
        'categoria': categoria
    }
    print(f"Producto '{nombre}' agregado exitosamente.")

def eliminar_producto(nombre: str):
    """
    Elimina un producto del inventario si existe.
    """
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado correctamente.")
    else:
        print(f"No se encontró el producto '{nombre}' en el inventario.")

def actualizar_producto(nombre: str, cantidad=None, precio=None):
    """
    Actualiza los valores de cantidad y/o precio de un producto existente.
    """
    if nombre not in inventario:
        print(f"No se puede actualizar: '{nombre}' no está en el inventario.")
        return

    if cantidad is not None and cantidad >= 0:
        inventario[nombre]['cantidad'] = cantidad
    elif cantidad is not None:
        print("La cantidad no puede ser negativa.")

    if precio is not None and precio >= 0:
        inventario[nombre]['precio'] = precio
    elif precio is not None:
        print("El precio no puede ser negativo.")

def listar_por_categoria(categoria: str):
    """
    Muestra todos los productos que pertenecen a una categoría específica.
    """
    encontrado = False
    print(f"\nProductos en la categoría '{categoria}':")
    for nombre, detalles in inventario.items():
        if detalles['categoria'] == categoria:
            print(f"- {nombre}: {detalles['cantidad']} unidades, ${detalles['precio']:.2f}")
            encontrado = True
    if not encontrado:
        print("No hay productos en esta categoría.")

def calcular_valor_total():
    """
    Devuelve el valor total del inventario basado en cantidad * precio de cada producto.
    """
    valor_total = sum(detalles['cantidad'] * detalles['precio'] for detalles in inventario.values())
    return valor_total

def exportar_inventario_csv(nombre_archivo: str):
    """
    Exporta el inventario actual a un archivo CSV con las columnas:
    Producto, Cantidad, Precio, Categoría.
    """
    try:
        with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo_csv:
            encabezados = ['Producto', 'Cantidad', 'Precio', 'Categoría']
            escritor = csv.writer(archivo_csv)
            escritor.writerow(encabezados)

            for nombre, detalles in inventario.items():
                escritor.writerow([nombre, detalles['cantidad'], detalles['precio'], detalles['categoria']])
            print(f"Inventario exportado exitosamente a '{nombre_archivo}'.")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    # Agregar algunos productos de ejemplo
    agregar_producto("Laptop", 10, 700, "Electrónica")
    agregar_producto("Manzana", 50, 0.5, "Alimentos")
    agregar_producto("Camiseta", 30, 15, "Ropa")
    agregar_producto("Tablet", 15, 300, "Electrónica")

    # Actualizar uno de los productos
    actualizar_producto("Manzana", cantidad=40, precio=0.6)

    # Listar productos por categoría
    listar_por_categoria("Electrónica")

    # Mostrar valor total del inventario
    total = calcular_valor_total()
    print(f"\nValor total del inventario: ${total:.2f}")

    # Exportar inventario a CSV
    exportar_inventario_csv("inventario.csv")