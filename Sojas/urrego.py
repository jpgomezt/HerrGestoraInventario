from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import smtplib

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

class Colores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_producto = db.Column(db.Integer, db.ForeignKey('producto.id'))
    rojo = db.Column(db.Boolean(), default = False, nullable = False )
    azul = db.Column(db.Boolean(), default = False, nullable = False )
    verde = db.Column(db.Boolean(), default = False, nullable = False )
    blanco = db.Column(db.Boolean(), default = False, nullable = False )
    negro = db.Column(db.Boolean(), default = True, nullable = False )

class Tallas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_producto = db.Column(db.Integer, db.ForeignKey('producto.id'))
    Talla_S = db.Column(db.Boolean(), default = False, nullable = False )
    Talla_M = db.Column(db.Boolean(), default = True, nullable = False )
    Talla_L = db.Column(db.Boolean(), default = False, nullable = False )
    Talla_XL = db.Column(db.Boolean(), default = False, nullable = False )


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
    #colores = db.Column(db.Integer, db.ForeignKey('colores.id')) #ej: rojo,azul,verde
    #tallas = db.Column(db.Integer, db.ForeignKey('tallas.id')) #ej: S,XL,M


class Pedidos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('user.id'))
    total_ropa_hombre = db.Column(db.Integer)
    total_ropa_mujer = db.Column(db.Integer)
    total_ropa_descuento = db.Column(db.Integer)




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
    if current_user.is_authenticated:
        return render_template('home.html')
    else:
        return render_template('home.html')   

@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/')
def index():
    if current_user.is_authenticated:
        return render_template('home.html')
    else:
        return render_template('home.html')

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

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)

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
        return render_template("consola_admin.html")
    else:
        return redirect(url_for('home'))

@app.route('/consola_admin/informe')
@login_required
def informe():
    if current_user.is_admin:
        subject = "Informe"
        text = "Hello World!"
        message = 'Subject: {}\n\n{}'.format(subject, text)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("notificaciones.sojas@gmail.com", "Cl4v3d3s0j4s")
        server.sendmail("notificaciones.sojas@gmail.com", "jpgomezt@eafit.edu.co", message)
        server.quit()
        return render_template("correo.html")
    else:
        return redirect(url_for('home'))


@app.route('/consola_admin/cantidades', methods=['GET', 'POST'])
@login_required
def cantidades():
    if current_user.is_admin:
        productos = Producto.query.order_by(Producto.id).all()
        colores = Colores.query.order_by(Colores.id).all()
        tallas = Tallas.query.order_by(Tallas.id).all()
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

            prod = Producto(nombre = name, url_img = url_img, precio = precio, descrip = descrip, stock = stock, descuento = descuento, inventario = inventario, tipo = gender)
            try:
                db.session.add(prod)
                db.session.commit()
                col = Colores(id_producto = prod.id ,rojo = color_rojo , azul = color_azul, verde = color_verde , negro = color_negro, blanco = color_blanco)
                db.session.add(col)
                db.session.commit()
                talla = Tallas(id_producto = prod.id,Talla_S = Talla_S, Talla_M = Talla_M, Talla_L = Talla_L, Talla_XL = Talla_XL)
                db.session.add(talla)
                db.session.commit()
                return redirect(url_for('cantidades'))
            except:
                return render_template("/utilidades_admin/cantidades.html", mensaje ="Hubo un problema, agregando el producto", productos = productos, color = colores, talla = tallas)
        else:
            return render_template("/utilidades_admin/cantidades.html", mensaje ="", productos = productos, color = colores, talla = tallas)
    else:
        return redirect(url_for('home'))

@app.route('/consola_admin/cantidades/delete/<int:id>')
def delete_producto(id):
    if current_user.is_admin:
        product_to_delete = Producto.query.get_or_404(id)
        colors_to_delete = Colores.query.get_or_404(id)
        tallas_to_delete = Tallas.query.get_or_404(id)
        try:
            db.session.delete(product_to_delete)
            db.session.delete(colors_to_delete)
            db.session.delete(tallas_to_delete)
            db.session.commit()
            return redirect(url_for('cantidades'))
        except:
            return 'Tuvimos problemas eliminando el producto, intentelo de nuevo'
    else:
        return redirect(url_for('home'))


@app.route('/consola_admin/cantidades/update/<int:id>', methods=['GET', 'POST'])
def update_producto(id):
    if current_user.is_admin:
        productos = Producto.query.get_or_404(id)
        colores = Colores.query.get_or_404(id)
        tallas = Tallas.query.get_or_404(id)
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

                colores.rojo = color_rojo
                colores.azul = color_azul
                colores.verde = color_verde
                colores.negro = color_negro
                colores.blanco = color_blanco

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
                
                tallas.Talla_S = Talla_S
                tallas.Talla_M = Talla_M
                tallas.Talla_L = Talla_L
                tallas.Talla_XL = Talla_XL

                try:
                    db.session.commit()
                    return redirect(url_for('cantidades'))
                except:
                    return 'Hubo problemas actualizando el producto'

        else:
            return render_template('/utilidades_admin/actualizar_producto.html', productos=productos, colores = colores, tallas = tallas)
    else:
        return redirect(url_for('home'))



@app.route('/products', methods=['GET', 'POST'])
def product():
    productos = Producto.query.order_by(Producto.id).all()
    return render_template('products.html', productos=productos)

if __name__ == '__main__':
    #Creacion de la cuenta del Admin
    hashed_password = generate_password_hash("12345678", method='sha256')
    new_user = User(username="admin", email="admon.sojas@gmail.com",is_admin=True ,password=hashed_password)
    comp_user = User.query.filter_by(username="admin").first()
    comp_email = User.query.filter_by(email="admon.sojas@gmail.com").first()
    if comp_user is not None or comp_email is not None:
        pass
    else:
        db.session.add(new_user)
        db.session.commit()
    app.run(debug=True)
