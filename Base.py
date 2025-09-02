productos = {}
categorias = {}
clientes = {}
empleados = {}
proveedor = {}
ofertas = {}
ventas = {}
compras = {}

class Productos:
    def __init__(self, idproducto, nombreproduc, precioproduc, idcategoria, totalventas = 0, totalcompras = 0):
        self.idproducto = idproducto
        self.nombreproduc = nombreproduc
        self.precioproduc = precioproduc
        self.idcategoria = idcategoria
        self.stock = 0
        self.totalventas = totalventas
        self.totalcompras = totalcompras

    def Stock(self, cantidad, tipo):
        if tipo == 'Compra':
            self.stock += cantidad
        elif tipo == 'Venta':
            if cantidad > self.Stock:
                raise ValueError("El producto es insuficiente")
            self.stock -= cantidad
            self.stock += cantidad

    def resumen(self):
        return f"{self.idproducto} - {self.nombreproduc} - Q.{self.precioproduc: .2f} - Stock: {self.stock}"

class Categorias:
    def __init__(self, idcategoria, nombrecat):
        self.idcategoria = idcategoria
        self.nombrecat = nombrecat

    def resumen(self):
        return f"{self.idcategoria} - {self.nombrecat}"

class Clientes:
    def __init__(self, nit, nombreclien, telefono, direccion, correo):
        self.nit = nit
        self.nombreclien = nombreclien
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo

    def resumen(self):
        return (f"Nit: {self.nit} - {self.nombreclien} - Telefono: {self.telefono}"
                f"- Direccion: {self.direccion} - Correo: {self.correo}")

class Empleados:
    def __init__(self, idempleado, nombreempleado, telefonoempleado, direccionempleado, correoempleado):
        self.idempleado = idempleado
        self.nombreempleado = nombreempleado
        self.telefonoempleado = telefonoempleado
        self.direccionempleado = direccionempleado
        self.correoempleado = correoempleado

    def resumen(self):
        return (f"{self.idempleado} - {self.nombreempleado} - Telefono: {self.telefonoempleado} "
                f"Direccion: {self.direccionempleado} - Correo: {self.correoempleado}")

class Proveedor:
    def __init__(self, idproveedor, nombreprovee, empresa, telefonoprovee, direccionprovee, correoprovee, idcategoria):
        self.idprovee = idproveedor
        self.nombreprovee = nombreprovee
        self.empresa = empresa
        self.telefonoprovee = telefonoprovee
        self.direccionprovee = direccionprovee
        self.correoprovee = correoprovee
        self.idcategoria = idcategoria

    def resumen(self):
        return (f"{self.idprovee} - {self.nombreprovee} - Empresa: {self.empresa} - Telefono: {self.telefonoprovee} - Direccoin: {self.direccionprovee}"
                f"- Correo: {self.correoprovee} - Producto: {self.idcategoria}")

class Venta:
    def __init__(self, idventa, fecha, cliente, empleado):
        self.idventa = idventa
        self.fecha = fecha
        self.cliente = cliente
        self.empleado = empleado
        self.detalles = []
        self.total = 0

    def agregarDetalleVentas(self, producto, cantidad, preciounitario, descuento = 0):
        producto.Stock(cantidad, "Venta")
        subtotal = cantidad * preciounitario
        preciooriginal = preciounitario / (1 - descuento / 100) if descuento > 0 else preciounitario
        ahorro = cantidad * (preciooriginal - preciounitario)
        detalle = {
            "Producto": producto,
            "Cantidad": cantidad,
            "PrecioUnitario": preciounitario,
            "Subtotal": subtotal,
            "Descuento": descuento,
            "Ahorro": ahorro
        }
        self.detalles.append(detalle)
        self.total += subtotal
        if not hasattr(self, "Ahorro Total"):
            self.ahorrototal = 0
        self.ahorrototal += subtotal

    def resumen(self):
        return (f"Venta No: {self.idventa} | Fecha: {self.fecha} | Cliente: {self.cliente.nombreclien} | Empleado: {self.empleado.nombreempleado} |"
                f"Total: Q.{self.total: .2f} | Ahorro por oferta: Q.{self.ahorrototal: .2f}")

