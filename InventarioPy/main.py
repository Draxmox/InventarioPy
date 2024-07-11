from funciones import (guardar_productos, cargar_productos, 
                       ingresar_producto, editar_producto, 
                       eliminar_producto, listar_productos, MAX_PRODUCTOS)

def main():
    productos = [{} for _ in range(MAX_PRODUCTOS)]
    num_productos = cargar_productos(productos)
    opcion = 0

    while opcion != 5:
        print("\nSistema de Inventarios para Tienda de Abarrotes")
        print("1. Ingresar Producto")
        print("2. Editar Producto")
        print("3. Eliminar Producto")
        print("4. Listar Productos")
        print("5. Salir")
        opcion = int(input("Seleccionar una opción: "))
        if opcion == 1:
            num_productos = ingresar_producto(productos, num_productos)
        elif opcion == 2:
            editar_producto(productos, num_productos)
        elif opcion == 3:
            num_productos = eliminar_producto(productos, num_productos)
        elif opcion == 4:
            listar_productos(productos, num_productos)
        elif opcion == 5:
            print("Guardando y saliendo del sistema...")
            guardar_productos(productos, num_productos)
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
