productos = {}
categorias = {}
clientes = {}
empleados = {}
proveedor = {}
ofertas = {}
ventas = {}
compras = {}

class Productos:
    def _init_(self, IdProducto, NombreProduc, PrecioProduc, IdCategoria, TotalVentas = 0, TotalCompras = 0):
        self.IdProducto = IdProducto
        self.NombreProduc = NombreProduc
        self.PrecioProduc = PrecioProduc
        self.IdCategoria = IdCategoria
        self.Stock = 0
        self.TotalVentas = TotalVentas
        self.TotalCompras = TotalCompras

    def Stock(self, Cantidad, Tipo):
        if Tipo == 'Compra':
            self.Stock += Cantidad
        elif Tipo == 'Venta':
            if Cantidad > self.Stock:
                raise ValueError("El producto es insuficiente")
            self.Stock -= Cantidad
            self.Stock += Cantidad

    def resumen(self):
        return f"{self.IdProducto} - {self.NombreProduc} - Q.{self.PrecioProduc: .2f} - Stock: {self.Stock}"

class Categorias:
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
        return (f"Nit: {self.Nit} - {self.NombreClien} - Telefono: {self.Telefono}"
                f"- Direccion: {self.Direccion} - Correo: {self.Correo}")

class Empleados:
    def _init_(self, IdEmpleado, NombreEmpleado, TelefonoEmpleado, DireccionEmpleado, CorreoEmpleado):
        self.IdEmpleado = IdEmpleado
        self.NombreEmpleado = NombreEmpleado
        self.TelefonoEmpleado = TelefonoEmpleado
        self.DireccionEmpleado = DireccionEmpleado
        self.CorreoEmpleado = CorreoEmpleado

    def resumen(self):
        return (f"{self.IdEmpleado} - {self.NombreEmpleado} - Telefono: {self.TelefonoEmpleado} "
                f"Direccion: {self.DireccionEmpleado} - Correo: {self.CorreoEmpleado}")

class Proveedor:
    def _init_(self, IdProveedor, NombreProvee, Empresa, TelefonoProvee, DireccionProvee, CorreoProvee, IdCategoria):
        self.IdProvee = IdProveedor
        self.NombreProvee = NombreProvee
        self.Empresa = Empresa
        self.TelefonoProvee = TelefonoProvee
        self.DireccionProvee = DireccionProvee
        self.CorreoProvee = CorreoProvee
        self.IdCategoria = IdCategoria

    def resumen(self):
        return (f"{self.IdProvee} - {self.NombreProvee} - Empresa: {self.Empresa} - Telefono: {self.TelefonoProvee} - Direccoin: {self.DireccionProvee}"
                f"- Correo: {self.CorreoProvee} - Producto: {self.IdCategoria}")

class Venta:
    def __init__(self, IdVenta, Fecha, Cliente, Empleado):
        self.IdVenta = IdVenta
        self.Fecha = Fecha
        self.Cliente = Cliente
        self.Empleado = Empleado
        self.Detalles = []
        self.Total = 0

    def agregarDetalleVentas(self, Producto, Cantidad, PrecioUnitario, Descuento = 0):
        Producto.Stock(Cantidad, "Venta")
        subTotal = Cantidad * PrecioUnitario
        PrecioOriginal = PrecioUnitario / (1 - Descuento / 100) if Descuento > 0 else PrecioUnitario
        Ahorro = Cantidad * (PrecioOriginal - PrecioUnitario)
        Detalle = {
            "Producto": Producto,
            "Cantidad": Cantidad,
            "PrecioUnitario": PrecioUnitario,
            "Subtotal": subTotal,
            "Descuento": Descuento,
            "Ahorro": Ahorro
        }
        self.Detalles.append(Detalle)
        self.Total += subTotal
        if not hasattr(self, "Ahorro Total"):
            self.AhorroTotal = 0
        self.AhorroTotal += subTotal

    def resumen(self):
        return (f"Venta No: {self.IdVenta} | Fecha: {self.Fecha} | Cliente: {self.Cliente.NombreClien} | Empleado: {self.Empleado.NombreEmpleado} |"
                f"Total: Q.{self.Total: .2f} | Ahorro por oferta: Q.{self.AhorroTotal: .2f}")

