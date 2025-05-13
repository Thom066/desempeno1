#creating a dictionary which we define as an inventory 
inventory = {
    'leche' : {'precio' : 3500, 'cantidad' : 20},
    'queso' : {'precio' : 4000, 'cantidad' : 13},
    'arroz' : {'precio' : 4800, 'cantidad' : 30},
    'lentejas' : {'precio' : 3950, 'cantidad' : 25},
    'mantequilla' : {'precio' : 5500, 'cantidad' : 18}
}

#function for add products in inventory
#finish
def addProducts():
    print("Vas a agregar productos en el inventario")

    while True:

        nameProduct = input("Ingrese el nombre del producto: ").lower()
        
        if nameProduct in inventory:
            print("Este producto ya esta en el inventario.")
        else:
            print("Ahora: ")
            break

    try:
            priceProduct = int(input("Ingrese el precio del producto (en pesos, sin punto decimal): "))
            if priceProduct <= 0:
                print(" El precio debe ser un número positivo.")
                return

            cantityProduct = int(input("Ingrese la cantidad disponible: "))
            if cantityProduct < 0:
                print(" La cantidad no puede ser negativa.")
                return
            
    except ValueError:
        print("Invalido, ingrese solo números válidos para los precios y cantidades.")
    


    inventory[nameProduct]={ 
        "precio" : priceProduct,
        "cantidad" : cantityProduct
       
    }
    
    print("Producto agregado")

#function for search products in inventory
#finish
def searchProducts():
    print("Busqueda de productos")
    global inventory
    while True:
        searchProductName = input ("Digite el nombre del producto: ").lower()

        if searchProductName in inventory:
            product = inventory[searchProductName]
            print(f"Producto: {searchProductName}\n Precio: {product['precio']}\n Cantidad: {product['cantidad']}")
            break
        else :
            print("No existe en el inventario")

#function for modify products in inventory
#finish
def modifyProducts():
    
    print("Entraste a actualizar productos")
    print("¿Qué desea actualizar?\n1) Precio\n2) Cantidad")
    
    optionModify = input("Digite la opción: ")

    if optionModify == "1":
        productName = input("Digite el nombre del producto que desea actualizar: ").lower()
        
        if productName in inventory:
            print(f"Producto encontrado: {productName}")
            try:
                newPrice = int(input("Digite el nuevo precio sin puntos ni decimales: "))
                if newPrice > 0:
                    inventory[productName]['precio'] = newPrice
                    print("Precio actualizado .")
                else:
                    print("El precio debe ser mayor a cero por favor.")
            except ValueError:
                print("inválido, digite solo números enteros sin puntos.")
        else:
            print("Este producto no se encuentra en el inventario.")

    elif optionModify == "2":
        productName = input("Digite el nombre del producto que desea actualizar: ").lower()
        
        if productName in inventory:
            print(f"Producto encontrado: {productName}")
            try:
                newCantidad = int(input("Digite la nueva cantidad: "))
                if newCantidad >= 0:
                    inventory[productName]['cantidad'] = newCantidad
                    print(" Cantidad actualizada.")
                else:
                    print(" La cantidad no puede ser menor a 0.")
            except ValueError:
                print("invalida, digite solo numeros enteros.")
        else:
            print("Este producto no se encuentra en el inventario.")
    else:
        print(" Opción inválida.")

#function for delete products in inventory
#finish
def deleteProducts():
    print("Eliminar producto")

    while True:
        productDelete = input("Digite el nombre del producto que desea eliminar: ").lower()
        
        if productDelete not in inventory:
            print("No esta en el sistema")
        else :
            print("Seguro que quieres eliminarlo?")
            print("1)Si 2)No")

            optionDelete = input("Ingrese una opcion: ")

            if optionDelete == "1":
                print("Producto ELIMINADO")
                inventory.pop(productDelete)
                break
            else :
                print("saliendo de eliminar")
                break

#function for calculate total in inventory
#finish
def calculateProducts():
    print("Calcular el valor total del inventario")
    total = 0
    for dates in inventory.values():
        total += dates['precio'] * dates['cantidad']
    print(f" Valor total del inventario: ${total:,.2f}\n")

#this is menu in a cicle while for runing functions
while True:
    print("---"*10,"\n",inventory)
    print("---"*10,"\nBienvenido al inventario\n","1)Añadir productos al inventario\n","2)Consultar productos en inventario\n","3)Actualizar precios de productos\n","4)Eliminar productos del inventario\n","5)Calcular el valor total del inventario\n","6)Salir\n","---"*10)
    optionUser = input("Digite una Opcion: ")

    if optionUser == "1":
        addProducts()
    elif optionUser == "2":
        searchProducts()
    elif optionUser == "3":
        modifyProducts()
    elif optionUser == "4":
        deleteProducts()
    elif optionUser == "5":
        calculateProducts()
    elif optionUser == "6":
        break
    else:
        print("Opcion INVALIDA")