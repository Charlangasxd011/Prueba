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
    nombre_buscado = input("Ingrese marca a consultar: ").lower()
    total_stock = 0
    for codigo, detalles in productos.items():
        marca = detalles[0].lower()
        if marca == nombre_buscado:
            if codigo in stock:
                total_stock += stock[codigo][1]
    print(f"El stock total de la marca '{nombre_buscado.capitalize()}' es: {total_stock}")

        
def buscar_precio():
    try:
        precio_min = int(input("Ingrese precio mínimo: "))
        precio_max = int(input("Ingrese precio máximo: "))
        encontrados = False
        for codigo, datos in stock.items():
            precio = datos[0]
            if precio_min <= precio <= precio_max:
                print(f"Producto {codigo} - Precio: ${precio} - Stock: {datos[1]} - Marca: {productos[codigo][0]}")
                encontrados = True
        if not encontrados:
            print("No se encontraron productos en ese rango de precios.")
    except ValueError:
        print("Debe ingresar valores numéricos válidos.")

def actualizar_precio():
    codigo = input("Ingrese el código del producto a actualizar: ")
    if codigo in stock:
        try:
            nuevo_precio = int(input("Ingrese el nuevo precio: "))
            stock[codigo][0] = nuevo_precio
            print(f"Precio actualizado correctamente para el producto {codigo}.")
        except ValueError:
            print("Debe ingresar un número válido.")
    else:
        print("El código de producto no existe.")

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