class DetallesVentas:
    def __init__(self, iddetalleventa, idventa, producto, cantidad):
        self.iddetalleventa = iddetalleventa
        self.idventa = idventa
        self.idproducto = producto.idproducto
        self.cantidad = cantidad
        self.precio = producto.precio
        self.Subtotal = self.precio * self.cantidad

    def resumen(self):
        return (f"Detalle No: {self.iddetalleventa} | Venta No: {self.idventa} | Producto: {self.idproducto} | Cantidad: {self.cantidad} |"
                f"Precio: Q.{self.precio: .2f} | Subtotal: Q.{self.Subtotal: .2f}")

class Compras:
    def __init__(self, idcompras, fecha, idproveedor, idempleado):
        self.idcompras = idcompras
        self.fecha = fecha
        self.idproveedo = idproveedor
        self.idempleado = idempleado
        self.detalles = []
        self.total = 0

    def agregarDetallesCompras(self , producto, cantidad, preciounita, fechacaducidad):
        producto.Stock(cantidad, "Compras")
        detallecompras = DetallesCompras(len(self.detalles)+1, self.idcompras, producto.id, cantidad, preciounita, fechacaducidad)
        self.detalles.append(detallecompras)
        self.total += detallecompras.Subtotal

    def resumen(self):
        proveedores = proveedor.get(self.idproveedo)
        empleado = empleados.get(self.idempleado)
        nombprovee = proveedores.nombrepro if proveedor else "Desconocido"
        nombreemple = empleado.nombreemple if empleado else "Desconocido"
        return (f"Compra No: {self.idcompras} | Fecha: {self.fecha} | Proveedorees: {nombprovee} | Empleados: {nombreemple} |"
                f"Total: Q.{self.total:.2f}")

class DetallesCompras:
    def _init_(self, iddetallecompras, idproducto, cantidad, preciocompra, fechacaducidad, idcompras):
        self.iddetallecompras = iddetallecompras
        self.idcompras = idcompras
        self.producto = idproducto
        self.cantidad = cantidad
        self.preciocompra = preciocompra
        self.Subtotal = self.preciocompra * self.cantidad
        self.fechacaducidad = fechacaducidad

    def resumen(self):
        return (f"Detalle No. {self.iddetallecompras} | Compra No: {self.idcompras} | Producto: {self.idproducto} | Cantidad: {self.cantidad} |"
                f"Precio: Q.{self.preciocompra:.2f} | Subtotal: Q.{self.Subtotal: .2f} | Fecha: {self.fechacaducidad} |")

def cargar():
    cargarProductos()
    cargarCategoria()
    cargarProveedores()
    cargarClientes()
    cargarEmpleados()
    cargarVentas()
    cargarCompras()

def AgregarCategoria():
    idcategoria = len(categorias) + 1
    nombrecat = input("Nombre de la categoría: ")
    categorias[idcategoria] = Categorias(idcategoria, nombrecat)
    print("Categoría agregada con éxito.")

def AgregarProductos():
    idproducto = len(productos) + 1
    nombproducto = input("Ingrese el nombre de la producto: ")
    precioprod = float(input("Ingrese el precio de la producto: "))
    print("Categorias disponibles")
    for a in categorias.values():
        print(a.resumen())
    idcategoria = int(input("Ingrese el ID de la categoria: "))
    cate = categorias.get(idcategoria)
    if not cate:
        print("Categoria inexistente")
        return
    productos[idproducto] = Productos(idproducto, nombproducto, precioprod, idcategoria)
    print("Productos agregados correctamente")

def InforCliente():
    nit = input("Ingrese el Nit: ")
    if nit in clientes:
        print("Este nit ya existe")
        return
    nombrecliente = input("Ingrese el nombre de la cliente: ")
    telefono = input("Ingrese el teléfono: ")
    direccion = input("Ingrese la direccion: ")
    correo = input("Ingrese el correo: ")
    clientes[nit] = Clientes(nit, nombrecliente, telefono, direccion, correo)
    print("Clientes agregados correctamente")

