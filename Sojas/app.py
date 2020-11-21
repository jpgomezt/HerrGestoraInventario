from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import smtplib
import random
import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'True'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    is_admin = db.Column(db.Boolean(), default = False, nullable = False )
    password = db.Column(db.String(80))
    direccion = db.Column(db.String(80),default='')
    ciudad = db.Column(db.String(80),default='')
    tarjeta = db.Column(db.String(30),default='')
    telefono = db.Column(db.String(15),default='')

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(60))
    url_img = db.Column(db.String(255))
    precio = db.Column(db.Float)
    descrip = db.Column(db.String(255))
    stock = db.Column(db.Integer)
    descuento = db.Column(db.Float)
    inventario = db.Column(db.Integer)
    tipo = db.Column(db.String(30))
    genero = db.Column(db.String(10))
    rojo = db.Column(db.Boolean(), default = False, nullable = False )
    azul = db.Column(db.Boolean(), default = False, nullable = False )
    verde = db.Column(db.Boolean(), default = False, nullable = False )
    blanco = db.Column(db.Boolean(), default = False, nullable = False )
    negro = db.Column(db.Boolean(), default = True, nullable = False )
    Talla_S = db.Column(db.Boolean(), default = False, nullable = False )
    Talla_M = db.Column(db.Boolean(), default = True, nullable = False )
    Talla_L = db.Column(db.Boolean(), default = False, nullable = False )
    Talla_XL = db.Column(db.Boolean(), default = False, nullable = False )
    #colores = db.Column(db.Integer, db.ForeignKey('colores.id')) #ej: rojo,azul,verde
    #tallas = db.Column(db.Integer, db.ForeignKey('tallas.id')tarjetp) #ej: S,XL,M


class Pedidos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('user.id'))
    ganancia_total = db.Column(db.Float)
    ganancia_ropa_hombre = db.Column(db.Float)
    ganancia_ropa_mujer = db.Column(db.Float)
    ganancia_ropa_unisex = db.Column(db.Float)
    cantidad_total = db.Column(db.Integer)
    cantidad_ropa_hombre = db.Column(db.Integer)
    cantidad_ropa_mujer = db.Column(db.Integer)
    cantidad_ropa_unisex = db.Column(db.Integer)

class Carrito(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('user.id'))
    id_producto = db.Column(db.Integer, db.ForeignKey('producto.id'))
    cantidad = db.Column(db.Integer)
    color = db.Column(db.String(60))
    talla = db.Column(db.String(60))

class Registro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('user.id'))
    id_producto = db.Column(db.Integer, db.ForeignKey('producto.id'))
    color = db.Column(db.String(60))
    talla = db.Column(db.String(60))
    precio = db.Column(db.Float)
    fecha = db.Column(db.String(60))


class Comentarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('user.id'))
    id_producto = db.Column(db.Integer, db.ForeignKey('producto.id'))
    num_estrellas = db.Column(db.Float)
    comentario = db.Column(db.String(300))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])



@app.route('/home')
def home():
    productos = Producto.query.order_by(Producto.id).all()
    if current_user.is_authenticated:
        return render_template('home.html', productos = productos)
    else:
        return render_template('home.html', productos = productos)

@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/')
def index():
    productos = Producto.query.order_by(Producto.id).all()
    if current_user.is_authenticated:
        return render_template('home.html', productos = productos)
    else:
        return render_template('home.html', productos = productos)

#Listo
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated == False:
        form = LoginForm()

        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user:
                if check_password_hash(user.password, form.password.data):
                    login_user(user, remember=form.remember.data)
                    return redirect(url_for('home'))

            return render_template('login.html', form=form, error = "No esta registrado! \n Registrate!")    

        return render_template('login.html', form=form, error = "")
    else:
        return redirect(url_for('home'))  

#Listo
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated == False:
        form = RegisterForm()

        if form.validate_on_submit():
            try:
                hashed_password = generate_password_hash(form.password.data, method='sha256')
                new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
                comp_user = User.query.filter_by(username=form.username.data).first()
                comp_email = User.query.filter_by(email=form.email.data).first()
                if comp_user is not None or comp_email is not None:
                    return render_template('signup.html', form=form, error="El usuario o correo ya esta registrado! \n Ingrese uno diferente!")
                else:
                    db.session.add(new_user)
                    db.session.commit()
                    return redirect(url_for('index'))
            except:
                return redirect(url_for('error'))    
        return render_template('signup.html', form=form , error="")
    else:
        return redirect(url_for('home')) 

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


