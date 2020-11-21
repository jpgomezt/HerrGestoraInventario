from app import *


# Se hace primero el insert de los datos de productos

# Producto numero 1
prod = Producto(nombre="Camiseta Wonder Woman", url_img="https://i.pinimg.com/originals/5c/bf/b7/5cbfb75106b0c2501f663cdd57cd2eaa.jpg",
                precio=65690, descrip="Camisa de la coleccion DC de Wonder Woman", stock=45, descuento=77,
                inventario=47, tipo='M', rojo=True, azul=False,
                verde=False, negro=True, blanco=True,
                Talla_S=False, Talla_M=False, Talla_L=False, Talla_XL=True)
db.session.add(prod)
db.session.commit()

# Producto numero 2
prod = Producto(nombre="Camiseta Ballena", url_img="https://www.fundacionmalpelo.org/wp-content/uploads/2019/02/camisetas-mujer-PRECOLOMBINO-07-04.jpg",
                precio=133, descrip="Camiseta con diseñooo precolombino de un ballena", stock=23, descuento=60,
                inventario=48, tipo='M', rojo=False, azul=True,
                verde=False, negro=True, blanco=False,
                Talla_S=True, Talla_M=True, Talla_L=True, Talla_XL=True)
db.session.add(prod)
db.session.commit()


# Producto numero 3
prod = Producto(nombre="Camiseta I FIND", url_img="https://ae01.alicdn.com/kf/HTB1woUvaYus3KVjSZKbq6xqkFXaR/Mujer-de-moda-de-se-ora-s-lido-ltimo-Cruz-vendaje-Sexy-Tops-camiseta-coreana-ropa.jpg_q50.jpg",
                precio=40, descrip="Camiset con cruz I DO NOT SEEK, I FIND.", stock=35, descuento=98,
                inventario=39, tipo='M', rojo=True, azul=True,
                verde=False, negro=True, blanco=True,
                Talla_S=False, Talla_M=True, Talla_L=True, Talla_XL=True)
db.session.add(prod)
db.session.commit()


# Producto numero 4
prod = Producto(nombre="Tenis Asics", url_img="https://www.irrenlauf.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/t/e/tennis_mujer_puma-826bnz.jpg",
                precio=66404, descrip="Tenis de cordon grueso", stock=19, descuento=42,
                inventario=38, tipo='M', rojo=False, azul=True,
                verde=True, negro=True, blanco=False,
                Talla_S=True, Talla_M=False, Talla_L=True, Talla_XL=True)
db.session.add(prod)
db.session.commit()


# Producto numero 5
prod = Producto(nombre="Buzo de Interior", url_img="https://tottocr.vteximg.com.br/arquivos/ids/190022-1000-1000/Totto-BUZO-PARA-MUJER-COLOR-NEGRO-TIPO-SUDADERA-CRUZIA_1.jpg?v=637262005522700000",
                precio=98853, descrip="Buzo con cierre para interiores", stock=19, descuento=4,
                inventario=28, tipo='M', rojo=False, azul=True,
                verde=False, negro=True, blanco=True,
                Talla_S=False, Talla_M=False, Talla_L=False, Talla_XL=True)
db.session.add(prod)
db.session.commit()

# Producto numero 6
prod = Producto(nombre="Pantalon Dril", url_img="https://qafacol.vteximg.com.br/arquivos/ids/204385-770-700/40070145-10_1.jpg?v=636650172818500000",
                precio=56876, descrip="Pantalon en dril 5 bolsillos ", stock=11, descuento=32,
                inventario=35, tipo='M', rojo=False, azul=False,
                verde=False, negro=True, blanco=True,
                Talla_S=True, Talla_M=True, Talla_L=False, Talla_XL=True)
db.session.add(prod)
db.session.commit()

# Producto numero 7
prod = Producto(nombre="Camistea Deportiva Neon", url_img="https://qafacol.vteximg.com.br/arquivos/ids/238754-770-700/40090586-9734_1.jpg?v=636768683364600000",
                precio=51972, descrip="Camistea para deportes con cuello V", stock=22, descuento=63,
                inventario=34, tipo='M', rojo=True, azul=False,
                verde=False, negro=False, blanco=False,
                Talla_S=True, Talla_M=False, Talla_L=True, Talla_XL=True)
