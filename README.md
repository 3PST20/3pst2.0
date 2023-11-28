
# 3PST 2.0
### 3PST 2.0 – Sistema web para gestão do portfólio de Programas, Projetos, Produtos, Serviços e Tecnologias do INPE 

Nesta pasta, ficarão os arquivos e informações referentes a plataforma web do 3pst 2.0, eles estarão sujeitos a mudanças constantes.


## Stakeholders
- SEPEC employees: sector employees, who directly participate in the management of portfolio data;
- COGPI employees: coordination employees, who indirectly participate in the management of portfolio data;
- INPE employees: employees of the institution who intend to open TAPs, TAPgs and TAS.

## Programming languages
- Python 3.9 - https://www.python.org/downloads/release/python-390/

## Database
- PostgreSQL 12 - https://www.postgresql.org/download/


## Libraries
- Flask : https://pypi.org/project/Flask/
- Psycopg2 : https://pypi.org/project/psycopg2/


## Frontend Initialization:
- ``flask --app main run``

## Local Database initialization:  
- Main.py line 8:``app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://owner:password@localhost/database'``

