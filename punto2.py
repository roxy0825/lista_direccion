def agregar_producto(diccionario):
    nombre = input("Digite el nombre del producto: ")
    precio = float(input("Digite el precio del producto: "))
    descripcion = input("Digite la descripción del producto: ")
    diccionario[nombre] = {"Precio": precio, "Descripción": descripcion}
    print("Producto agregado.")

def imprimir_productos(diccionario):
    print("PRODUCTOS")
    print("Nombre\tPrecio\tDescripción")
    for nombre, datos in diccionario.items():
        print(f"{nombre}\t{datos['Precio']}\t{datos['Descripción']}")


nombre_diccionario = input("Ingrese el nombre de la lista: ")

diccionario_productos = {}

while True:
    print("\nMENU PRODUCTO")
    print("1. Agregar ")
    print("2. Imprimir ")
    print("3. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        agregar_producto(diccionario_productos)
    elif opcion == "2":
        imprimir_productos(diccionario_productos)
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Intente de nuevo.")

print(f"El diccionario de productos {nombre_diccionario} ha sido cerrado.")