def InforEmpleado():
    idempleado = len(empleados) + 1
    nombempleado = input("Ingrese el nombre: ")
    telefonoempleado = input("Ingrese el telefono: ")
    direccionempleado = input("Ingrese la direccion: ")
    correoempleado = input("Ingrese el correo: ")
    empleados[idempleado] = Empleados(idempleado, nombempleado, telefonoempleado, direccionempleado, correoempleado)
    print("Empleados agregados correctamente")

def InforProveedores():
    idproveedor = len(proveedor) + 1
    nombprovee = input("Ingrese el nombre: ")
    empresa = input("Ingrese el empresa: ")
    telefonoprovee = input("Ingrese el telefono: ")
    direccionprovee = input("Ingrese la direccion: ")
    correoprovee = input("Ingrese el correo: ")
    print("Categorias Disponibles")
    for a in categorias.values():
        print(f"Id: {a.idcategoria} - Nombre: {a.nombrecat}")
    idcategoria = int(input("Ingrese el ID de la categoria: "))
    if idcategoria in categorias:
        print("Categoria inexistente")
        return
    proveedor[idproveedor] = Proveedor(idproveedor, nombprovee, empresa, telefonoprovee, direccionprovee, correoprovee, idcategoria)
    print("Proveedores agregados correctamente")

def RegistrarVentas():
    nit = input("Ingrese el Nit: ").strip()
    print("Empleados disponibles")
    for a in empleados.values():
        print(f"Id: {a.idempleado} - Nombre: {a.nombreempleado}")
    idempleado = int(input("Ingrese el ID de la categoria: "))
    fecha = input("Ingrese la fecha: ")
    cliente = clientes.get(nit)
    empleado = empleados.get(idempleado)
    if not cliente or not empleado:
        print("El empleado o cliente no existe")
        return
    venta = Venta(len(ventas) + 1, fecha, cliente, empleado)
    if input("Quiere ingresar una oferta al producto (s/N): ").lower() == "s":
        RegistrarOfertas()
    while True:
        idproducto = int(input("Ingrese el ID de la producto: "))
        producto = productos.get(idproducto)
        if not producto:
            print("El producto no existe")
            continue
        cantidad = int(input("Ingrese la cantidad de ventas: "))
        preciounitario = producto.PrecioP
        descuento = ofertas.get(idproducto, 0)
        preciofin = preciounitario * (1 - descuento / 100)
        print(f"Descuento: {descuento}%")
        print(f"Precio con descuento: Q{preciofin:.2f}")
        try:
            venta.agregarDetalleVentas(producto, cantidad, preciofin, descuento)
            print("Productos agregados con descuento correctamente")
        except ValueError as a:
            print(f"Error al agregar el producto: {a}")
        if input("Desea agregar mas productos (s/N): ").lower() == "s":
            break
    ventas.append(venta)
    print(f"Productos agregados correctamente. Total: Q.{venta.total: .2f}")
    print(f"Ahorro total por ofertas: Q.{venta.ahorrototal: .2f}")

def RegistrarOfertas():
    idproducto = int(input("Ingrese el ID de la producto: "))
    producto = productos.get(idproducto)
    if not producto:
        print("El producto no existe")
        return
    print(f"Productos seleccionados son: {producto.nombreproducto}")
    descuento = float(input("El porcentaje de descuento es (%): "))
    if descuento < 0 or descuento > 100:
        print("El descuento debe de estar entre 0 a 100")
        return
    ofertas[idproducto] = descuento
    print(f"Ofertas registradas: {descuento}% para los productos: '{producto.nombreproducto}' (Id: {idproducto})")