class DetallesVentas:
    def __init__(self, IdDetalleVenta, IdVenta, Producto, Cantidad):
        self.IdDetalleVenta = IdDetalleVenta
        self.IdVenta = IdVenta
        self.IdProducto = Producto.IdProducto
        self.Cantidad = Cantidad
        self.Precio = Producto.Precio
        self.SubTotal = self.Precio * self.Cantidad

    def resumen(self):
        return (f"Detalle No: {self.IdDetalleVenta} | Venta No: {self.IdVenta} | Producto: {self.IdProducto} | Cantidad: {self.Cantidad} |"
                f"Precio: Q.{self.Precio: .2f} | Subtotal: Q.{self.SubTotal: .2f}")

class Compras:
    def __init__(self, IdCompras, Fecha, IdProveedor, idEmpleado):
        self.IdCompras = IdCompras
        self.Fecha = Fecha
        self.IdProveedo = IdProveedor
        self.idEmpleado = idEmpleado
        self.Detalles = []
        self.Total = 0

    def agregarDetallesCompras(self , Producto, Cantidad, PrecioUnita, FechaCaducidad):
        Producto.Stock(Cantidad, "Compras")
        detalleCompras = DetallesCompras(len(self.Detalles)+1, self.IdCompras, Producto.Id, Cantidad, PrecioUnita, FechaCaducidad)
        self.Detalles.append(detalleCompras)
        self.Total += detalleCompras.Subtotal

    def resumen(self):
        proveedores = proveedor.get(self.IdProveedo)
        empleado = empleados.get(self.idEmpleado)
        NombProvee = proveedores.NombrePro if proveedor else "Desconocido"
        nombreEmple = empleado.NombreEmple if empleado else "Desconocido"
        return (f"Compra No: {self.IdCompras} | Fecha: {self.Fecha} | Proveedorees: {NombProvee} | Empleados: {nombreEmple} |"
                f"Total: Q.{self.Total:.2f}")

class DetallesCompras:
    def _init_(self, IdDetalleCompras, IdProducto, Cantidad, precioCompra, FechaCaducidad, IdCompras):
        self.IdDetalleCompras = IdDetalleCompras
        self.IdCompras = IdCompras
        self.producto = IdProducto
        self.Cantidad = Cantidad
        self.PrecioCompra = precioCompra
        self.Subtotal = self.PrecioCompra * self.Cantidad
        self.FechaCaducidad = FechaCaducidad

    def resumen(self):
        return (f"Detalle No. {self.IdDetalleCompras} | Compra No: {self.IdCompras} | Producto: {self.IdProducto} | Cantidad: {self.Cantidad} |"
                f"Precio: Q.{self.PrecioCompra:.2f} | Subtotal: Q.{self.Subtotal: .2f} | Fecha: {self.FechaCaducidad} |")

def cargar():
    cargarProductos()
    cargarCategoria()
    cargarProveedores()
    cargarClientes()
    cargarEmpleados()
    cargarVentas()
    cargarCompras()

def AgregarCategoria():
    IdCategoria = len(categorias) + 1
    NombCat = input("Ingrese el nombre de la categoria: ")
    categorias[IdCategoria] = Categorias(IdCategoria, NombCat)
    print("Categoria cargada exitosamente")

def AgregarProductos():
    IdProducto = len(productos) + 1
    NombProducto = input("Ingrese el nombre de la producto: ")
    PrecioProd = int(input("Ingrese el precio de la producto: "))
    print("Categorias disponibles")
    for a in categorias.values():
        print(a.resumanse())
    IdCategoria = int(input("Ingrese el ID de la categoria: "))
    cate = categorias.get(IdCategoria)
    if not cate:
        print("Categoria inexistente")
        return
    productos[IdProducto] = Productos(IdProducto, NombProducto, PrecioProd, IdCategoria)
    print("Productos agregados correctamente")

def InforCliente():
    Nit = input("Ingrese el Nit: ")
    if Nit in clientes:
        print("Este nit ya existe")
        return
    NombreCliente = input("Ingrese el nombre de la cliente: ")
    Telefono = input("Ingrese el teléfono: ")
    Direccion = input("Ingrese la direccion: ")
    Correo = input("Ingrese el correo: ")
    clientes[Nit] = Clientes(Nit, NombreCliente, Telefono, Direccion, Correo)
    print("Clientes agregados correctamente")

def InforEmpleado():
    IdEmpleado = len(empleados) + 1
    NombEmpleado = input("Ingrese el nombre: ")
    TelefonoEmpleado = input("Ingrese el telefono: ")
    DireccionEmpleado = input("Ingrese la direccion: ")
    CorreoEmpleado = input("Ingrese el correo: ")
    empleados[IdEmpleado] = Empleados(IdEmpleado, NombEmpleado, TelefonoEmpleado, DireccionEmpleado, CorreoEmpleado)
    print("Empleados agregados correctamente")

