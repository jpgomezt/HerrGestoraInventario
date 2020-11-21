from app import *


# Se hace primero el insert de los datos de productos

# Creacion de la cuenta del Admin
hashed_password = generate_password_hash("12345678", method='sha256')
new_user = User(username="admin", email="admon.sojas@gmail.com",
                is_admin=True, password=hashed_password)
comp_user = User.query.filter_by(username="admin").first()
comp_email = User.query.filter_by(email="admon.sojas@gmail.com").first()
if comp_user is not None or comp_email is not None:
    pass
else:
    db.session.add(new_user)
    db.session.commit()

# Creacion de usuario surregog 
hashed_password = generate_password_hash("qwertyuiop", method='sha256')
new_user = User(username="surregog", email="surregog@eafit.edu.co", password=hashed_password)
comp_user = User.query.filter_by(username="surregog").first()
comp_email = User.query.filter_by(email="surregog@eafit.edu.co").first()
if comp_user is not None or comp_email is not None:
    pass
else:
    db.session.add(new_user)
    db.session.commit()

# Creacion de usuario salzatec1 
hashed_password = generate_password_hash("asdfghjkl", method='sha256')
new_user = User(username="salzatec1", email="salzatec1@eafit.edu.co", password=hashed_password)
comp_user = User.query.filter_by(username="salzatec1").first()
comp_email = User.query.filter_by(email="salzatec1@eafit.edu.co").first()
if comp_user is not None or comp_email is not None:
    pass
else:
    db.session.add(new_user)
    db.session.commit()

# Creacion de usuario jpgomezt 
hashed_password = generate_password_hash("qazwsxedcrfv", method='sha256')
new_user = User(username="jpgomezt", email="jpgomezt@eafit.edu.co", password=hashed_password)
comp_user = User.query.filter_by(username="jpgomezt").first()
comp_email = User.query.filter_by(email="jpgomezt@eafit.edu.co").first()
if comp_user is not None or comp_email is not None:
    pass
else:
    db.session.add(new_user)
    db.session.commit()