def RegistrarCompras():
    idproveedor = int(input("Ingrese el ID del proveedor: "))
    idempleado = int(input("Ingrese el ID del empleado: "))
    fecha = input("Ingrese la fecha: ")
    provee = proveedor.get(idproveedor)
    empleado = empleados.get(idempleado)
    if not provee or not empleado:
        print("El proveedor o empleado no existe")
        return
    compra = Compras(len(compras) + 1, fecha, idproveedor, idempleado)
    while True:
        idproducto = int(input("Ingrese el ID de la producto: "))
        producto = productos.get(idproducto)
        if not producto:
            print("El producto no existe")
            continue
        cantidad = int(input("Ingrese la cantidad de ventas: "))
        preciounitario = int(input("Ingrese el precio unitario: Q. "))
        fechacaducidad = input("La fecha de caducidad del producto es: ")
        compra.agregarDetallesCompras(producto, cantidad, preciounitario, fechacaducidad)
        print("Productos agregados correctamente")
        if input("Desea agregar productos (s/N): ").lower() == "s":
            break
    compras.append(compra)
    print(f"Compras agregaa correctamente. Total: Q.{compra.total: .2f}")

def MostrarCompras():
    if not compras:
        print("No hay compras")
        return
    for compra in compras:
        provee = proveedor.get(compra.idproveedor)
        emplea = empleados.get(compra.Idempleado)
        nombreproveedor = provee.nombrepro if provee else "Desconocido"
        nombreempleado = emplea.nombreemp if emplea else "Desconocido"
        print(f"\nId Commpras: {compra.idcompras}")
        print(f"Fecha: {compra.fecha}")
        print(f"Proveedor: {nombreproveedor}")
        print(f"Empleado: {nombreempleado}")
        print(f"Total: {compra.total: .2f}")
        print("Detalles: ")
        for det in compra.detalles:
            producto = det.producto
            nombreproducto = producto.nombreproduc if producto else "Desconocido"
            print(f" - Producto: {nombreproducto}")
            print(f" - Cantidad: {det.cantidad}")
            print(f" - Precio Unitario: {det.preciocompra}")
            print(f" - SubTotal: {det.subtotal: .2f}")
            print(f" - Fecha de Vencimiento: {det.fechacaducidad}")

def MostrarVentas():
    if not ventas:
        print("No hay ventas")
        return
    for venta in ventas:
        print(f"Id Ventas: {venta.idventa}")
        print(f"Fecha: {venta.fecha}")
        print(f"Clientes: {venta.cliente.nombreclien}")
        print(f"Empleado: {venta.empleado.nombreempleado}")
        print(f"Total: {venta.total: .2f}")
        print("Detalles: ")
        for det in venta.detalles:
            producto = det["producto"]
            print(f" Producto: {producto.nombreproducto}")
            print(f" Precio Unitario: {det["PrecioUnitario"]:.2f} ")
            print(f" Subtotal: {det["Subtotal"]:.2f}")
            print(f" Descuento aplicado: {det["descuento"]}%")

def ConsultarInven():
    print(f"Productos registrados: {len(productos)}")
    if not productos:
        print("No hay productos")
        return
    for produc in productos.values():
        nombecategoria =categorias[produc.idcategoria].nombrecat if produc.idcategoria in categorias else "Sin Categorias"
        print(f"Producto: {produc.idproducto}")
        print(f"Nombre: {produc.nombreproduc}")
        print(f"Precio Unitario: Q.{produc.precioproduc: .2f}")
        print(f"Stock: {produc.stock}")
        print(f"Categoria: {nombecategoria}")
        print(f"Total Compras: {produc.totalcompras}")
        print(f"Total ventas: {produc.totalventas}")

def GuardarProductos():
    with open("Productos.txt", "w", encoding="utf-8") as archivo:
        for prod in productos.values():
            archivo.write(f"{prod.idproducto} | {prod.nombreproduc} | {prod.precioproduc} | {prod.stock} | {prod.idcategoria} | {prod.totalventas} | {prod.totalcompras}")

