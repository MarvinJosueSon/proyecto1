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
                print("\nProducto encontrado:")
                print(f"Codigo: {producto.codigo}")
                print(f"Nombre: {producto.nombre}")
                print(f"Categoria: {producto.categoria}")
                print(f"Precio: {producto.precio}")
                print(f"Stock: {producto.stock}")
                return producto

        print("\nNo se encontró ningún producto con ese código.")
        return None

ingresar()
buscador = Buscador(productosDiccionario)
buscador.buscar_por_codigo()