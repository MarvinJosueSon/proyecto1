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
        nombreAux=input("Ingrese el nombre del producto: ")
        if nombreAux != "" :
            break
        else:
            print("El nombre no puede estar en blanco")