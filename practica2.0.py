asistentes = []

def registrar_asistente():
    try:
        nombre = input("Ingrese nombre del asisitente: ")
        if nombre.isdigit():
            print("Error: El nombre no puede ser numerico.")
            return
        edad = int(input("Ingrese edad del asistente: "))
        if edad <= 0:
            print("Error: Edad invalida.")
            return
        correo = input("Ingrese el correo electrónico: ")
        if "@" not in correo or "." not in correo:
            print("Correo inválido.")
            return
        nuevo_asistente = {
            "nombre": nombre,
            "edad": edad,
            "correo": correo
        }
        asistentes.append(nuevo_asistente)
        print("Asistente registrado con exito.")
    except ValueError:
        print("Error")

def mostrar_asistentes():
    if len(asistentes) == 0:
        print("No hay asistentes registarados.")
        return
    print("\n---Lista de Asistentes---")
    for a in asistentes:
        print(f"Nombre: {a['nombre']} | Edad: {a['edad']} | Correo: {a['correo']}")

def buscar_asistente():
    nombre_buscado = input("ingrese el nombre del socio a buscar: ")
    for a in asistentes:
        if a["nombre"].lower() == nombre_buscado.lower():
            print(f"Asistente encontrado : Edad: {a['edad']} | Correo: {a['correo']} ")
            return
    print("Asistente no encontrado.")
def eliminar_asistente():
    nombre_buscado = input("ingrese el nombre del asistente a eliminar: ")
    for i in range(len(asistentes)):
        if asistentes[i]["nombre"].lower() == nombre_buscado.lower():
            asistentes.pop(i)
            print("asistente eliminado exitosamente.")
            return
    print("Aistente no encontrado.")

def contar_mayores_edad():
    contador = 0
    for a in asistentes:
        if a["edad"] >= 18:
            contador +=1
        print(f"Total de asistentes mayores de edad: {contador}.")

    

def menu():
    while True:
        print("1. Registrar asistente")
        print("2. Ver asistentes")
        print("3. Buscar asistente")
        print("4. Eliminar asistente")
        print("5. Contar mayores de edad")
        print("6. Salir")
        try:
            opcion = int(input("Seleccione una opción (1-6): "))
            if opcion == 1:
                registrar_asistente()
            elif opcion == 2:
                mostrar_asistentes()
            elif opcion == 3:
                buscar_asistente()
            elif opcion == 4:
                eliminar_asistente()
            elif opcion == 5:
                contar_mayores_edad()
            elif opcion == 6:
                print("Gracias por usar el sistema.")
                break
            else:
                print("Opcion invalida")
        except ValueError:
            print("Debe ingresar un número válido")

menu()