db.session.add(prod)
db.session.commit()


# Producto numero 8
prod = Producto(nombre="Camisa de Batman", url_img="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimg.elo7.com.br%2Fproduct%2Fzoom%2F8B4C3F%2Fcamiseta-batman-preta-camiseta-personalizada-batman.jpg&f=1&nofb=1",
                precio=44253, descrip="Camisa de la coleccion DC de Batman", stock=46, descuento=7,
                inventario=46, tipo='H', rojo=True, azul=False,
                verde=True, negro=True, blanco=True,
                Talla_S=True, Talla_M=True, Talla_L=False, Talla_XL=False)
db.session.add(prod)
db.session.commit()


# Producto numero 9
prod = Producto(nombre="Pantalon Rasguñado", url_img="https://sc01.alicdn.com/kf/H28b76d7716ce42c1a85e31ca9c4a5e3cP.jpg_350x350.jpg",
                precio=34493, descrip="Pantalon Denim rasguñado", stock=1, descuento=6,
                inventario=29, tipo='H', rojo=False, azul=True,
                verde=False, negro=True, blanco=False,
                Talla_S=False, Talla_M=True, Talla_L=False, Talla_XL=True)
db.session.add(prod)
db.session.commit()


# Producto numero 10
prod = Producto(nombre="Camiseta Deportiva Manga Corta", url_img="https://qafacol.vteximg.com.br/arquivos/ids/172828-770-700/60090053-3588_1.jpg?v=636612851597470000",
                precio=33730, descrip="Camiseta unicolor con cuello V", stock=22, descuento=74,
                inventario=23, tipo='H', rojo=True, azul=False,
                verde=False, negro=False, blanco=True,
                Talla_S=True, Talla_M=False, Talla_L=False, Talla_XL=False)
db.session.add(prod)
db.session.commit()

# Producto numero 11
prod = Producto(nombre="Buzo California", url_img="https://qafacol.vteximg.com.br/arquivos/ids/348913-770-700/60060104-4227_1.jpg?v=637298415468670000",
                precio=84182, descrip="Buzo de Hombre cuello redondo", stock=29, descuento=0,
                inventario=35, tipo='H', rojo=True, azul=False,
                verde=False, negro=True, blanco=True,
                Talla_S=True, Talla_M=False, Talla_L=True, Talla_XL=False)
db.session.add(prod)
db.session.commit()

# Producto numero 12
prod = Producto(nombre="Tenis Tellenzi", url_img="https://dafitistaticco-a.akamaihd.net/p/tellenzi-4063-4454021-1-product.jpg",
                precio=72737, descrip="Tenis de altura taco ", stock=2, descuento=69,
                inventario=31, tipo='H', rojo=False, azul=True,
                verde=False, negro=True, blanco=False,
                Talla_S=False, Talla_M=False, Talla_L=False, Talla_XL=True)
db.session.add(prod)
db.session.commit()

# Producto numero 13
prod = Producto(nombre="Camiseta Botella", url_img="https://www.bazzarbog.com/11104-large_default/camiseta-hombre.jpg",
                precio=62245, descrip="Camiseta con dibujo de una playa dentro de una botella", stock=5, descuento=69,
                inventario=48, tipo='H', rojo=True, azul=False,
                verde=True, negro=True, blanco=False,
                Talla_S=True, Talla_M=True, Talla_L=False, Talla_XL=False)
db.session.add(prod)
db.session.commit()

# Producto numero 14
prod = Producto(nombre="Camiseta Fish Bone", url_img="https://www.pedrobraun.com/1505-large_default/camiseta-hombre-diseno.jpg",
                precio=86600, descrip="Camiseta en algodon con dibujo", stock=10, descuento=56,
                inventario=48, tipo='H', rojo=False, azul=True,
                verde=False, negro=True, blanco=True,
                Talla_S=True, Talla_M=True, Talla_L=True, Talla_XL=True)
db.session.add(prod)
db.session.commit()

# Producto numero 15
prod = Producto(nombre="Camiseta Stop COVID", url_img="https://www.riojafactory.com/wp-content/uploads/2020/03/mockup-65fb235e.jpg",
                precio=54894, descrip="Camiseta con diseño solidario", stock=6, descuento=55,
                inventario=6, tipo='U', rojo=False, azul=True,
                verde=False, negro=True, blanco=True,
                Talla_S=False, Talla_M=False, Talla_L=False, Talla_XL=True)