#Todo lo que tengo extension de consola admin debe de tener una
#verificacion si el usuario esta registrado ademas de si es administrador
@app.route('/consola_admin', methods=['GET', 'POST'])
@login_required
def consola_admin():
    if current_user.is_admin:
        cantidades_ropa_hombre = db.engine.execute(f'SELECT cantidad_ropa_hombre FROM Pedidos WHERE cantidad_ropa_hombre > 0')
        ropaHombre = 0
        for cantidad_hombre in cantidades_ropa_hombre:
            ropaHombre = cantidad_hombre[0]
        cantidades_ropa_mujer = db.engine.execute(f'SELECT cantidad_ropa_mujer FROM Pedidos WHERE cantidad_ropa_mujer > 0')
        ropaMujer = 0
        for cantidad_mujer in cantidades_ropa_mujer:
            ropaMujer = cantidad_mujer[0]
        cantidades_ropa_unisex = db.engine.execute(f'SELECT cantidad_ropa_unisex FROM Pedidos WHERE cantidad_ropa_unisex > 0')
        ropaUnisex = 0
        for cantidad_unisex in cantidades_ropa_unisex:
            ropaUnisex = cantidad_unisex[0]
        ganancias_total = db.engine.execute(f'SELECT ganancia_total FROM Pedidos WHERE ganancia_total > 0')
        ganancias = 0
        for ganancias in ganancias_total:
            ganancias = ganancias[0]
        return render_template("consola_admin.html", ropaHombre = ropaHombre, ropaMujer = ropaMujer, ropaUnisex = ropaUnisex, ganancias = ganancias)
    else:
        return redirect(url_for('home'))

@app.route('/consola_admin/informe')
@login_required
def informe():
    if current_user.is_admin:
        return render_template("/utilidades_admin/correo.html", correo = current_user.email)
    else:
        return redirect(url_for('home'))

@app.route('/consola_admin/mandar-informe', methods=['GET', 'POST'])
@login_required
def enviarInforme():
    if current_user.is_admin:
        subject = "Informe"
        text = []
        text.append("Este es el informe generado: \n")
        cantidadHombre = request.form.get('cantidadHombre')
        cantidadMujer = request.form.get('cantidadMujer')
        cantidadUnisex = request.form.get('cantidadUnisex')
        cantidadTotal = request.form.get('cantidadTotal')
        gananciasHombre = request.form.get('gananciasHombre')
        gananciasMujer = request.form.get('gananciasMujer')
        gananciasUnisex = request.form.get('gananciasUnisex')
        gananciasTotal = request.form.get('gananciasTotal')
        if(cantidadHombre == "on"):
            cantidades_ropa_hombre = db.engine.execute(f'SELECT cantidad_ropa_hombre FROM Pedidos WHERE cantidad_ropa_hombre > 0')
            cantidad_ropa_hombre = 0
            for cantidad_hombre in cantidades_ropa_hombre:
                cantidad_ropa_hombre = cantidad_hombre[0]
            text.append("Se han vendido " + str(cantidad_ropa_hombre) + " productos de hombre. \n")
        if(cantidadMujer == "on"):
            cantidades_ropa_mujer = db.engine.execute(f'SELECT cantidad_ropa_mujer FROM Pedidos WHERE cantidad_ropa_mujer > 0')
            cantidad_ropa_mujer = 0
            for cantidad_mujer in cantidades_ropa_mujer:
                cantidad_ropa_mujer = cantidad_mujer[0]
            text.append("Se han vendido " + str(cantidad_ropa_mujer) + " productos de mujer. \n")
        if(cantidadUnisex == "on"):
            cantidades_ropa_unisex = db.engine.execute(f'SELECT cantidad_ropa_unisex FROM Pedidos WHERE cantidad_ropa_unisex > 0')
            cantidad_ropa_unisex = 0
            for cantidad_unisex in cantidades_ropa_unisex:
                cantidad_ropa_unisex = cantidad_unisex[0]
            text.append("Se han vendido " + str(cantidad_ropa_unisex) + " productos unisex. \n")
        if(cantidadTotal == "on"):
            cantidades_total = db.engine.execute(f'SELECT cantidad_total FROM Pedidos WHERE cantidad_total > 0')
            cantidad_total = 0
            for total in cantidades_total:
                ganancia_total = total[0]
            text.append("Se han vendido " + str(ganancia_total) + " productos en total. \n")
        if(gananciasHombre == "on"):
            ganancias_ropa_hombre = db.engine.execute(f'SELECT ganancia_ropa_hombre FROM Pedidos WHERE ganancia_ropa_hombre > 0')
            ganancia_ropa_hombre = 0
            for ganancia_hombre in ganancias_ropa_hombre:
                ganancia_ropa_hombre = ganancia_hombre[0]
            text.append("Se han recaudado $" + str(ganancia_ropa_hombre) + " pesos en ropa de hombre. \n")
        if(gananciasMujer == "on"):
            ganancias_ropa_mujer = db.engine.execute(f'SELECT ganancia_ropa_mujer FROM Pedidos WHERE ganancia_ropa_mujer > 0')
            ganancia_ropa_mujer = 0
            for ganancia_mujer in ganancias_ropa_mujer:
                ganancia_ropa_mujer = ganancia_mujer[0]
            text.append("Se han recaudado $" + str(ganancia_ropa_mujer) + " pesos en ropa de mujer. \n")
        if(gananciasUnisex == "on"):
            ganancias_ropa_unisex = db.engine.execute(f'SELECT ganancia_ropa_unisex FROM Pedidos WHERE ganancia_ropa_unisex > 0')
            ganancia_ropa_unisex = 0
            for ganancia_unisex in ganancias_ropa_unisex:
                ganancia_ropa_unisex = ganancia_unisex[0]
            text.append("Se han recaudado $" + str(ganancia_ropa_unisex) + " pesos en ropa unisex. \n")
        if(gananciasTotal == "on"):
            ganancias_total = db.engine.execute(f'SELECT ganancia_total FROM Pedidos WHERE ganancia_total > 0')
            ganancia_total = 0
            for ganancias in ganancias_total:
                ganancia_total = ganancias[0]
            text.append("Se han recaudado $" + str(ganancia_total) + " pesos en total. \n")
        text = ''.join(text)
        message = 'Subject: {}\n\n{}'.format(subject, text)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("notificaciones.sojas@gmail.com", "Cl4v3d3s0j4s")
        server.sendmail("notificaciones.sojas@gmail.com", current_user.email, message)
        server.quit()
        return render_template("consola_admin.html")
    else:
        return redirect(url_for('home'))

