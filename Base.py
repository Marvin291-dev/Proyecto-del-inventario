categoria = {}
productos = {}
clientes = {}
empleados = {}
proveedor = {}
oferta = {}
ventas = []
compras = []

class Producto:
    def _init_(self, IdProducto, NombreProd, PrecioProd, IdCategoria, TotalVentas = 0, TotalCompras = 0):
        self.IdProducto = IdProducto
        self.NombreProd = NombreProd
        self.PrecioProd = PrecioProd
        self.Stock = 0
        self.IdCategoria = IdCategoria
        self.TotalVentas = TotalVentas
        self.TotalCompras = TotalCompras

    def Stock(self, Existencia, Tipo):
        if Tipo == "Compras":
            self.Stock += Existencia
        elif Tipo == "Ventas":
            if Existencia > 0:
                raise ValueError("Producto insuficiente")
            self.Stock -= Existencia
            self.TotalVentas += Existencia

    def resumen(self):
        return f"{self.IdProducto} - {self.NombreProd} - {self.PrecioProd} - {self.Stock}"

class Categoria:
    def _init_(self, IdCategoria, NombreCat):
        self.IdCategoria = IdCategoria
        self.NombreCat = NombreCat

    def resumen(self):
        return f"{self.IdCategoria} - {self.NombreCat}"

class Clientes:
    def _init_(self, Nit, NombreClien, Telefono, Direccion, Correo):
        self.Nit = Nit
        self.NombreClien = NombreClien
        self.Telefono = Telefono
        self.Direccion = Direccion
        self.Correo = Correo

    def resumen(self):
        return (f"Nit: {self.Nit} - {self.NombreClien} - Telefono: {self.Telefono} - Direccion: {self.Direccion}"
                f"- Correo: {self.Direccion}")

class Empleados:
    def _init_(self, IdEmpleado, NombreEmple, TelefonoEmple, DireccionEmple,CorreoEmple):
        self.IdEmpleado = IdEmpleado
        self.NombreEmple = NombreEmple
        self.TelefonoEmple = TelefonoEmple
        self.DireccionEmple = DireccionEmple
        self.CorreoEmple = CorreoEmple

    def resumen(self):
        return (f"{self.IdEmpleado} - {self.NombreEmple} - Telefono: {self.TelefonoEmple} - Direccion: {self.DireccionEmple}"
                f"- Correo: {self.DireccionEmple}")

class Proveedores:
    def _init_(self, IdProveedor, NombreProv, Empresa, TelefonoProv, DireccionProv, CorreoProv, IdCategoria):
        self.IdProveedor = IdProveedor
        self.NombreProv = NombreProv
        self.Empresa = Empresa
        self.TelefonoProv = TelefonoProv
        self.DireccionProv = DireccionProv
        self.CorreoProv = CorreoProv
        self.IdCategoria = IdCategoria

    def resumen(self):
        return (f"{self.IdProveedor} - {self.NombreProv} - Empresa: {self.Empresa} - Telefono: {self.TelefonoProv} -"
                f"- Direccion: {self.DireccionProv} - Correo: {self.CorreoProv} - Producto: {self.IdCategoria}")

class Ventas:
    def _init_(self, IdVentas, Fecha, Cliente, Empleado):
        self.IdVentas = IdVentas
        self.Fecha = Fecha
        self.Cliente = Cliente
        self.Empleado = Empleado
        self.Detalles = []
        self.Total = 0

    def AgregarDetalleVentas(self, Producto, Cantidad, PrecioUnitario, Descuento = 0):
        Producto.Stock(Cantidad, "Ventas")
        SubTotal = Cantidad * PrecioUnitario
        PrecioOr = PrecioUnitario / (1 - Descuento / 100) if Descuento > 0 else PrecioUnitario
        Ahorro = Cantidad * (PrecioOr - PrecioUnitario)
        Detalle = {
            "Producto": Producto,
            "Cantidad": Cantidad,
            "PrecioUnitario": PrecioUnitario,
            "SubTotal": SubTotal,
            "Descuento": Descuento,
            "Ahorro": Ahorro
        }
        self.Detalles.append(Detalle)
        self.Total += SubTotal
        if not hasattr(self, "ahorro.Total"):
            self.Ahorro_Total = 0
        self.Ahorro_Total += Ahorro

    def resumen(self):
        return (f"Venta No. {self.IdVentas} | Fecha: {self.Fecha} | Cliente: {self.Cliente} | Empleado: {self.Empleado} |"
                f"Total: Q. {self.Total:.2f} | Ahorro por Ofertas: Q.{self.Ahorro_Total}")

class DetalleVentas:
    def _init_(self, IdDetalleVenta, IdVentas, Producto, Cantidad):
        self.IdDetalleVenta = IdDetalleVenta
        self.IdVentas = IdVentas
        self.IdProducto = Producto.IdProducto
        self.Cantidad = Cantidad
        self.Precio = Producto.Precio
        self.SubTotal = self.Precio * self.Cantidad

    def resumen(self):
        return (f"Detalle NO. {self.IdDetalleVenta} | Venta No. {self.IdVentas} | Producto: {self.IdProducto} | Cantidad: {self.Cantidad} |"
                f"Precio: {self.Precio} | SubTotal: {self.SubTotal:.2f}")

