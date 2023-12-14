from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Projeto(db.Model):
    __tablename__ = 'projeto'
    id = db.Column(db.Integer, primary_key=True)

    nomeProjeto = db.Column(db.String(140), default="")
    processoSEIProjeto = db.Column(db.String(140), default="")

    stakeholder = db.relationship('Stakeholder', backref='projeto', lazy='dynamic')


class Stakeholder(db.Model):
    #atributos conforme o modelo físico
    __tablename__ = 'stakeholder'
    stk_id = db.Column(db.Integer, primary_key=True)
    projeto_id = db.Column(db.Integer, db.ForeignKey('projeto.id'))

    stk_parteInteressada = db.Column(db.Text, default="")
    stk_expectativa = db.Column(db.Text, default="")
    stk_requisito = db.Column(db.Text, default="")

    def to_json(self):
        return{"id": self.stk_id, "parteInteressada": self.stk_parteInteressada, "expectativasInteresse": self.stk_expectativa, "requisitos": self.stk_requisito}