def InforProveedores():
    IdProveedor = len(proveedor) + 1
    NombProvee = input("Ingrese el nombre: ")
    Empresa = input("Ingrese el empresa: ")
    TelefonoProvee = input("Ingrese el telefono: ")
    DireccionProvee = input("Ingrese la direccion: ")
    CorreoProvee = input("Ingrese el correo: ")
    print("Categorias Disponibles")
    for a in categorias.values():
        print(f"Id: {a.IdCategoria} - Nombre: {a.NombreCat}")
    IdCategoria = int(input("Ingrese el ID de la categoria: "))
    if IdCategoria in categorias:
        print("Categoria inexistente")
        return
    proveedor[IdProveedor] = Proveedor(IdProveedor, NombProvee, Empresa, TelefonoProvee, DireccionProvee, CorreoProvee, IdCategoria)
    print("Proveedores agregados correctamente")

def RegistrarVentas():
    Nit = input("Ingrese el Nit: ").strip()
    print("Empleados disponibles")
    for a in empleados.values():
        print(f"Id: {a.IdEmpleado} - Nombre: {a.NombreEmpleado}")
    IdEmpleado = int(input("Ingrese el ID de la categoria: "))
    Fecha = input("Ingrese la fecha: ")
    Cliente = clientes.get(Nit)
    empleado = empleados.get(IdEmpleado)
    if not Cliente or not empleado:
        print("El empleado o cliente no existe")
        return
    venta = Venta(len(ventas) + 1, Fecha, Cliente, empleado)
    if input("Quiere ingresar una oferta al producto (s/N): ").lower() == "s":
        RegistrarOfertas()
    while True:
        IdProducto = int(input("Ingrese el ID de la producto: "))
        producto = productos.get(IdProducto)
        if not producto:
            print("El producto no existe")
            continue
        Cantidad = int(input("Ingrese la cantidad de ventas: "))
        PrecioUnitario = producto.PrecioP
        Descuento = ofertas.get(IdProducto, 0)
        PrecioFin = PrecioUnitario * (1 - Descuento / 100)
        print(f"Descuento: {Descuento}%")
        print(f"Precio con descuento: Q{PrecioFin:.2f}")
        try:
            venta.agregarDetalleVentas(producto, Cantidad, PrecioFin, Descuento)
            print("Productos agregados con descuento correctamente")
        except ValueError as a:
            print(f"Error al agregar el producto: {a}")
        if input("Desea agregar mas productos (s/N): ").lower() == "s":
            break
    ventas.append(venta)
    print(f"Productos agregados correctamente. Total: Q.{venta.Total: .2f}")
    print(f"Ahorro total por ofertas: Q.{venta.AhorroTotal: .2f}")

def RegistrarOfertas():
    IdProducto = int(input("Ingrese el ID de la producto: "))
    producto = productos.get(IdProducto)
    if not producto:
        print("El producto no existe")
        return
    print(f"Productos seleccionados son: {producto.NombreProducto}")
    Descuento = float(input("El porcentaje de descuento es (%): "))
    if Descuento < 0 or Descuento > 100:
        print("El descuento debe de estar entre 0 a 100")
        return
    ofertas[IdProducto] = Descuento
    print(f"Ofertas registradas: {Descuento}% para los productos: '{producto.NombreProducto}' (Id: {IdProducto})")

def RegistrarCompras():
    IdProveedor = int(input("Ingrese el ID del proveedor: "))
    IdEmpleado = int(input("Ingrese el ID del empleado: "))
    Fecha = input("Ingrese la fecha: ")
    provee = proveedor.get(IdProveedor)
    empleado = empleados.get(IdEmpleado)
    if not provee or not empleado:
        print("El proveedor o empleado no existe")
        return
    compra = Compras(len(compras) + 1, Fecha, IdProveedor, IdEmpleado)
    while True:
        IdProducto = int(input("Ingrese el ID de la producto: "))
        producto = productos.get(IdProducto)
        if not producto:
            print("El producto no existe")
            continue
        Cantidad = int(input("Ingrese la cantidad de ventas: "))
        PrecioUnitario = int(input("Ingrese el precio unitario: Q. "))
        FechaCaducidad = input("La fecha de caducidad del producto es: ")
        compra.agregarDetallesCompras(producto, Cantidad, PrecioUnitario, FechaCaducidad)
        print("Productos agregados correctamente")
        if input("Desea agregar productos (s/N): ").lower() == "s":
            break
    compras.append(compra)
    print(f"Compras agregaa correctamente. Total: Q.{compra.Total: .2f}")