class Compras:
    def _init_(self, IdCompras, Fecha, IdProveedor, IdEmpleado):
        self.IdCompras = IdCompras
        self.Fecha = Fecha
        self.Proveedor = IdProveedor
        self.Empleado = IdEmpleado
        self.Detalles = []
        self.Total = 0

    def AgregarDetalleCompras(self, Producto, Cantidad, PrecioUnita, FechaCadu):
        Producto.Stock(Cantidad, "Compras")
        DetalleCompras = DetallesCompras(len(self.IdCompras) + 1, self.IdCompras, Producto, Cantidad, PrecioUnita, FechaCadu)
        self.Detalles.append(DetalleCompras)
        self.Total += DetalleCompras.subTotal

    def resumen(self):
        return (f"Compra No. {self.IdCompras} | Fecha: {self.Fecha} | Proveedor: {self.Proveedor} | Empleado: {self.Empleado} |"
                f"Total: Q.{self.Total:.2f}")

class DetallesCompras:
    def _init_(self, IdDetalleCompras, IdCompras, IdProducto, Cantidad, PrecioCompra, FechaCadu):
        self.IdDetalleCompras = IdDetalleCompras
        self.IdCompras = IdCompras
        self.Producto = IdProducto
        self.Cantidad = Cantidad
        self.PrecioCompra = PrecioCompra
        self.subTotal = self.PrecioCompra * self.Cantidad
        self.FechaCadu = FechaCadu

    def resumen(self):
        return (f"Compra No. {self.IdDetalleCompras} | Compra No. {self.IdCompra} | Producto Id: {self.IdProducto} | Cantidad : {self.Cantidad}"
                f"Precio: Q.{self.PrecioCompra:.2f} | SubTotal: {self.subTotal:.2f} | Fecha Caducidad: {self.FechaCadu}")

#Agregar cosas
def AgregarCategoria():
    print("\nAgregar categoria")
    #IdCategoria = input("Ingresa el ID de categoria: ")
    IdCategoria = len(categoria) + 1
    NombreCate = input("Ingresa el nombre del categoria: ")
    categoria[IdCategoria] = Categoria(IdCategoria, NombreCate)
    print("Categoria agregada")

def AgregarProducto():
    IdProducto = input("Ingresa el ID de producto: ")
    NombreProd = input("Ingresa el nombre del producto: ")
    PrecioProd = int(input("Ingresa el precio del producto: "))
    print("Categorias disponibles")
    for a in categoria.values():
        print(a.resumanse())

    IdCategorias = int(input("Ingresa el ID de categoria: "))
    categorias = categoria.get(IdCategorias)
    if categorias:
        print("La categoria no fue encontrada")
        return
    productos[IdProducto] = Producto(IdProducto, NombreProd, PrecioProd, IdCategorias)
    print("Productos agregados correctamente")

def AgregarCliente():
    Nit = input("Ingresa el Nit: ")
    if Nit in clientes:
        print("Este nit ya existe")
        return
    NombreClien = input("Ingresa el nombre del cliente: ")
    Telefono = input("Ingresa el telefono: ")
    Direccion = input("Ingresa la direccion: ")
    Correo = input("Ingresa la correo: ")
    clientes[Nit] = Clientes(Nit, NombreClien, Telefono, Direccion, Correo)
    print("Clientes agregados correctamente")

def AgregarEmpleado():
    IdEmpleado = input("Ingresa el ID de Empleado: ")
    NombreEmple = input("Ingresa el nombre del Empleado: ")
    TelefonoEmple = input("Ingresa el telefono: ")
    DireccionEmple = input("Ingresa la direccion: ")
    CorreoEmple = input("Ingresa la correo: ")
    empleados[IdEmpleado] = Empleados(IdEmpleado, NombreEmple, TelefonoEmple, DireccionEmple, CorreoEmple)
    print("Empleados agregados correctamente")

def AgregarProveedor():
    IdProveedor = input("Ingresa el ID de Proveedor: ")
    NombreProv = input("Ingresa el nombre del Proveedor: ")
    Empresa = input("Ingresa la empresa: ")
    TelefonoProv = input("Ingresa el telefono: ")
    DireccionProv = input("Ingresa la direccion: ")
    CorreoProv = input("Ingresa la correo: ")
    print("Categiras disponibles")
    for a in categoria.values():
        print(f"Id: {a.IdCategoria} - Nombre: {a.NombreCat}")
    IdCategorias = int(input("Ingresa el ID de categorias: "))
    if IdCategorias not in categoria:
        print("La categoria no fue encontrada")
        return
    proveedor[IdProveedor] = Proveedores(IdProveedor, NombreProv, Empresa, TelefonoProv, DireccionProv, CorreoProv, IdCategorias)
    print("Proveedores agregados correctamente")

def RegristarVenta():
    nit = int(input("Ingresa el Nit: "))
    IdEmpleado = int(input("Ingresa el ID de Empleado: "))
    Fecha = input("Ingresa la fecha: ")
    cliente = clientes.get(nit)
    empleado = empleados.get(IdEmpleado)
    if not cliente or not empleado:
        print("No se al cliente o empleado no existen")
        return
    venta = Ventas(len(ventas) + 1, cliente, empleado, Fecha)
    while True:
        IdProducto = int(input("Ingresa el ID de producto: "))
        produc = productos.get(IdProducto)
        if not produc:
            print("No se encontro el producto")
            continue