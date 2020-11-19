from app import *


#Se hace primero el insert de los datos de productos

#Producto numero 1
prod = Producto(nombre = "Camisa blanca de Carolina Herrera", url_img = "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=80", 
precio = 108, descrip = "Camisa base que puede servirte para todo tipo de ocasiones" , stock = 23, descuento = 13, 
inventario = 50, tipo = 'H', rojo = True , azul = False, 
verde = True , negro = False, blanco = False, 
Talla_S = True, Talla_M = True, Talla_L = True, Talla_XL = False)
db.session.add(prod)
db.session.commit()

#Producto numero 2
prod = Producto(nombre = "Buso de temporada de Calvin Klein", url_img = "https://images.unsplash.com/photo-1517865288-978fcb780652?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=401&q=80",
precio = 97, descrip = "Buso de manga larga, ideal para combinar con gorros de neive de calvin klein", stock = 44, descuento = 3,
inventario = 44, tipo = 'M', rojo = False , azul = True,
verde = True , negro = False, blanco = False,
Talla_S = True, Talla_M = False, Talla_L = False, Talla_XL = False)
db.session.add(prod)
db.session.commit()


#Producto numero 3
prod = Producto(nombre = "Chaqueta estilo pantalón", url_img = "https://images.unsplash.com/flagged/photo-1576190645751-87b320784350?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=80",
        precio = 138, descrip = "Chaqueta impermeable, con bolsillos, para llevar en lugares frios o combinar con tu ropa preferida", stock = 48, descuento = 97,        
        inventario = 48, tipo = 'U', rojo = True , azul = False,
        verde = False , negro = False, blanco = False,
        Talla_S = False, Talla_M = True, Talla_L = True, Talla_XL = True)
db.session.add(prod)
db.session.commit()


#Producto numero 4
prod = Producto(nombre = "Abrigo de invierno de Bershka", url_img = "https://images.unsplash.com/photo-1585439623131-6a91ce98e4c0?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80",
        precio = 32, descrip = "Abrigo de invierno con manga larga, perfecto para un regalo o las temporadas frias ", stock = 47, descuento = 1,
        inventario = 50, tipo = 'H', rojo = True , azul = True,
        verde = True , negro = False, blanco = False,
        Talla_S = False, Talla_M = True, Talla_L = False, Talla_XL = True)
db.session.add(prod)
db.session.commit()


#Producto numero 5
prod = Producto(nombre = "Chaqueta felpuda", url_img = "https://images.unsplash.com/photo-1597612041798-2f87cb7b5572?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=80",
        precio = 58, descrip = "Linda chaqueta felpuda hecha de poliester para ocasiones sque hagan frío", stock = 10, descuento = 97,
        inventario = 34, tipo = 'M', rojo = False , azul = False,
        verde = False , negro = True, blanco = True,
        Talla_S = True, Talla_M = True, Talla_L = True, Talla_XL = False)
db.session.add(prod)
db.session.commit()

#Producto numero 6

prod = Producto(nombre = "Chaqueta de cuero de España", url_img = "https://images.unsplash.com/photo-1519167130418-c3640bd21b7e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=80",
        precio = 138, descrip = "Bonita y comoda chaqueta de cuero. Hecha 100% de cuero de las mejores vacas y toros", stock = 20, descuento = 98,
        inventario = 26, tipo = 'U', rojo = True , azul = False,
        verde = True , negro = False, blanco = True,
        Talla_S = True, Talla_M = True, Talla_L = False, Talla_XL = False)
db.session.add(prod)
db.session.commit()

#Producto numero 7
prod = Producto(nombre = "Vestido de trenzas ", url_img = "https://images.unsplash.com/photo-1594633313593-bab3825d0caf?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80",
        precio = 199, descrip = "Vestido con hilos traidos desde la india. Para tus ocasiones más elegantes y severas para una buena fiesta y reunión", stock = 31, descuento = 31,
        inventario = 31, tipo = 'H', rojo = True , azul = False,
        verde = True , negro = True, blanco = True,
        Talla_S = True, Talla_M = True, Talla_L = False, Talla_XL = True)
