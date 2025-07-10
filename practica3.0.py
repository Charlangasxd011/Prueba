talleres = {
    "Python Básico": 10,
    "Data Science": 8,
    "Ciberseguridad": 5
}

participante = []
def registrar_participante():
    try:
        nombre = input("ingrese nombre del asistente: ")
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
        print("\nTALLERES DISPONIBLES")
        for t, c in talleres.items():
            print(f"- {t} ({c} cupos)")

        taller = input("Seleccione un taller exacatamente como aparece: ")
        if taller not in talleres:
            print("Taller no existe.")
            return
        if talleres[taller] <= 0:
            print("No quedan cupos para ese taller.")
            return
        


        nuevo_participante = {
            "nombre": nombre,
            "edad": edad,
            "correo": correo,
            "taller": taller
        }
        participante.append(nuevo_participante)
        talleres[taller] -= 1
        
        print(f"Participante registrado. Cupos restantes en '{taller}': {talleres[taller]}")

    except ValueError:
        print("Error: Edad debe ser un numero entero.")    
def mostrar_participantes():
    if len(participante) == 0:
        print("No hay participantes registrados.")
        return
    print("\n---lista de Participantes---")
    for p in participante:
        print(f"Nombre : {p['nombre']} | Edad: {p['edad']} | Correo : {p['correo']} Taller : {p['taller']} ")
def buscar_participante():
    nombre_buscado = input("Ingrese el nombre del participante a buscar: ")
    for p in participante:
        if p["nombre"].lower() == nombre_buscado.lower():
            print(f"Participante encontardo : Edad: {p['edad']} | Correo : {p['correo']} Taller : {p['taller']}")
            return
    print("Asistente no encontrado.")
def eliminar_participante():
    nombre_buscado = input("Inegrese el nombre del participante a elimiar: ")
    for i in range(len(participante)):
        if participante[i]["nombre"].lower() == nombre_buscado.lower():
            participante.pop(i)
            print("participante eliminado exitosamente.")
            return
    print("participante no encontrado") 
def contar_por_taller():
    conteo = {}
    for p in participante:
        taller = p["taller"]
        if taller in conteo:
            conteo [taller] += 1
    print("\nCantidad de participantes por taller:")
    for t in talleres:
        print(f"{t}: {conteo.get(t, 0)} inscritos")

def mostar_talleres():
    print("\nTalleres disponibles y cupos:")
    for nombre, cupos in talleres.items():
        print(f". {nombre}: {cupos} cupos disponibles")


def menu():
    while True:
        try:
            print("")
            opcion = int(input("Seleccione una opcion (1-7): "))
            if opcion == 1:
                registrar_participante()
            elif opcion == 2:
                mostrar_participantes()
            elif opcion == 3:
                buscar_participante()
            elif opcion == 4:
                eliminar_participante()
            elif opcion == 5:
                contar_por_taller()
            elif opcion == 6:
                mostar_talleres()
            elif opcion == 7:
                print("Gracias por usar el sistema.")
                break
            else:
                print("Opcion invalida")    
        except ValueError:
            print("solo se admiten digitos")
menu()