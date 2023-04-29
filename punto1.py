def agregar(lista):
    cedula = input("Digite la cédula: ")
    nombre = input("Digite el nombre: ")
    apellido = input("Digite el apellido: ")
    correo = input("Digite el correo: ")
    lista.append([cedula, nombre, apellido, correo])


def imprimir(lista):
    print("Cédula\tNombre\tApellido\tCorreo")
    for dato in lista:
        print(*dato, sep='\t')


def buscar(lista):
    cedula = input("Ingrese la cédula: ")
    for dato in lista:
        if dato[0] == cedula:
            print("Cédula\tNombre\tApellido\tCorreo")
            print(*dato, sep='\t')
            return
    print("No se encontró la cédula en la lista.")


lista_datos = []

while True:
    print("\nMENU")
    print("1. Agregar")
    print("2. Imprimir la lista")
    print("3. Buscar")
    print("4. Salir")
    opcion = input("Elija opción: ")

    if opcion == "1":
        agregar(lista_datos)
    elif opcion == "2":
        imprimir(lista_datos)
    elif opcion == "3":
        buscar(lista_datos)
    elif opcion == "4":
        break
    else:
        print("Opción inválida. Intente de nuevo.")
        
        