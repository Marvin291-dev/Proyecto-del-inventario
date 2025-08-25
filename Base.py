Producto = {}
categoria = {}
Clientes = {}
Empleados = {}
Proveedor = {}
Ventas = {}
Compras = {}

class Productos:
    def __int__(self, IdProducto, Nombre, IdCategoria, Precio, TotalCompras = 0, TotalVentas = 0, Stock = 0):
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
    def __int__(self, IdCategoria ,Nombre):
        self.IdCategoria = IdCategoria
        self.Nombre = Nombre

    def resumen(self):
        return f"{self.IdCategoria} - {self.Nombre}"

class Clientes:
    def __int__(self, Nit, Nombre, Telefono, Direccion, Correo):
        self.Nit = Nit
        self.Nombre = Nombre
        self.Telefono = Telefono
        self.Direccion = Direccion
        self.Correo = Correo

    def resumen(self):
        return f"Nit: {self.Nit} - {self.Nombre} - Telefono: {self.Telefono} - Direccion: {self.Direccion} - Correo: {self.Correo}"

class Empleados:
    def __int__(self, IdEmpleado, Nombre, Telefono, Direccion, Correo):
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
    def __int__(self, IdVentas, Fecha, Cliente, Empleado, Categoria):
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
def AgregarCategoria():
    Idcategoria = input("Ingrese el ID Producto: ")
    nombre = input("Ingrese el nombre de la categoria: ")
    categoria[Idcategoria] = Categoria(Idcategoria, nombre)
    print("Se ingreso la categoria exitosamente")

while True:
    print("------Bienvenido---------")
    print("1. Agregar Producto")
    print("2. Agregar Categoria")
    print("3. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        AgregarCategoria()
    elif opcion == "2":
        print("Saliendo...")
        break