db.session.add(prod)
db.session.commit()


#Producto numero 8
prod = Producto(nombre = "Camisa manga larga con botones negros", url_img = "https://images.unsplash.com/photo-1583846782968-4ebf5c76cc02?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=375&q=80",
        precio = 75, descrip = "Camiseta manga larga con posibilidad de poner corbata, para poder tener reuniones semi formales al mejor estilo!", stock = 8, descuento = 65,
        inventario = 43, tipo = 'M', rojo = False , azul = False,
        verde = True , negro = True, blanco = False,
        Talla_S = False, Talla_M = True, Talla_L = False, Talla_XL = False)
db.session.add(prod)
db.session.commit()

#Producto numero 9
prod = Producto(nombre = "Vestido de playa con adornos de flores", url_img = "https://images.unsplash.com/photo-1587366801951-0dcd4ae429f9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80",
        precio = 87, descrip = "Vestido largo con pecho destapado,perfecto para los lugares en los que hace calor y para tener un dia fresco", stock = 20, descuento = 43,
        inventario = 49, tipo = 'M', rojo = True , azul = False,
        verde = True , negro = True, blanco = True,
        Talla_S = False, Talla_M = False, Talla_L = False, Talla_XL = True)
db.session.add(prod)
db.session.commit()


#Producto numero 10
prod = Producto(nombre = "Camisa de SPARTANS 1.0", url_img = "https://images.unsplash.com/photo-1516258454449-64fed1caa732?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=751&q=80",
        precio = 117, descrip = "Camisa diseñada con el logotipo de SPARTANS para poder realizar el deporte a gusto.", stock = 29, descuento = 65,
        inventario = 40, tipo = 'M', rojo = True , azul = True,
        verde = True , negro = False, blanco = False,
        Talla_S = True, Talla_M = True, Talla_L = True, Talla_XL = True)
db.session.add(prod)
db.session.commit()

#Producto numero 11
prod = Producto(nombre = "Top corto de Carolina Herrera", url_img = "https://images.unsplash.com/photo-1603217192766-e9db2d08a0fc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=375&q=80",
        precio = 184, descrip = "Top para las salidas casuales, perfecto para sentir frescura en el cuerpo", stock = 44, descuento = 87,
        inventario = 48, tipo = 'U', rojo = False , azul = True,
        verde = True , negro = False, blanco = False,
        Talla_S = False, Talla_M = True, Talla_L = True, Talla_XL = False)
db.session.add(prod)
db.session.commit()

#Producto numero 12
prod = Producto(nombre = "Vestido de baño primevare passion", url_img = "https://images.unsplash.com/photo-1597348469103-ddd8e854e4d3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=333&q=80",
        precio = 24, descrip = "Vestido de baño ajustado y comodo para sentirte como si estuvieras en primavera", stock = 34, descuento = 77,
        inventario = 43, tipo = 'M', rojo = False , azul = False,
        verde = False , negro = True, blanco = True,
        Talla_S = True, Talla_M = True, Talla_L = False, Talla_XL = False)
db.session.add(prod)
db.session.commit()

#Producto numero 13
prod = Producto(nombre = "Shorts cortos con tela de Egipto", url_img = "https://images.unsplash.com/photo-1584370848036-d63286d83fa4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80",
        precio = 193, descrip = "Shorts cortos, perfecto para relajarse y poder dejar las piernas al aire libre.", stock = 25, descuento = 47,
        inventario = 46, tipo = 'U', rojo = True , azul = True,
        verde = False , negro = True, blanco = False,
        Talla_S = True, Talla_M = True, Talla_L = False, Talla_XL = True)
db.session.add(prod)
db.session.commit()

#Producto numero 14
prod = Producto(nombre = "Pantalones de rayas primavera", url_img = "https://images.unsplash.com/photo-1551048632-24e444b48a3e?ixlib=rb-1.2.1&auto=format&fit=crop&w=334&q=80",
        precio = 157, descrip = "Pantalones de rayas perfecto para ocasiones frescas y temporadas de calor para poder lucir con lo mejor.", stock = 14, descuento = 20,  
        inventario = 16, tipo = 'U', rojo = True , azul = True,
        verde = True , negro = False, blanco = False,
        Talla_S = True, Talla_M = True, Talla_L = False, Talla_XL = False)
