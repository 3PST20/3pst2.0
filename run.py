from pst2 import app, db
from flask_migrate import Migrate

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)

# Para rodar o projeto -> python run.py
# Para instalar os pacotes -> pip install -r requirements.txt