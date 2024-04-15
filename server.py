from flask import Flask
from flask_session import Session
from flask_login import LoginManager
from routes.login import login_page
from routes.match import match_page
from session import def_loader


app = Flask(__name__)

# Estrategia usada para almacenar las sessiones de usuarios
app.config['SESSION_TYPE'] = 'filesystem' 

# Clave secreta usada para firmar las claves de session de usuarios
app.config['SECRET_KEY'] = 'I[MQ1q)Yoy?.Txe&3Ez:f@9(nlmfNxE25/2aL~LurS'

# Configurar las sessiones
Session(app)

# Configurar la extension para el inicio de session
login_manager = LoginManager()
login_manager.init_app(app)
def_loader(login_manager)


# Agregar las rutas
app.register_blueprint(login_page)
app.register_blueprint(match_page)

# Finalmente, ejecutar aplicacion
app.run('0.0.0.0', 5000)