def MostrarCompras():
    if not compras:
        print("No hay compras")
        return
    for compra in compras:
        provee = proveedor.get(compra.IdProveedor)
        emplea = empleados.get(compra.IdEmpleado)
        nombreProveedor = provee.nombrePro if provee else "Desconocido"
        nombreEmpleado = emplea.nombreEmp if emplea else "Desconocido"
        print(f"\nId Commpras: {compra.IdCompras}")
        print(f"Fecha: {compra.Fecha}")
        print(f"Proveedor: {nombreProveedor}")
        print(f"Empleado: {nombreEmpleado}")
        print(f"Total: {compra.Total: .2f}")
        print("Detalles: ")
        for det in compra.Detalles:
            producto = det.producto
            NombreProducto = producto.NombreProduc if producto else "Desconocido"
            print(f" - Producto: {NombreProducto}")
            print(f" - Cantidad: {det.Cantidad}")
            print(f" - Precio Unitario: {det.PrecioCompra}")
            print(f" - SubTotal: {det.Subtotal: .2f}")
            print(f" - Fecha de Vencimiento: {det.FechaCaducidad}")

def MostrarVentas():
    if not ventas:
        print("No hay ventas")
        return
    for venta in ventas:
        print(f"Id Ventas: {venta.IdVenta}")
        print(f"Fecha: {venta.Fecha}")
        print(f"Clientes: {venta.Cliente.NombreClien}")
        print(f"Empleado: {venta.Empleado.NombreEmpleado}")
        print(f"Total: {venta.Total: .2f}")
        print("Detalles: ")
        for det in venta.Detalles:
            producto = det["producto"]
            print(f" Producto: {producto.NombreProduc}")
            print(f" Precio Unitario: {det["PrecioUnitario"]:.2f} ")
            print(f" Subtotal: {det["Subtotal"]:.2f}")
            print(f" Descuento aplicado: {det["descuento"]}%")

def ConsultarInven():
    print(f"Productos registrados: {len(productos)}")
    if not productos:
        print("No hay productos")
        return
    for produc in productos.values():
        NombeCategoria =categorias[produc.IdCategoria].NombreCat if produc.IdCategoria in categorias else "Sin Categorias"
        print(f"Producto: {produc.IdProducto}")
        print(f"Nombre: {produc.NombreProduc}")
        print(f"Precio Unitario: Q.{produc.PrecioProduc: .2f}")
        print(f"Stock: {produc.Stock}")
        print(f"Categoria: {NombeCategoria}")
        print(f"Total Compras: {produc.TotalCompras}")
        print(f"Total ventas: {produc.TotalVentas}")

def GuardarProductos():
    with open("Productos.txt", "w", encoding="utf-8") as archivo:
        for prod in productos.values():
            archivo.write(f"{prod.IdProducto} | {prod.NombreProduc} | {prod.PrecioProduc} | {prod.Stock} | {prod.IdCategoria} | {prod.TotalVentas} | {prod.TotalCompras}")