def cargarProductos():
    try:
        with open("Productos.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                idproducto, nombre, precio, stock, cate, vent, comp = linea.strip().split(":")
                producto = Productos(int(idproducto), nombre, float(precio), int(cate), int(vent), int(comp))
                producto.stock = int(stock)
                productos[int(idproducto)] = producto
    except FileNotFoundError:
        print("Productos.txt no existe el archivo")

def GuardarCategoria():
    with open("Categorias.txt", "w", encoding="utf-8") as archivo:
        for Cat in categorias.values():
            archivo.write(f"{Cat.idcategoria} , {Cat.nombrecat}\n")

def cargarCategoria():
    try:
        with open("Categorias.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                idcategorias, nombrecategorias = linea.strip().split(",")
                categorias[int(idcategorias)] = Categorias(int(idcategorias), nombrecategorias)
    except FileNotFoundError:
        print("Categorias.txt no existe el archivo")

def GuardarClientes():
    with open("Clientes.txt", "w", encoding="utf-8") as archivo:
        for Clien in clientes.values():
            archivo.write(f"{Clien.nit} | {Clien.nombreclien} | {Clien.telefono} | {Clien.direccion} | {Clien.correo}")

def cargarClientes():
    try:
        with open("Clientes.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                nit, nombreclien, telefonoclien, direccionclien, correoclie = linea.strip().split(",")
                clientes[nit] = Clientes(nit, nombreclien, telefonoclien, direccionclien, correoclie)
    except FileNotFoundError:
        print("Clientes.txt no existe el archivo")

def GuardarEmpleados():
    with open("Empleados.txt", "w", encoding="utf-8") as archivo:
        for Emple in empleados.values():
            archivo.write(f"{Emple.idempleado} | {Emple.nombreempleado} | {Emple.telefonoempleado} | {Emple.direccionempleado} | {Emple.correoempleado}")

def cargarEmpleados():
    try:
        with open("Empleados.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                idempleado, nombreemple, telefonoemple, direccionemple, correoemple = linea.strip().split(",")
                empleados[int(idempleado)] = Empleados(int(idempleado), nombreemple, telefonoemple, direccionemple, correoemple)
    except FileNotFoundError:
        print("Empleados.txt no existe el archivo")

def GuardarVentas():
    with open("Ventas.txt", "w", encoding="utf-8") as archivo:
        for Vent in ventas.values():
            archivo.write(f"{Vent.idventa} | {Vent.fecha} | {Vent.cliente.nit} | {Vent.empleado.idempleado} | {Vent.totalventas} | {Vent.total}")

def cargarVentas():
    try:
        with open("Ventas.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                iddetalleventa, fecha, nit, idempleado, total = linea.strip().split(",")
                cliente = clientes.get(nit)
                emplea = empleados.get(idempleado)
                ven = Venta(int(iddetalleventa), fecha, cliente, emplea)
                ven.Total = float(total)
                ventas.append(ven)
    except FileNotFoundError:
        print("Ventas.txt no existe el archivo")

def GuardarProveedores():
    with open("Proveedores.txt", "w", encoding="utf-8") as archivo:
        for Provee in proveedor.values():
            archivo.write(f"{Provee.idprovee} | {Provee.nombreprovee} | {Provee.empresa} | {Provee.telefonoprovee} | {Provee.direccionprovee} | {Provee.correoprovee}")

def cargarProveedores():
    try:
        with open("Proveedores.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                idproveedor, nombreproveed, empresa, telefonoproveed, direccionprovee, correoprovee, idcategoria = linea.strip().split(",")
                proveedor[int(idproveedor)] = Proveedor(int(idproveedor), nombreproveed, empresa, telefonoproveed, direccionprovee, correoprovee, idcategoria, direccionprovee)
    except FileNotFoundError:
        print("Proveedores.txt no existe el archivo")

def GuardarDetallesVenta():
    with open("DetallesVenta.txt", "w", encoding="utf-8") as archivo:
        for Venta in ventas:
            for detella in Venta.Detalles:
                archivo.write(f"{Venta.idventa} | {detella["Producto"].idproducto} | {detella["Cantidad"]} | {detella["Precio Unitario"]} | {detella["SubTotal"]} | {detella["Descuento"]}\n")

def GuardarCompras():
    with open("Compras.txt", "w", encoding="utf-8") as archivo:
        for compra in compras:
            archivo.write(f"{compra.idcompra} | {compra.fecha} | {compra.proveedor.idprovee} | {compra.totalventas} | {compra.total: .2f}")

def guardardetalleCom():
    with open("DetallesVenta.txt", "w", encoding="utf-8") as archivo:
       for compra in compras:
           for venta in compra.Detalles:
               archivo.write(f"{compra.idcompras} | {venta["Producto"].idproducto} | {venta["Cantidad"]} | {venta["Precio Unitario"]} | {venta["SubTotal"]} | {venta["Descuento"]}")

def cargarCompras():
    try:
        with open("Compras.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                iddetallecompra, fecha, idproveedor,total = linea.strip().split(",")
                provee = proveedor.get(int(idproveedor))
                compra = Compras(int(iddetallecompra), fecha, provee)
                compra.Total = float(total)
                compras.append(compra)
    except FileNotFoundError:
        print("Compras.txt no existe el archivo")

def GuardarTodos():
    GuardarProductos()
    GuardarClientes()
    GuardarCompras()
    GuardarEmpleados()
    GuardarProveedores()
    GuardarCategoria()
    GuardarVentas()

while True:
    print("*******Bienvenido a Menu principal*************")
    print("1. Gerencia")
    print("2. Area de Bodega")
    print("3. Area de Cajas")
    print("4. Salir")

    opcion = input("Seleccione una opcion: ")
    match (opcion):
        case "1":
            while True:
                print("*****Bienvenido a Gerencia******")
                print("1. Agregar Empleado")
                print("2. Consultar Inventario")
                print("3. Mostrar Ventas")
                print("4. Mostrar Compras")
                print("5. Regresar al menu principal")
                opcionGerencia = input("Seleccione una opcion: ")
                if opcionGerencia == "1":
                    InforEmpleado()
                elif opcionGerencia == "2":
                    ConsultarInven()
                elif opcionGerencia == "3":
                    MostrarVentas()
                elif opcionGerencia == "4":
                    MostrarCompras()
                elif opcionGerencia == "5":
                    break
                else:
                    print("Opcion no valida, intente de nuevo")

        case "2":
            while True:
                print("******Bienvenido al area de bodega******")
                print("1. Agregar Categorias")
                print("2. Agregar Productos")
                print("3. Agregar Proveedores")
                print("4. Registrar Compras")
                print("5. Mostrar Compras")
                print("6. Regresar al menu principal")
                opcionBodega = input("Seleccione una opcion: ")
                if opcionBodega == "1":
                    AgregarCategoria()
                elif opcionBodega == "2":
                    AgregarProductos()
                elif opcionBodega == "3":
                    InforProveedores()
                elif opcionBodega == "4":
                    RegistrarCompras()
                elif opcionBodega == "5":
                    MostrarCompras()
                elif opcionBodega == "6":
                    break
                else:
                    print("Opcion no valida, intente de nuevo")

        case "3":
            while True:
                print("******Bienvenido al area de Cajas*******")
                print("1. Agregar Clientes")
                print("2. Registrar Ventas")
                print("3. Consultar Inventario")
                print("4. Mostrar Ventas")
                print("5. Regresar al menu principal")
                opcionCajas = input("Seleccione una opcion: ")
                if opcionCajas == "1":
                    InforCliente()
                elif opcionCajas == "2":
                    RegistrarVentas()
                elif opcionCajas == "3":
                    ConsultarInven()
                elif opcionCajas == "4":
                    MostrarVentas()
                elif opcionCajas == "5":
                    break
                else:
                    print("Opcion no valida, intente de nuevo")

        case "4":
            print("Guardando información...")
            GuardarTodos()
            print("Cerrando el sistema. ¡Hasta pronto!")
            exit()
        case _:
            print("Opcion no valida, intente de nuevo")