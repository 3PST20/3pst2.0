from flask import Flask
from app.models import db
from app.main import views, resources
from flask_migrate import Migrate

app = Flask(__name__, template_folder='./app/templates', static_folder='./app/static')
app.secret_key = "usuario-inpe"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#configurações para a conexão com o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123123@localhost/3pst'

db.init_app(app)
migrate = Migrate(app, db)

views.init_app(app)
resources.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)