@app.route('/consola_admin/cantidades', methods=['GET', 'POST'])
@login_required
def cantidades():
    if current_user.is_admin:
        productos = Producto.query.order_by(Producto.id).all()
        if request.method == 'POST':
            
            name = request.form['nombre']
            url_img = request.form['url_img']
            precio = request.form['precio']
            descrip = request.form['descrip']
            stock = request.form['stock']
            descuento = request.form['descuento']
            inventario = request.form['inventario']
            color_rojo = False
            color_azul = False
            color_verde = False
            color_negro = False
            color_blanco = False
            Talla_S = False
            Talla_M = False
            Talla_L = False
            Talla_XL = False

            #Para los colores de la ropa
            try:
                color = request.form['rojo']
                color_rojo = True
            except:
                color_rojo = False
            try:
                color = request.form['azul']
                color_azul = True
            except:
                color_azul = False
            try:
                color = request.form['verde']
                color_verde = True
            except:
                color_verde = False
            try:
                color = request.form['negro']
                color_negro = True
            except:
                color_negro = False
            try:
                color = request.form['blanco']
                color_blanco = True
            except:
                color_blanco = False


            #Para los tamaños de la ropa
            try:
                color = request.form['S']
                Talla_S = True
            except:
                Talla_S = False
            try:
                color = request.form['M']
                Talla_M = True
            except:
                Talla_M = False
            try:
                color = request.form['L']
                Talla_L = True
            except:
                Talla_L = False
            try:
                color = request.form['XL']
                Talla_XL = True
            except:
                Talla_XL = False


            gender = request.form['genero']
            
            if (Talla_S or Talla_M or Talla_L or Talla_XL) and ( color_azul or color_rojo or color_blanco or color_negro or color_verde):
                prod = Producto(nombre = name, url_img = url_img, precio = precio, descrip = descrip, stock = stock, descuento = descuento, inventario = inventario, tipo = gender, rojo = color_rojo , azul = color_azul, verde = color_verde , negro = color_negro, blanco = color_blanco, Talla_S = Talla_S, Talla_M = Talla_M, Talla_L = Talla_L, Talla_XL = Talla_XL)
            else:
                return render_template("/utilidades_admin/cantidades.html", mensaje ="No puedes dejar los campos de talla o colores vacios", productos = productos)
            try:
                db.session.add(prod)
                db.session.commit()
                return redirect(url_for('cantidades'))
            except:
                return render_template("/utilidades_admin/cantidades.html", mensaje ="Hubo un problema, agregando el producto", productos = productos)
        else:
            return render_template("/utilidades_admin/cantidades.html", mensaje ="", productos = productos)
    else:
        return redirect(url_for('home'))