db.session.add(prod)
db.session.commit()

#Producto numero 15
prod = Producto(nombre = "Camisa de mano de esqueleto", url_img = "https://images.unsplash.com/photo-1503342296413-28a6ec3768b5?ixlib=rb-1.2.1&auto=format&fit=crop&w=334&q=80",
        precio = 33, descrip = "Perfecta camisa de un color exquisito para ir a la ultima moda sobre las tendencias de musica.", stock = 12, descuento = 57,
        inventario = 26, tipo = 'M', rojo = True , azul = True,
        verde = False , negro = True, blanco = False,
        Talla_S = False, Talla_M = True, Talla_L = True, Talla_XL = False)
db.session.add(prod)
db.session.commit()

#Producto numero 16
prod = Producto(nombre = "Jean classic version slim-fit", url_img = "https://images.unsplash.com/photo-1584370848010-d7fe6bc767ec?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80",
        precio = 97, descrip = "Jean pantalon clasico para todo tipo de ocasion y clima no debe faltar en ningun armario", stock = 22, descuento = 83,
        inventario = 43, tipo = 'U', rojo = True , azul = True,
        verde = True , negro = False, blanco = True,
        Talla_S = True, Talla_M = True, Talla_L = True, Talla_XL = True)
db.session.add(prod)
db.session.commit()


#Producto numero 17
prod = Producto(nombre = "Chaqueta negra de Cristian Dior", url_img = "https://images.unsplash.com/photo-1601582067612-7a347874f27d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80",
        precio = 140, descrip = "Para lucir las mejoras prendas en invierno y para no pasar frio, esta es la mejor selección de la temporada.", stock = 12, descuento = 16,
        inventario = 19, tipo = 'U', rojo = True , azul = True,
        verde = True , negro = False, blanco = True,
        Talla_S = False, Talla_M = True, Talla_L = False, Talla_XL = True)
db.session.add(prod)
db.session.commit()


#Producto numero 18
prod = Producto(nombre = "Abrigo ligero con estampado de flores", url_img = "https://images.unsplash.com/photo-1557433841-e964bdf8c263?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=332&q=80",
        precio = 119, descrip = "Fresco y ligero, perfecto para combinar con todo tipo de colores bases  y perfecto para el invierno", stock = 28, descuento = 58,       
        inventario = 38, tipo = 'H', rojo = True , azul = True,
        verde = False , negro = False, blanco = True,
        Talla_S = True, Talla_M = True, Talla_L = True, Talla_XL = True)
db.session.add(prod)
db.session.commit()

#Producto numero 19
prod = Producto(nombre = "Chaqueta de bolsillos con estampado multiple", url_img = "https://images.unsplash.com/photo-1576555361498-efcdde9b8897?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=667&q=80",
        precio = 34, descrip = "La mejor elección para lucir fachero a la hora que sea necesario y siempre verse fresco", stock = 40, descuento = 61,
        inventario = 48, tipo = 'M', rojo = False , azul = True,
        verde = True , negro = True, blanco = True,
        Talla_S = True, Talla_M = False, Talla_L = True, Talla_XL = True)
db.session.add(prod)
db.session.commit()

#Producto numero 20
prod = Producto(nombre = "Chaqueta de cierre con cremallera", url_img = "https://images.unsplash.com/photo-1536995769641-12e9f98fd223?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80",
        precio = 74, descrip = "Chaqueta perfecta para el frio y para las ocasiones con los buenos amigos.", stock = 5, descuento = 78,
        inventario = 38, tipo = 'U', rojo = False , azul = False,
        verde = True , negro = False, blanco = False,
        Talla_S = True, Talla_M = True, Talla_L = True, Talla_XL = True)
db.session.add(prod)
db.session.commit()