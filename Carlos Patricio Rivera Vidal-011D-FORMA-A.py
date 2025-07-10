productos = {'8475HD':['HP',15.6,'8GB','DD','1T','Intel Core i5','Nvidia GTX1050'],
             '2175HD':['Lenovo',14,'4GB','SSD','512','Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD':['Asus',14,'16GB','SSD','256GB','Intel Core i7','Nvidia RTX2080TI'],
             'fgdxFHD':['HP',15.6,'8GB','DD','1T','Intel Core i3','integrada'],
             'GF75HD':['Asus',15,6,'8GB','DD','1T','Intel Core i7','Nvidia GTX1050'],
             '123FHD':['lenovo',14,'6GB','1T','AMD Ryzen 5','Integrada'],
             '342FHD':['lenovo',15.6,'8GB','DD','1T','AMD Ryzen 7','Nvidia GTX1050'],
             'UWU131HD':['Dell',15.6,'8GB','DD','1T','AMD Ryzen3','Nvidia GTX1015']}

stock = {'8475HD':[387990,10],'2175HD':[327990,4],'JjfFHD':[429990,1],
         'fgdxFHD':[664990,21],'GF75HD':[749990,2],'123FHD':[290890,2],
         '342FHD':[444990,7],'UWU131HD':[349990,1]}

def stock_marca():
    nombre_buscado = input("Ingrese marca a consultar: ")
    for i in range(len(stock)):
        if  stock [i][""].lower() == nombre_buscado.lower():
            print(f"El stock es de: {stock}")
        
def buscar_precio():
    pass
def actualizar_precio():
    pass
def menu():
    while True:
        try:
            print("*** MENU PRINCIPAL***")
            print("1. Stock marca.")
            print("2. Busqueda por precio.")
            print("3. Actualizar precio.")
            print("4. Salir")
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                stock_marca()
            elif opcion == 2:
                buscar_precio()
            elif opcion == 3:
                actualizar_precio()
            elif opcion == 4:
                print("Programa finalizado.")
                break
            else:
                print("Debe seleccionar una opcion valida!!")




        except ValueError:
            print("Error: Debes ingresar un numero valido.")
menu()