def cargarProductos():
    try:
        with open("Productos.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                IdProducto, Nombre, Precio, Stock, Cate, Vent, Comp = linea.strip().split(":")
                producto = Productos(int(IdProducto), Nombre, float(Precio), int(Cate), int(Vent), int(Comp))
                producto.Stock = int(Stock)
                producto[int(IdProducto)] = producto
    except FileNotFoundError:
        print("Productos.txt no existe el archivo")

def GuardarCategoria():
    with open("Categorias.txt", "w", encoding="utf-8") as archivo:
        for Cat in categorias.values():
            archivo.write(f"{Cat.IdCategoria} | {Cat.NombreCat}")

def cargarCategoria():
    try:
        with open("Categorias.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                IdCategorias, NombreCategorias = linea.strip().split(",")
                categorias[int(IdCategorias)] = Categorias(int(IdCategorias), NombreCategorias)
    except FileNotFoundError:
        print("Categorias.txt no existe el archivo")

def GuardarClientes():
    with open("Clientes.txt", "w", encoding="utf-8") as archivo:
        for Clien in clientes.values():
            archivo.write(f"{Clien.Nit} | {Clien.NombreClien} | {Clien.Telefono} | {Clien.Direccion} | {Clien.Cidade} | {Clien.Correo}")

def cargarClientes():
    try:
        with open("Clientes.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                Nit, NombreClien, TelefonoClien, DireccionClien, CorreoClie = linea.strip().split(",")
                clientes[Nit] = Clientes(Nit, NombreClien, TelefonoClien, DireccionClien, CorreoClie)
    except FileNotFoundError:
        print("Clientes.txt no existe el archivo")

def GuardarEmpleados():
    with open("Empleados.txt", "w", encoding="utf-8") as archivo:
        for Emple in empleados.values():
            archivo.write(f"{Emple.IdEmpleado} | {Emple.NombreEmpleado} | {Emple.TelefonoEmpleado} | {Emple.DireccionEmpleado} | {Emple.CorreoEmpleado}")

def cargarEmpleados():
    try:
        with open("Empleados.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                IdEmpleado, NombreEmple, TelefonoEmple, DireccionEmple, CorreoEmple = linea.strip().split(",")
                empleados[int(IdEmpleado)] = Empleados(int(IdEmpleado), NombreEmple, TelefonoEmple, DireccionEmple, CorreoEmple)
    except FileNotFoundError:
        print("Empleados.txt no existe el archivo")

def GuardarVentas():
    with open("Ventas.txt", "w", encoding="utf-8") as archivo:
        for Vent in ventas.values():
            archivo.write(f"{Vent.IdVenta} | {Vent.Fecha} | {Vent.Cliente.Nit} | {Vent.Empleado.IdEmpleado} | {Vent.TotalVentas} | {Vent.Total}")

def cargarVentas():
    try:
        with open("Ventas.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                IdDetalleVenta, Fecha, Nit, IdEmpleado, Total = linea.strip().split(",")
                cliente = clientes.get(Nit)
                emplea = empleados.get(IdEmpleado)
                ven = Venta(int(IdDetalleVenta), Fecha, cliente, emplea)
                ven.Total = float(Total)
                ventas.append(ven)
    except FileNotFoundError:
        print("Ventas.txt no existe el archivo")

def GuardarProveedores():
    with open("Proveedores.txt", "w", encoding="utf-8") as archivo:
        for Provee in proveedor.values():
            archivo.write(f"{Provee.IdProvee} | {Provee.NombreProvee} | {Provee.Empresa} | {Provee.TelefonoProvee} | {Provee.DireccionProvee} | {Provee.CorreoProvee}")

def cargarProveedores():
    try:
        with open("Proveedores.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                IdProveedor, NombreProveed, Empresa, TelefonoProveed, DireccionProvee, CorreoProvee = linea.strip().split(",")
                proveedor[int(IdProveedor)] = Proveedor(int(IdProveedor), NombreProveed, Empresa, TelefonoProveed, DireccionProvee, CorreoProvee, IdCategoria, DireccionProvee)
    except FileNotFoundError:
        print("Proveedores.txt no existe el archivo")

def GuardarDetallesVenta():
    with open("DetallesVenta.txt", "w", encoding="utf-8") as archivo:
        for Venta in ventas:
            for detella in Venta.Detalles:
                archivo.write(f"{Venta.IdVenta} | {detella["Producto"].IdProducto} | {detella["Cantidad"]} | {detella["Precio Unitario"]} | {detella["SubTotal"]} | {detella["Descuento"]}\n")

def GuardarCompras():
    with open("Compras.txt", "w", encoding="utf-8") as archivo:
        for compra in compras:
            archivo.write(f"{compra.IdCompra} | {compra.Fecha} | {compra.proveedor.IdProvee} | {compra.TotalVentas} | {compra.Total: .2f}")

def guardardetalleCom():
    with open("DetallesVenta.txt", "w", encoding="utf-8") as archivo:
       for compra in compras:
           for venta in compra.Detalles:
               archivo.write(f"{compra.IdCompras} | {venta["Producto"].IdProducto} | {venta["Cantidad"]} | {venta["Precio Unitario"]} | {venta["SubTotal"]} | {venta["Descuento"]}")

def cargarCompras():
    try:
        with open("Compras.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                IdDetalleCompra, Fecha, IdProveedor,Total = linea.strip().split(",")
                Provee = proveedor.get(IdProveedor)
                compras[IdDetalleCompra] = Compras(int(IdDetalleCompra), Fecha, Provee, Total)


def GuardarTodos():