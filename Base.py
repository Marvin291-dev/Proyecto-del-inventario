Producto = {}
categoria = {}
Clientes = {}
Empleados = {}
Proveedor = {}
Ventas = {}
Compras = {}

class Productos:
    def __init__(self, IdProducto, Nombre, IdCategoria, Precio, TotalCompras = 0, TotalVentas = 0, Stock = 0):
        self.IdProducto = IdProducto
        self.Nombre = Nombre
        self.IdCategoria = IdCategoria
        self.Precio = Precio
        self.TotalCompras = TotalCompras
        self.TotalVentas = TotalVentas
        self.Stock = Stock

    def Stock(self, existencia, Tipo):
        if  Tipo == 'Compra':
            self.Stock += existencia
        elif Tipo == 'Venta':
            if existencia > self.Stock:
                raise ValueError("Productos no existe")
            self.Stock -= existencia

    def resumen(self):
        return f"{self.IdProducto} - {self.Nombre} - Q.{self.Precio} - Q.{self.TotalCompras} - Q.{self.TotalVentas} - {self.Stock}"

class Categoria:
    def __init__(self, IdCategoria, Nombre):
        self.IdCategoria = IdCategoria
        self.Nombre = Nombre

    def resumen(self):
        return f"{self.IdCategoria} - {self.Nombre}"

class Clientes:
    def __init__(self, Nit, Nombre, Telefono, Direccion, Correo):
        self.Nit = Nit
        self.Nombre = Nombre
        self.Telefono = Telefono
        self.Direccion = Direccion
        self.Correo = Correo

    def resumen(self):
        return f"Nit: {self.Nit} - {self.Nombre} - Telefono: {self.Telefono} - Direccion: {self.Direccion} - Correo: {self.Correo}"

class Empleados:
    def __init__(self, IdEmpleado, Nombre, Telefono, Direccion, Correo):
        self.IdEmpleado = IdEmpleado
        self.Nombre = Nombre
        self.Telefono = Telefono
        self.Direccion = Direccion
        self.Correo = Correo

    def resumen(self):
        return f" {self.IdEmpleado} - {self.Nombre} - Telefono: {self.Telefono} - Direccion: {self.Direccion} - Correo: {self.Correo}"

class Proveedores:
    def __init__(self, IdProveedores, Nombre, Empresa, Telefono, Direccion, Correo, IdCategoria):
        self.IdProveedores = IdProveedores
        self.Nombre = Nombre
        self.Empresa = Empresa
        self.Telefono = Telefono
        self.Direccion = Direccion
        self.Correo = Correo
        self.IdCategoria = IdCategoria

    def resumen(self):
        return f" {self.IdProveedores} - {self.Nombre} - Empresa: {self.Empresa} - Telefono: {self.Telefono} - Direccion: {self.Direccion} - Correo: {self.Correo} - IdCategoria: {self.IdCategoria}"

class Ventas:
    def __init__(self, IdVentas, Fecha, Cliente, Empleado, Categoria):
        self.IdVentas = IdVentas
        self.Fecha = Fecha
        self.Cliente = Cliente
        self.Empleado = Empleado
        self.Categoria = Categoria
        self.Detalles = []
        self.Total = 0

    def DetalleVenta(self, Producto, Cantidad):
        Producto.Stock(Cantidad, "Ventas")
        Detalles = DetallesVenta[Producto, Cantidad]
        self.Detalles.append(Detalles)
        self.Total += Detalles.SubTotal

    def resumen(self):
        return f"Venta No: {self.IdVentas} | Fecha: {self.Fecha} | Cliente: {self.Cliente} | Empleado: {self.Empleado} | Total: Q.{self.Total: 2.f}"

class DetallesVenta:
    def __init__(self, IdDetallesVentas, IdVentas, Cantidad, IdProduto, Precio, Producto):
        self.IdDetallesVentas = IdDetallesVentas
        self.IdVentas = IdVentas
        self.IdProduto = IdProduto #tengo duda
        self.Producto = Producto.id
        self.Cantidad = Cantidad
        self.Precio = Producto.precio
        self.SubTotal = self.precio * self.Cantidad

    def resumen(self):
        return (f" Detalles No: {self.IdDetallesVentas} | Venta No: {self.IdVentas} | Producto id: {self.IdProduto} | Cantidad: {self.Cantidad}"
                f"Precio: Q.{self.Precio: .2f} | Subtotal: Q.{self.SubTotal: .2f}")

