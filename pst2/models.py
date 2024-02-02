from pst2 import db, bcrypt

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(140), nullable=False)
    email = db.Column(db.String(140), unique=True, nullable=False)
    tipoUsuario = db.Column(db.String(60), nullable=False)
    senha = db.Column(db.String(255), nullable=False)

    def to_json(self):
        return{"id": self.id, "nome": self.nome, "email": self.email, "tipoUsuario": self.tipoUsuario}
    
    def __init__(self, nome, email, tipoUsuario, senha):
        self.nome = nome
        self.email = email
        self.tipoUsuario = tipoUsuario
        self.senha = bcrypt.generate_password_hash(senha).decode('utf-8')

class Projeto(db.Model):
    __tablename__ = 'projeto'
    id = db.Column(db.Integer, primary_key=True)

    nomeProjeto = db.Column(db.String(140), default="")
    processoSEIProjeto = db.Column(db.String(140), default="")

    stakeholder = db.relationship('Stakeholder', backref='projeto', lazy='dynamic', passive_deletes=True)


class Stakeholder(db.Model):
    #atributos conforme o modelo físico
    __tablename__ = 'stakeholder'
    stk_id = db.Column(db.Integer, primary_key=True)
    projeto_id = db.Column(db.Integer, db.ForeignKey('projeto.id', ondelete='CASCADE'))

    stk_parteInteressada = db.Column(db.Text, default="")
    stk_expectativa = db.Column(db.Text, default="")
    stk_requisito = db.Column(db.Text, default="")

    def to_json(self):
        return{"id": self.stk_id, "parteInteressada": self.stk_parteInteressada, "expectativasInteresse": self.stk_expectativa, "requisitos": self.stk_requisito}