db.session.add(prod)
db.session.commit()

# Producto numero 16
prod = Producto(nombre="Tenis Stripes", url_img="https://falabella.scene7.com/is/image/FalabellaCO/4922542_2?wid=800&hei=800&qlt=70",
                precio=69479, descrip="Tenis Moda VI Court Stripes", stock=33, descuento=99,
                inventario=37, tipo='U', rojo=True, azul=True,
                verde=True, negro=False, blanco=True,
                Talla_S=True, Talla_M=True, Talla_L=False, Talla_XL=True)
db.session.add(prod)
db.session.commit()


# Producto numero 17
prod = Producto(nombre="Chaqueta Hunter Mountain", url_img="https://thermos.vteximg.com.br/arquivos/ids/161444-768-768/IMG_1283.jpg?v=637104698322130000",
                precio=44812, descrip="Chaqueta imperbeable y liviana", stock=19, descuento=22,
                inventario=50, tipo='U', rojo=True, azul=False,
                verde=True, negro=False, blanco=True,
                Talla_S=True, Talla_M=True, Talla_L=False, Talla_XL=True)
db.session.add(prod)
db.session.commit()

# Producto numero 18
prod = Producto(nombre="Camiseta J Balvin", url_img="https://http2.mlstatic.com/camiseta-unisex-j-balvin-D_NQ_NP_972574-MCO43151316974_082020-F.jpg",
                precio=45581, descrip="Cmiseta con tuit de J Balvin", stock=26, descuento=32,
                inventario=29, tipo='U', rojo=True, azul=True,
                verde=False, negro=False, blanco=True,
                Talla_S=False, Talla_M=True, Talla_L=True, Talla_XL=False)
db.session.add(prod)
db.session.commit()

# Producto numero 19
prod = Producto(nombre="Pantalon RainLock", url_img="https://ruta40.com.co/wp-content/uploads/2019/09/PANTALÓN-UNISEX-RAINLOCK.jpg",
                precio=86640, descrip="Pantalon comodo para lluvia", stock=21, descuento=4,
                inventario=24, tipo='U', rojo=False, azul=True,
                verde=True, negro=True, blanco=False,
                Talla_S=False, Talla_M=True, Talla_L=True, Talla_XL=False)
db.session.add(prod)
db.session.commit()

# Producto numero 20
prod = Producto(nombre="Gorro Invierno", url_img="https://lasenoritapepis.com/1025/gorro-unisex-polar-manzaneda.jpg",
                precio=91183, descrip="Gorro trenzado para invierno", stock=15, descuento=86,
                inventario=39, tipo='U', rojo=False, azul=True,
                verde=True, negro=False, blanco=True,
                Talla_S=False, Talla_M=True, Talla_L=False, Talla_XL=False)
db.session.add(prod)
db.session.commit()

# Producto numero 21
prod = Producto(nombre="Camiseta Seleccion Colombia", url_img="https://cdn2.totalcode.net/sportlife/product-zoom/es/camiseta-adidas--fcf-polo-hombre-1.jpg",
                precio=49779, descrip="Camiseta Polo Seleccion Colombia", stock=5, descuento=73,
                inventario=9, tipo='H', rojo=False, azul=True,
                verde=True, negro=False, blanco=True,
                Talla_S=True, Talla_M=True, Talla_L=True, Talla_XL=False)
db.session.add(prod)
db.session.commit()

# Producto numero 22
prod = Producto(nombre="Pantalon Deportivo", url_img="https://falabella.scene7.com/is/image/FalabellaCO/4980994_1?q=i?wid=800&hei=800&qlt=70",
                precio=71490, descrip="Pantalon comodo para deportes", stock=12, descuento=7,
                inventario=28, tipo='H', rojo=False, azul=False,
                verde=False, negro=False, blanco=True,
                Talla_S=True, Talla_M=True, Talla_L=False, Talla_XL=True)
db.session.add(prod)
db.session.commit()