@app.route('/consola_admin/cantidades/delete/<int:id>')
@login_required
def delete_producto(id):
    if current_user.is_admin:
        product_to_delete = Producto.query.get_or_404(id)
        try:
            db.session.delete(product_to_delete)
            db.session.commit()
            return redirect(url_for('cantidades'))
        except:
            return 'Tuvimos problemas eliminando el producto, intentelo de nuevo'
    else:
        return redirect(url_for('home'))


@app.route('/consola_admin/cantidades/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update_producto(id):
    if current_user.is_admin:
        productos = Producto.query.get_or_404(id)
        if request.method == 'POST':
                productos.nombre = request.form['nombre']
                productos.url_img = request.form['url_img']
                productos.precio = request.form['precio']
                productos.descrip = request.form['descrip']
                productos.stock = request.form['stock']
                productos.descuento = request.form['descuento']
                productos.inventario = request.form['inventario']
                productos.tipo = request.form['genero']
                color_rojo = False
                color_azul = False
                color_verde = False
                color_negro = False
                color_blanco = False
                Talla_S = False
                Talla_M = False
                Talla_L = False
                Talla_XL = False

                #Para los colores de la ropa
                try:
                    color = request.form['rojo']
                    color_rojo = True
                except:
                    color_rojo = False
                try:
                    color = request.form['azul']
                    color_azul = True
                except:
                    color_azul = False
                try:
                    color = request.form['verde']
                    color_verde = True
                except:
                    color_verde = False
                try:
                    color = request.form['negro']
                    color_negro = True
                except:
                    color_negro = False
                try:
                    color = request.form['blanco']
                    color_blanco = True
                except:
                    color_blanco = False

                productos.rojo = color_rojo
                productos.azul = color_azul
                productos.verde = color_verde
                productos.negro = color_negro
                productos.blanco = color_blanco

                #Para los tamaños de la ropa
                try:
                    color = request.form['S']
                    Talla_S = True
                except:
                    Talla_S = False
                try:
                    color = request.form['M']
                    Talla_M = True
                except:
                    Talla_M = False
                try:
                    color = request.form['L']
                    Talla_L = True
                except:
                    Talla_L = False
                try:
                    color = request.form['XL']
                    Talla_XL = True
                except:
                    Talla_XL = False
                
                productos.Talla_S = Talla_S
                productos.Talla_M = Talla_M
                productos.Talla_L = Talla_L
                productos.Talla_XL = Talla_XL

                try:
                    db.session.commit()
                    return redirect(url_for('cantidades'))
                except:
                    return redirect(url_for('error'))

        else:
            return render_template('/utilidades_admin/actualizar_producto.html', productos=productos)
    else:
        return redirect(url_for('home'))



@app.route('/products', methods=['GET', 'POST'])
def product():
    tipo = "all"
    if request.method == 'POST':
        tipo = request.form.get("tipo")
    productos = Producto.query.order_by(Producto.id).all()
    return render_template('products.html', productos=productos, tipo=tipo)

@app.route('/products/producto/<int:id>', methods=['GET', 'POST'])
def vista_producto(id):
    productos = Producto.query.get_or_404(id)
    query = db.engine.execute(f'SELECT id_usuario,num_estrellas,comentario FROM Comentarios WHERE id_producto = {id} ')
    reviews = []
    for row in query:
        query_user = db.engine.execute(f'SELECT username FROM User WHERE id = {row[0]} ')
        usuario = ""
        for row_user in query_user:
            usuario = row_user[0]
        # El nombre del usuario, las estrellas que le puso y el comentario que realizo
        reviews.append((usuario,int(round(row[1])),row[2]))

    if request.method == 'POST':
        if current_user.is_authenticated:
            if productos.stock > 0:
                color = ""
                talla = ""
                cantidad = 0
                try:
                    color = request.form['color']
                    talla = request.form['Field5']
                    cantidad = int(request.form['cantidad'])
                except:
                    return render_template('productos/vista_productos.html', producto = productos, error = "Dejaste un campo de selección vacio")
                if cantidad <= productos.stock:
                    pedido = Carrito(id_usuario = current_user.id, id_producto = productos.id, cantidad = cantidad, color = color ,talla = talla)
                    
                    try:
                        #print(productos.id)
                        db.session.add(pedido)
                        db.session.commit()
                        return redirect(url_for('carrito')) # Debe despues ir al carrito 
                    except:
                        return render_template('productos/vista_productos.html', producto = productos, error = "Hubo problemas con los datos suministrados", reviews = reviews)
                else:
                    return render_template('productos/vista_productos.html', producto = productos, error = "La cantidad supera la cantidad en Stock no lo puedes agregar!", reviews = reviews)
            else:
                return render_template('productos/vista_productos.html', producto = productos, error = "El stock esta en cero no lo puedes agregar! ", reviews = reviews)
        else:
            return render_template('productos/vista_productos.html', producto = productos, error = "Necesitas estar loguedo para continuar", reviews = reviews)
        
    else:
        return render_template('productos/vista_productos.html', producto = productos, error = "", reviews = reviews)




@app.route('/carrito', methods=['GET', 'POST'])
@login_required
def carrito():
    productos_cart = db.engine.execute(f'SELECT * FROM Carrito WHERE id_usuario = {current_user.id}')
    cantidad = 0
    total = 0
    display_carrito =[]
    #ID Carrito, nombre producto, imagen producto, color, talla , precio del producto, cantidad 
    #Coste total
    for producto in productos_cart :
        tp = db.engine.execute(f'SELECT * FROM Producto WHERE id = {producto[2]}') 
        #print(producto)
        for temp in tp:
            #print(temp)
            coste = temp[3]
            if temp[6] >= 0:
                coste = coste - ((temp[6]/100) * coste)
            tpl = [producto[0],temp[1],temp[2],producto[4], producto[5], coste, producto[3]]
            display_carrito.append(tpl)
            total = total + (coste * producto[3])
        cantidad = cantidad + 1
    if not current_user.is_admin:
        total = total + 5
        return render_template('/productos/carrito.html', productos = display_carrito, total = total)
    else:
        return redirect(url_for('home'))


@app.route('/carrito/producto/delete/<int:id>')
@login_required
def borrar_carrito(id):
    if not current_user.is_admin:
        product_to_delete = Carrito.query.get_or_404(id)
        try:
            db.session.delete(product_to_delete)
            db.session.commit()
            return redirect(url_for('carrito'))
        except:
            return 'Tuvimos problemas eliminando el producto, intentelo de nuevo'
    else:
        return redirect(url_for('home'))


@app.route('/carrito/check_out/', methods=['GET', 'POST'])
@login_required
def check_out():
    if not current_user.is_admin:
        count = db.engine.execute(f'SELECT COUNT(id) FROM Carrito WHERE id_usuario = {current_user.id}')
        num = 0
        for c in count:
            num = c[0]
        if num > 0:
            usuario = User.query.get_or_404(current_user.id)
            if request.method == 'POST':
                usuario.ciudad = request.form['ciudad']
                usuario.telefono = request.form['tel']
                usuario.direccion = request.form['dir']
                try:
                    db.session.commit()
                    return redirect(url_for('finalizar_orden'))
                except:
                    return redirect(url_for('error'))
            else:
                return render_template('/finalizar_orden/check_out.html', usuario = usuario)
        else:
            return redirect(url_for('carrito'))
    else:
        return redirect(url_for('home'))


@app.route('/carrito/check_out/finalizar_orden', methods=['GET', 'POST'])
@login_required
def finalizar_orden():
    if not current_user.is_admin:
        count = db.engine.execute(f'SELECT COUNT(id) FROM Carrito WHERE id_usuario = {current_user.id}')
        num = 0
        for c in count:
            num = c[0]
        if num > 0:
            azar = random.randint(2,15)
            usuario = User.query.get_or_404(current_user.id)
            if request.method == 'POST':
                usuario.tarjeta = request.form['cardNumber']
                if True:
                    cart_del = db.engine.execute(f'SELECT * FROM Carrito WHERE id_usuario = {current_user.id}')
                    total_h = 0    
                    total_m = 0    
                    total_u = 0
                    cantidad_h = 0
                    cantidad_m = 0
                    cantidad_u = 0
                    for cart in cart_del:
                        producto = Producto.query.get_or_404(cart[2])
                        producto.stock = producto.stock - cart[3]
                        
                        # 5 es coste de envio mas impuestos
                        if producto.tipo == 'H':
                            total_h = total_h + ((producto.precio - ((producto.descuento/100) * producto.precio)) * cart[3])
                            cantidad_h += (1 * cart[3])
                        elif producto.tipo == 'M':
                            total_m = total_m + ((producto.precio - ((producto.descuento/100) * producto.precio)) * cart[3])
                            cantidad_m += (1 * cart[3])
                        else:
                            total_u = total_u + ((producto.precio - ((producto.descuento/100) * producto.precio)) * cart[3])
                            cantidad_u += (1 * cart[3])

                        registro = Registro(id_usuario = current_user.id, id_producto = cart[2], color = cart[4], talla = cart[5], precio = producto.precio, fecha = datetime.datetime.today().date())
                        db.session.add(registro)
                    pedido = Pedidos(id_usuario = current_user.id, ganancia_total = (5 + total_h + total_m + total_u), ganancia_ropa_hombre = total_h, ganancia_ropa_mujer = total_m, ganancia_ropa_unisex = total_u, cantidad_total = (cantidad_h + cantidad_m + cantidad_u), cantidad_ropa_hombre = cantidad_h, cantidad_ropa_mujer = cantidad_m, cantidad_ropa_unisex = cantidad_u)
                    db.session.add(pedido)
                    db.session.commit()
                    cart_del = db.engine.execute(f'DELETE FROM Carrito WHERE id_usuario = {current_user.id}')
                    
                    return redirect(url_for('consola_usuario'))
                else:
                    return redirect(url_for('error'))
            else:
                return render_template('/finalizar_orden/tarjeta.html',usuario = usuario, rand = azar)
        else:
            return redirect(url_for('carrito'))
    else:
        return redirect(url_for('home'))
    





#Modificaciones hechas a partir de esta linea!!!!!!!!!!!!!!!!!!

@app.route('/consola_usuario', methods=['GET', 'POST'])
@login_required
def consola_usuario():
    if not current_user.is_admin:
        
        query = db.engine.execute(f'SELECT * FROM Registro WHERE id_usuario = {current_user.id} ORDER BY id DESC')
        historico = []
        recientemente = []
        fecha = ""
        primera = True
        for row in query:
            url_img = ""
            nombre = ""
            query_pro = db.engine.execute(f'SELECT * FROM Producto WHERE id = {row[2]}')
            for row_pro in query_pro:
                nombre = row_pro[1]
                url_img = row_pro[2]
            
            if primera:
                fecha = row[6]
                primera = False
            
            #Id del producto, Color, talla, precio, fecha , url_img, nombre producto
            tpl = (row[2],row[3],row[4],row[5],row[6],url_img, nombre)

            if fecha == row[6]:
                recientemente.append(tpl)

            historico.append(tpl)
        
        return render_template("/utilidades_usuario/consola_usuario.html", hist = historico, recien = recientemente)
    else:
        return redirect(url_for('home'))


@app.route('/consola_usuario/resena/<int:id>', methods=['GET', 'POST'])
@login_required
def review(id):
    if not current_user.is_admin:
        query_compra = db.engine.execute(f'SELECT COUNT(*) FROM Registro WHERE id_usuario = {current_user.id} and id_producto = {id}')
        for row in query_compra:
            if row[0] == 0:
                return "Usted no ha comprado este producto! No se puedes dar una reseña de este articulo!!!"


        producto = Producto.query.get_or_404(id)

        if request.method == 'POST':
                comentario = request.form['comentario']
                if len(comentario) > 299:
                    return render_template('/utilidades_usuario/review.html', productos = producto , error = "Has escrito una reseña un poco larga" )

                estrellas = request.form['estrellas']
                if estrellas <= 5 or estrellas >=1: 
                    review = Comentarios(id_usuario = current_user.id, id_producto = producto.id, num_estrellas = int(estrellas) , comentario = comentario)
                    try:
                        db.session.add(review)
                        db.session.commit()
                        return redirect(url_for('consola_usuario'))
                    except:
                        return redirect(url_for('error'))
                else:
                    return render_template('/utilidades_usuario/review.html', productos = producto , error = "Has colocado un numero de estrellas equivocado" )

        else:
            return render_template('/utilidades_usuario/review.html', productos = producto, error = "")
    else:
        return redirect(url_for('home'))


@app.route('/quienes_somos')
def quienes_somos():
    return render_template('somos.html')

 

if __name__ == '__main__':
    app.run(debug=True)