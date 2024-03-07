from flask import Flask
from pst.models import db

app = Flask(__name__)

# Key gerada pelo 'secrets.token_hex(16)'
app.secret_key = 'cbd8aee641f63f8f5e263aa423e63743'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#configurações para a conexão com o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123123@localhost:5432/3pst'

db.init_app(app)

#Importando blueprints
from pst.main.routes import main
from pst.projeto.routes import projeto

#Registrando blueprints
app.register_blueprint(main)
app.register_blueprint(projeto)

from pst import models