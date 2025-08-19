productosDiccionario = {}

class Productos:
    def __init__(self, codigo, nombre, categoria, precio, stock):
        self.codigo = codigo
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
            precio = float(input("Ingrese el precio del producto en quetzales: "))
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

    productoAux = Productos(codigoAux, nombreAux, categoriaAux, precioAux, stockAux)
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


class Buscador:
    def __init__(self, productosDiccionario):
        self.productosDiccionario = productosDiccionario

    def buscar_por_codigo(self):
        codigo = input("Ingrese el codigo del producto a buscar: ")

        if codigo in self.productosDiccionario:
            producto = self.productosDiccionario[codigo]["producto"]
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
            print(f"Nombre: {producto.nombre}, Categoría: {producto.categoria}, Precio: {producto.precio}, Stock: {producto.stock}")

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


while True:
    print("\n==MENU==")
    print("1. Ingresar")
    print("2. Ver productos")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    opcion = input("Ingrese el numero de la opcion: ")

    match opcion:
        case "1":
            ingresar()
        case "2":
            listar_productos()
        case "3":
            buscador = Buscador(productosDiccionario)
            while True:
                print("\n..BUSCAR POR..")
                print("1. Buscar por codigo")
                print("2. Buscar por nombre")
                print("3. Salir")

                try:
                    subopcion = int(input("Seleccionar una opción: "))
                    match subopcion:
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

        case "4":
            actualizador = actualizar_producto(productosDiccionario)
            actualizador.actualizar()

        case "5":
            eliminador = eliminar_producto(productosDiccionario)
            eliminador.eliminar()

        case "6":
            print("Saliendo")
            break
        case _:
            print("Opcion no encontrada")
