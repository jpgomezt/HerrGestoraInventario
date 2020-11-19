from app import *
import random

#Insertar los productos a la plataforma 
num = 0
x = "No estoy vacio"
while x != "":

    titulo = str(input("Dime un nombre :) \n>"))
    descrip = str(input("Dame una descripcion :) \n>"))
    link = str(input("Inserte por favor un link :) \n>"))
    stock = random.randint(1,50)
    inventario = 0
    while inventario < stock:
        inventario = random.randint(1,50)
    tipo = ['H', 'M', 'U']

    rojo = random.choice([True, False])
    azul = random.choice([True, False])
    verde = random.choice([True, False])
    blanco = random.choice([True, False])
    negro = random.choice([True, False])
    while not (rojo or azul or verde or blanco or negro):
        rojo = random.choice([True, False])
        azul = random.choice([True, False])
        verde = random.choice([True, False])
        blanco = random.choice([True, False])
        negro = random.choice([True, False])
        

    S = random.choice([True, False])
    M = random.choice([True, False])
    L = random.choice([True, False])
    xl = random.choice([True, False])
    while not (S or M or L or xl):
        S = random.choice([True, False])
        M = random.choice([True, False])
        L = random.choice([True, False])
        xl = random.choice([True, False])

    print(f'''
        prod = Producto(nombre = "{titulo}", url_img = "{link}", 
        precio = {random.randint(1,200)}, descrip = "{descrip}", stock = {stock}, descuento = {random.randint(0, 99)}, 
        inventario = {inventario}, tipo = '{random.choice(tipo)}', rojo = {rojo} , azul = {azul}, 
        verde = {verde} , negro = {negro}, blanco = {blanco}, 
        Talla_S = {S}, Talla_M = {M}, Talla_L = {L}, Talla_XL = {xl})
        db.session.add(prod)
        db.session.commit()
    ''')
    prod = Producto(nombre = titulo, url_img = link, 
    precio = random.randint(1,200), descrip = descrip, stock = stock, descuento = random.randint(0, 99), 
    inventario = inventario, tipo = random.choice(tipo), rojo = rojo , azul = azul, 
    verde = verde , negro = negro, blanco = blanco, 
    Talla_S = S, Talla_M = M, Talla_L = L, Talla_XL = xl)
    db.session.add(prod)
    db.session.commit()
    num = num + 1
    print("Este es el ",num," de productos creados")
    x = input("Si no desea continuar deje esto vacio: ")
