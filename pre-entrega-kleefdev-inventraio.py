# Lista de productos ya cargardos en el inventario
productos = [
    {"nombre": "⌨️  Teclado", "cantidad": 30, "precio": 50.0},
    {"nombre": "🖱️  Mouse", "cantidad": 50, "precio": 20.0},
    {"nombre": "💻 Laptop", "cantidad": 20, "precio": 250.0},
    {"nombre": "🎦 Camara-web", "cantidad": 10, "precio": 25},
    {"nombre": "🖨️  Impresora", "cantidad": 15, "precio": 150.50}
]

# Mensaje de bienvenida en varios idiomas
print("""
    ❕Bienvenido a KLEEFDEV! Explora lo mejor en tecnología y diseño para tu negocio.❕       -  ES
    ❕Welcome to KLEEFDEV! Explore the best in technology and design for your business.❕     -  EN  
    ❕Bem-vindo à KLEEFDEV! Explore o melhor em tecnologia e design para o seu negócio.❕    -  PT 
    ❕Bienvenue chez KLEEFDEV ! Découvrez le meilleur de la technologie et du design pour votre entreprise.❕   -  FR
    ❕Byenveni nan KLEEFDEV! Eksplore pi bon nan teknoloji ak konsepsyon pou biznis ou.❕      -  HT
""")

# Bucle para el menú interactivo
while True:
    print("""
    MENU DE INVENTARIO\n
    1.     ➕   AGREGAR PRODUCTOS AL INVENTARIO
    2.     🗒️    MOSTRAR LOS PRODUCTOS EN STOCK
    3.     🗑️    ELIMINAR PRODUCTO
    4.     🔄   ACTUALIZAR CANTIDAD DE PRODUCTO
    5.     💰   CALCULAR VALOR TOTAL DEL INVENTARIO
    0.     👋   SALIR
""")
    opcion = input("Ingrese una opción: ")
    
    if opcion == '1':
        print("Agregando productos...")
        nombre = input("Ingrese el nombre del producto: ")
        nombre_existe = False
        for producto in productos:
            if producto['nombre'].lower() == nombre.lower():
                nombre_existe = True
                print("El producto ya existe. Intente con otro nombre.")
                break
        if not nombre_existe:
            cantidad = int(input("Ingrese la cantidad de unidades: "))
            precio = float(input("Ingrese el precio por unidad: "))
            productos.append({"nombre": nombre, "cantidad": cantidad, "precio": precio})
            print("Producto agregado correctamente.")

    elif opcion == '2':
        print("\n--- PRODUCTOS EN STOCK ---")
        if productos:
            for i, producto in enumerate(productos, start=1):
                print(f"{i}. Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']:.2f}")
        else:
            print("No hay productos en el inventario.")

    elif opcion == '3':
        print("Borrando productos en Stock...")
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        encontrado = False
        for producto in productos:
            if producto['nombre'].lower() == nombre.lower():
                productos.remove(producto)
                encontrado = True
                print(f"Producto '{nombre}' eliminado del inventario❌.")
                break
        if not encontrado:
            print("Producto no encontrado⛔.")

    elif opcion == '4':
        print("Actualizando cantidad de producto en Stock")
        nombre = input("Ingrese el nombre del producto a actualizar: ")
        encontrado = False
        for producto in productos:
            if producto['nombre'].lower() == nombre.lower():
                nuevo_cantidad = int(input("Ingrese la nueva cantidad: "))
                producto['cantidad'] = nuevo_cantidad
                encontrado = True
                print(f"Cantidad de '{nombre}' actualizada a {nuevo_cantidad}.")
                break
        if not encontrado:
            print("Producto no encontrado⛔.")

    elif opcion == '5':
        valor_total = sum(producto['cantidad'] * producto['precio'] for producto in productos)
        print(f"\nValor total del inventario: ${valor_total:.2f}")

    elif opcion == '0':
        print("Gracias por su visita🙏. Vuelve pronto")
        break

    else:
        print("Opción inválida🚫. Por favor, intente de nuevo.")