class Compras:
    def __init__(self, IdCompras, Fecha, IdProveedor, IdEmpleado):
        self.IdCompras = IdCompras
        self.Fecha = Fecha
        self.IdProveedor = IdProveedor
        self.IdEmpleado = IdEmpleado
        self.Detalles = []
        self.Total = 0

    def DetalleCompra(self, Producto, Cantidad, PrecioUnidad):
        Producto.Stock(Cantidad, "Compras")
        detallesCompras = DetallesCompras(Producto, Cantidad, PrecioUnidad)
        self.Detalles.append(detallesCompras)
        self.Total += detallesCompras.SubTotal

    def resumen(self):
        return f"Compra No.{self.IdCompras} | Proveedor: {self.IdProveedor} | Empleado: {self.IdEmpleado} | Total: Q.{self.Total: 2.f}"

class DetallesCompras:
    def __init__(self, IdDetallesCompras, IdCompras, Cantidad, IdProducto, PrecioCompras, FechaCaducidad):
        self.IdDetallesCompras = IdDetallesCompras
        self.IdCompras = IdCompras
        self.Cantidad = Cantidad
        self.IdProducto = IdProducto.id
        self.PrecioCompras = PrecioCompras
        self.subTotal = self.PrecioCompras * Cantidad
        self.FechaCaducidad = FechaCaducidad

    def resumen(self):
        return (f"Detalle No: {self.IdDetallesCompras} | Compra No: {self.IdCompras} | Producto Id: {self.IdProducto} | Cantidad: {self.Cantidad}"
                f"Precio: Q{self.PrecioCompras: .2f} | Subtotal: Q{self.subTotal: .2f} | Fecha: {self.FechaCaducidad}")

#Agregar
def agregar_categoria():
    IdCategoria = input("Ingrese el ID de la categoría: ")
    if IdCategoria in categoria:
        print("Esta categoría ya existe.")
        return
    Nombre = input("Ingrese el nombre de la categoría: ")
    nueva_categoria = Categoria(IdCategoria, Nombre)
    categoria[IdCategoria] = nueva_categoria

# Función para agregar producto
def agregar_producto():
    IdProducto = input("Ingrese el ID del producto: ")
    Nombre = input("Ingrese el nombre del producto: ")
    IdCategoria = input("Ingrese el ID de la categoría: ")

    if IdCategoria not in categoria:
        print("⚠️ La categoría no existe. Agregue la categoría primero.")
        return

    try:
        Precio = float(input("Ingrese el precio del producto: "))
    except ValueError:
        print("⚠️ Precio inválido. Debe ser un número.")
        return

    Producto[IdProducto] = Productos(IdProducto, Nombre, IdCategoria, Precio)
    print("✅ Producto agregado exitosamente.")

def agregar_Clientes():
    Nit = int(input("Ingrese el nit: "))
    if Nit in Clientes:
        print("Este cliente ya esta regristado")
        return

    Nombre = input("Ingrese el nombre del cliente: ")
    Telefono = int(input("Ingrese el teléfono del cliente: "))
    Direccion = input("Ingrese la dirección del cliente: ")
    Correo = input("Ingrese el correo del cliente: ")

    nuevo_Cliente = Clientes(Nit, Nombre, Telefono, Direccion, Correo)
    Clientes[Nit] = nuevo_Cliente
    print("Cliente agregado exitosamente.")

def Agregar_Empleados():
    IdEmpleado = input("Ingrese el ID de la empleado: ")
    if IdEmpleado in Empleados:
        print("Este empleado ya existe.")
        return

    Nombre = input("Ingrese el nombre del empleado: ")
    Telefono = int(input("Ingrese el teléfono del empleado: "))
    Direccion = input("Ingrese la dirección del empleado: ")
    Correo = input("Ingrese el correo del empleado: ")

    nuevo_Empleado = Empleados(IdEmpleado, Nombre, Telefono, Direccion, Correo)
    Empleados[IdEmpleado] = nuevo_Empleado
    print("Empleado agregado exitosamente.")