# Producto numero 23
prod = Producto(nombre="Chaqueta Slim Fit", url_img="https://dafitistaticco-a.akamaihd.net/p/frenezi-2634-562819-1-product.jpg",
                precio=34869, descrip="Chaqueta casual con cremallera", stock=16, descuento=98,
                inventario=44, tipo='H', rojo=True, azul=False,
                verde=False, negro=True, blanco=True,
                Talla_S=False, Talla_M=True, Talla_L=True, Talla_XL=True)
db.session.add(prod)
db.session.commit()

# Producto numero 24
prod = Producto(nombre="Tenis All Star", url_img="https://http2.mlstatic.com/D_NQ_NP_817091-MCO31129941365_062019-W.jpg",
                precio=66313, descrip="Tenis suela blanca All Star", stock=4, descuento=8,
                inventario=11, tipo='H', rojo=True, azul=False,
                verde=False, negro=True, blanco=True,
                Talla_S=False, Talla_M=False, Talla_L=True, Talla_XL=False)
db.session.add(prod)
db.session.commit()

# Producto numero 25
prod = Producto(nombre="Camiseta Flash", url_img="https://www.camisetas.fun/wp-content/uploads/2018/10/flash-sheldon-cooper-men-s-t-shirt-red-front.png",
                precio=32635, descrip="Camisa de la coleccion DC de Flash", stock=37, descuento=71,
                inventario=43, tipo='H', rojo=True, azul=False,
                verde=False, negro=True, blanco=False,
                Talla_S=False, Talla_M=False, Talla_L=True, Talla_XL=False)
db.session.add(prod)
db.session.commit()

# Producto numero 26
prod = Producto(nombre="Camiseta Catwomen", url_img="https://www.merchandisingplaza.es/261039/2/Camisetas-Catwoman-Camiseta-Catwoman-261039-l.jpg",
                precio=94425, descrip="Camisa de la coleccion DC de Catwomen", stock=39, descuento=21,
                inventario=39, tipo='M', rojo=True, azul=False,
                verde=False, negro=True, blanco=True,
                Talla_S=True, Talla_M=True, Talla_L=True, Talla_XL=True)
db.session.add(prod)
db.session.commit()

# Producto numero 27
prod = Producto(nombre="Gorro Pompon", url_img="https://thermos.vteximg.com.br/arquivos/ids/162338-1000-1000/GORRO-POMPON-PLUSH-MUJER-2020-THM-AZUL.jpg?v=637197162831370000",
                precio=89977, descrip="Gorro para frio con pompon", stock=25, descuento=54,
                inventario=40, tipo='M', rojo=True, azul=True,
                verde=False, negro=True, blanco=True,
                Talla_S=True, Talla_M=False, Talla_L=False, Talla_XL=True)
db.session.add(prod)
db.session.commit()

# Producto numero 28
prod = Producto(nombre="Tenis Coca-Cola", url_img="https://cdn1.coppel.com/images/catalog/pr/8161302-1.jpg",
                precio=70861, descrip="Tenis clasicos de la marca Coca-Cola", stock=29, descuento=1,
                inventario=35, tipo='M', rojo=True, azul=True,
                verde=False, negro=True, blanco=False,
                Talla_S=True, Talla_M=False, Talla_L=False, Talla_XL=False)
db.session.add(prod)
db.session.commit()

# Producto numero 29
prod = Producto(nombre="Jean Cintura Alta", url_img="https://www.dhresource.com/0x0/f2/albu/g9/M00/5F/E9/rBVaWFwrcCaADgfBAADsCY44dls388.jpg",
                precio=83251, descrip="Jean desgastado con cintura alta", stock=6, descuento=10,
                inventario=27, tipo='M', rojo=True, azul=True,
                verde=True, negro=True, blanco=False,
                Talla_S=True, Talla_M=False, Talla_L=False, Talla_XL=True)
db.session.add(prod)
db.session.commit()

# Producto numero 30
prod = Producto(nombre="Chaqueta Cuero", url_img="https://d26lpennugtm8s.cloudfront.net/stores/008/632/products/alexp291-bcd78f35e55d52592f15442927919565-640-0.jpg",
                precio=60831, descrip="Chaqueta en cuero Nina", stock=30, descuento=45,
                inventario=47, tipo='M', rojo=False, azul=False,
                verde=True, negro=True, blanco=False,
                Talla_S=True, Talla_M=False, Talla_L=True, Talla_XL=False)
db.session.add(prod)
db.session.commit()
