import json

MAX_PRODUCTOS = 100
FILE_NAME = "productos.json"

def guardar_productos(productos, num_productos):
    with open(FILE_NAME, "w") as file:
        data = productos[:num_productos]
        json.dump(data, file)
    print("Productos guardados exitosamente.")

def cargar_productos(productos):
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            num_productos = len(data)
            for i in range(num_productos):
                productos[i] = data[i]
            return num_productos
    except FileNotFoundError:
        print("No se encontró el archivo de productos, se creará uno nuevo.")
        return 0

def ingresar_producto(productos, num_productos):
    if num_productos >= MAX_PRODUCTOS:
        print("Límite de productos alcanzado")
        return num_productos
    nombre = input("Ingresar nombre del producto: ")
    cantidad = int(input("Ingresar cantidad: "))
    precio = float(input("Ingresar precio: "))
    categoria = input("Ingresar categoría: ")
    productos[num_productos] = {
        'nombre': nombre,
        'cantidad': cantidad,
        'precio': precio,
        'categoria': categoria
    }
    num_productos += 1
    guardar_productos(productos, num_productos)
    return num_productos

def editar_producto(productos, num_productos):
    nombre = input("Ingresar nombre del producto a editar: ")
    for i in range(num_productos):
        if productos[i]['nombre'] == nombre:
            print("Producto encontrado. Ingresar nueva cantidad: ")
            productos[i]['cantidad'] = int(input())
            print("Ingresar nuevo precio: ")
            productos[i]['precio'] = float(input())
            print("Ingresar nueva categoría: ")
            productos[i]['categoria'] = input()
            guardar_productos(productos, num_productos)
            return
    print("Producto no encontrado.")

def eliminar_producto(productos, num_productos):
    nombre = input("Ingresar nombre del producto a eliminar: ")
    for i in range(num_productos):
        if productos[i]['nombre'] == nombre:
            for j in range(i, num_productos - 1):
                productos[j] = productos[j + 1]
            num_productos -= 1
            guardar_productos(productos, num_productos)
            print("Producto eliminado.")
            return num_productos
    print("Producto no encontrado.")
    return num_productos

def listar_productos(productos, num_productos):
    if num_productos == 0:
        print("No hay productos ingresados.")
        return

    print("+----------------------------+----------+---------+----------------------------+")
    print("| Nombre                     | Cantidad | Precio  | Categoría                  |")
    print("+----------------------------+----------+---------+----------------------------+")

    for i in range(num_productos):
        print("| {:<26} | {:<8} | {:<7.2f} | {:<26} |".format(
            productos[i]['nombre'], productos[i]['cantidad'], productos[i]['precio'], productos[i]['categoria']))

    print("+----------------------------+----------+---------+----------------------------+")
