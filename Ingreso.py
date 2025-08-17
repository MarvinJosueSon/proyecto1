productosDiccionario = {}
class Productos:
    def __init__(self,nombre,categoria,precio,stock):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock
def ingresar():
    while True:
        try:
            codigoAux=input("Ingrese el codigo del producto: ")
            if not codigoAux in productosDiccionario:
                break
            else:
                print("El codigo del producto ya existe")
        except ValueError:
            print("El codigo del producto no existe")
    while True:
        try:
            nombreAux=input("Ingrese el nombre del producto: ")
            if nombreAux != "" :
                break
            else:
                print("El nombre no puede estar en blanco")
        except ValueError:
            print("El nombre no puede estar en blanco")
    while True:
        try:
            print("Categorias disponibles: ")
            print("1. Encendedores")
            print("2. Puros")
            print("3. Miselianas")
            opcion=input("Ingrese el numero de categoria")
            if opcion == "1":
                categoriaAux="Encendedores"
                break
            elif opcion == "2":
                categoriaAux="Puros"
                break
            elif opcion == "3":
                categoriaAux="Miselianas"
                break
            else:
                print("Categoria no existente")
        except ValueError:
            print("Categoria no existente")
