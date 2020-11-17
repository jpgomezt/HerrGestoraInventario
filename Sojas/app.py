from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

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

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(60))
    url_img = db.Column(db.String(255))
    precio = db.Column(db.String(30))
    descrip = db.Column(db.String(255))
    stock = db.Column(db.String(30))
    descuento = db.Column(db.String(30))
    inventario = db.Column(db.String(30))




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
            prod = Producto(nombre = name, url_img = url_img, precio = precio, descrip = descrip, stock = stock, descuento = descuento, inventario = inventario)
            try:
                db.session.add(prod)
                db.session.commit()
                return render_template("/utilidades_admin/cantidades.html", mensaje ="Añadido correctamente", productos = productos)
            except:
                return render_template("/utilidades_admin/cantidades.html", mensaje ="Hubo un problema, agregando el producto", productos = productos)
        else:
            return render_template("/utilidades_admin/cantidades.html", mensaje ="", productos = productos)
    else:
        return redirect(url_for('home'))

@app.route('/products', methods=['GET', 'POST'])
def product():
    productos = Producto.query.order_by(Producto.id).all()
    return render_template('products.html', productos=productos)

if __name__ == '__main__':
    #Creacion de la cuenta del Admin
    hashed_password = generate_password_hash("12345678", method='sha256')
    new_user = User(username="admin", email="admin@admin.com",is_admin=True ,password=hashed_password)
    comp_user = User.query.filter_by(username="admin").first()
    comp_email = User.query.filter_by(email="admin@admin.com").first()
    if comp_user is not None or comp_email is not None:
        pass
    else:
        db.session.add(new_user)
        db.session.commit()
    app.run(debug=True)
