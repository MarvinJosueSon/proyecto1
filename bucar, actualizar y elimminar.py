#ingreso que marvin hiso, no pude ver la parte del codigo que le toco
productosDiccionario = {}

class Productos:
    def __init__(self, nombre, categoria, precio, stock, codigo):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock
        self.codigo = codigo


def validar_codigo():
    while True:
        codigo = input("Ingrese el código del producto: ")
        if codigo not in productosDiccionario:
            return codigo
        else:
            print("El código del producto ya existe")


def validar_nombre():
    while True:
        nombre = input("Ingrese el nombre del producto: ")
        if nombre.strip() != "":
            return nombre
        else:
            print("El nombre no puede estar en blanco")


def validar_categoria():
    while True:
        print("Categorías disponibles: ")
        print("1. Encendedores")
        print("2. Puros")
        print("3. Miselianas")
        opcion = input("Ingrese el número de categoría: ")
        if opcion == "1":
            return "Encendedores"
        elif opcion == "2":
            return "Puros"
        elif opcion == "3":
            return "Miselianas"
        else:
            print("Categoría no existente")


def validar_precio():
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio > 0:
                return precio
            else:
                print("El precio no puede ser menor o igual a 0")
        except ValueError:
            print("El precio debe ser ingresado en números")


def validar_stock():
    while True:
        try:
            stock = int(input("Ingrese el stock del producto: "))
            if stock > 0:
                return stock
            else:
                print("El stock no puede ser menor o igual a 0")
        except ValueError:
            print("El stock debe ser ingresado en números enteros")


def ingresar():
    codigoAux = validar_codigo()
    nombreAux = validar_nombre()
    categoriaAux = validar_categoria()
    precioAux = validar_precio()
    stockAux = validar_stock()

    productoAux = Productos(nombreAux, categoriaAux, precioAux, stockAux, codigoAux)
    productosDiccionario[codigoAux] = {"producto": productoAux}





#MI PARTE DEL PROYECTO
class Buscador:
    def __init__(self, productosDiccionario):
        self.productosDiccionario = productosDiccionario

    def buscar_por_codigo(self):
        codigo = input("Ingrese el codigo del producto a buscar: ")

        for cod, datos in self.productosDiccionario.items():
            producto = datos["producto"]
            if cod == codigo:
                print("\n_-PRODUCTO ENCONTRADO-_:")
                print(f"Codigo: {producto.codigo}")
                print(f"Nombre: {producto.nombre}")
                print(f"Categoria: {producto.categoria}")
                print(f"Precio: {producto.precio}")
                print(f"Stock: {producto.stock}")
                return producto

        print("\nNO SE ENCONTRO NINGUN PRODUCTO CON ESE CODIGO...")
        return None

    def buscar_por_nombre(self):
        nombre = input("Ingrese el nombre del producto a buscar: ").lower()
        encontrado = []

        for datos in self.productosDiccionario.values():
            producto = datos["producto"]
            if nombre in producto.nombre.lower():
                encontrado.append(producto)

        if encontrado:
            print("\nPRODUCTOS ENCONTRADOS POR NOMBRE:")
            for p in encontrado:
                print(f"Código: {p.codigo}, Nombre: {p.nombre}, Categoría: {p.categoria}, Precio: {p.precio}, Stock: {p.stock}")
            return encontrado
        else:
            print("\n---NO SE ENCONTRO NINGUN PRODUCTO CON ESE NOMBRE---")
            return None




class actualizar_producto:
    def __init__(self, productosDiccionario):
        self.productosDiccionario = productosDiccionario

    def actualizar(self):
        codigo = input("Ingrese el codigo del producto a actualizar: ")

        if codigo in self.productosDiccionario:
            producto = self.productosDiccionario[codigo]["producto"]
            print("\nPRODUCTO ENCONTRADO:")
            print(f"Mombre: {producto.nombre}, Categoría: {producto.categoria}, Precio: {producto.precio}, Stock: {producto.stock}")

            while True:
                try:
                    precio_nuevo = float(input("Ingrese el nuevo precio: "))
                    if precio_nuevo > 0:
                        producto.precio = precio_nuevo
                        break
                    else:
                        print("EL PRECIO DEBE SER MAYOR A 0...")
                except ValueError:
                    print("ERROR...INGRESE UN NUMERO VALIDO.")

            while True:
                try:
                    stock_nuevo = int(input("INGRESE LA CANTIDAD EN STOCK: "))
                    if stock_nuevo >= 0:
                        producto.stock = stock_nuevo
                        break
                    else:
                        print("NO PUEDE SER NEGATIVO EL ESTOCK...")
                except ValueError:
                    print("ERROR...INGRESE UN NUMERO VALIDO.")

            print("\nPRODUCTO ACTUALIZADO CORRECTAMENTE...")
        else:
            print("\nERROR---NO SE ENCONTRO EL PRODUCTO---")



class eliminar_producto:
    def __init__(self, productosDiccionario):
        self.productosDiccionario = productosDiccionario

    def eliminar(self):
        codigo = input("Ingrese el codigo del producto a eliminar: ")

        if codigo in self.productosDiccionario:
            producto = self.productosDiccionario.pop(codigo)["producto"]
            print(f"\nPRODUCTO '{producto.nombre}' ELIMINADO CORRECTAMENTE.")
        else:
            print("\nNO SE ENCONTRO EL PRODUCTO...")

ingresar()
print()
buscador = Buscador(productosDiccionario)
while True:
    print("..BUSCAR POR..")
    print("1. buscar por codigo")
    print("2. buscar por nombre")
    print("3. Salir")

    try:
        opcion = int(input("Seleccionar una opción: "))
        match opcion:
            case 1:
                buscador.buscar_por_codigo()
            case 2:
                buscador.buscar_por_nombre()
            case 3:
                print("SALIENDO")
                break
            case _:
                print("Opción no válida.\n")
    except ValueError:
        print("Error: DEBE INGRESAR UN NUMERO ENTERO.\n")

actualizador = actualizar_producto(productosDiccionario)
actualizador.actualizar()
eliminador = eliminar_producto(productosDiccionario)
eliminador.eliminar()