def Agregar_Proveedor():
    IdProveedor = input("Ingrese el ID de la proveedor: ")
    if IdProveedor in Proveedor:
        print("Este proveedor ya existe.")
        return

    Nombre = input("Ingrese el nombre del proveedor: ")
    Empresa = input("Ingrese el nombre de la empresa: ")
    Telefono = int(input("Ingrese el teléfono del proveedor: "))
    Direccion = input("Ingrese la dirección del proveedor: ")
    Correo = input("Ingrese el correo del proveedor: ")
    IdCategoria = input("Ingrese el ID de la categoría asociada: ")

    Nuevo_Proveedor = Proveedores(IdProveedor, Nombre, Empresa, Telefono, Direccion, Correo, IdCategoria)
    Proveedor[IdProveedor] = Nuevo_Proveedor
    print("Proveedor agregado exitosamente.")

def AgregarVentas():
    IdVenta = input("Ingrese el ID de la venta: ")
    if IdVenta in Ventas:
        print("Este venta ya existe.")
        return

    Fecha = input("Ingrese "
                  "la fecha de la venta: ")
    Cliente = int(input("Ingrese el nit del cliente: "))
    Empleado = int(input("Ingrese el Id del empleado: "))
    Categoria = int(input("Ingrese el ID de la categoria: "))

    if Cliente not in Clientes:
        print("Este cliente no existe")
        return
    if Empleado not in Empleados:
        print("Este empleado no existe")
        return
    if Categoria not in categoria:
        print("Este categoria no existe")
        return

    Nuevo_Venta = Ventas(IdVenta, Fecha, Cliente, Empleado, Categoria)
    Ventas[IdVenta] = Nuevo_Venta

    while True:
        IdProducto = int(input("Ingrese el ID del producto que se vendió: "))
        if IdProducto not in Proveedor:
            break
        if IdProducto not in Productos:
            print("Este producto no existe")
            continue
        try:
            cantidad = int(input("Ingrese la cantidad vendida: "))
        except ValueError:
            print("La cantidad invalidad")
        try:
            Producto[IdProducto].Stock(cantidad, "Ventas")
            subTotal = Producto[IdProducto].precio * cantidad
            Nuevo_Venta.Detalles.append(IdProducto, cantidad, subTotal)
            Nuevo_Venta.Total += subTotal
        except ValueError as e:
            print(f"La cantidad invalidad: {e}")
            continue

    Ventas[IdVenta] = Nuevo_Venta
    print("Ventas agregada exitosamente.")
    print(Nuevo_Venta.resumen())

def agregar_compras():
    IdCompra = input("Ingrese el ID de la compra: ")
    fecha = input("Ingrese la fecha de la compra: ")
    proveedor = input("Ingrese el proveedor: ")
    empleado = input("Ingrese el empleado: ")
    compra = Compras(IdCompra, fecha, proveedor, empleado)

    Producto = []
    while True:
        p = input("Producto (fin): ")
        if p == "fin": break
        c = int(input("Cantidad: "))
        Producto[p].Stock(c, "Compras")
        precio = Producto[p].precio
        subtotal = precio * c
        Producto.append((p, c, precio, subtotal))
        compra.Total += subtotal

    compra.Detalles = Producto
    Compras[IdCompra] = compra
    print(f"Total registrado: Q. {compra.Total: .2}")

while True:
    print("------Bienvenido---------")
    print("1. Agregar Categoria")
    print("2. Agregar Producto")
    print("3. Agregar Clientes")
    print("4. Agregar Empleados")
    print("5. Agregar Proveedor")
    print("6. Agregar Ventas")
    print("7. Agregar Compras")
    print("8. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        agregar_categoria()
    elif opcion == "2":
        agregar_producto()
    elif opcion == "3":
        agregar_Clientes()
    elif opcion == "4":
        Agregar_Empleados()
    elif opcion == "5":
        Agregar_Proveedor()
    elif opcion == "6":
        AgregarVentas()
    elif opcion == "7":
        agregar_compras()
    elif opcion == "8":
        print("Saliendo...")
        break