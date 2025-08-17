productosDiccionario = {}

class Productos:
    def __init__(self, nombre, categoria, precio, stock):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock


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

    productoAux = Productos(nombreAux, categoriaAux, precioAux, stockAux)
    productosDiccionario[codigoAux] = {"producto": productoAux}

def quicksort(lista, clave):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x[clave] <= pivote[clave]]
        mayores = [x for x in lista[1:] if x[clave] > pivote[clave]]
        return quicksort(menores, clave) + [pivote] + quicksort(mayores, clave)

def listar_productos():
    if not productosDiccionario:
        print("No hay productos registrados.")
        return


    lista_productos = []
    for datos in productosDiccionario.values():
        p = datos["producto"]
        lista_productos.append({
            "nombre": p.nombre,
            "categoria": p.categoria,
            "precio": p.precio,
            "stock": p.stock
        })

    print("Opciones de ordenamiento:")
    print("1. Nombre")
    print("2. Precio")
    print("3. Stock")

    opcion = input("Elija el ordenamiento: ")

    if opcion == "1":
        ordenados = quicksort(lista_productos, "nombre")
    elif opcion == "2":
        ordenados = quicksort(lista_productos, "precio")
    elif opcion == "3":
        ordenados = quicksort(lista_productos, "stock")
    else:
        print("Opción inválida. Se mostrará sin ordenar.")
        ordenados = lista_productos

    print("--- LISTA DE PRODUCTOS ---")
    for p in ordenados:
        print(f"Nombre: {p['nombre']} | "
              f"Categoría: {p['categoria']} | "
              f"Precio: {p['precio']} | "
              f"Stock: {p['stock']}")
