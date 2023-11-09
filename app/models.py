from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Stakeholder(db.Model):
    #atributos conforme o modelo físico
    __tablename__ = 'stakeholder'
    stk_id = db.Column(db.Integer, primary_key=True)
    stk_nome = db.Column(db.Text)
    stk_expectativa = db.Column(db.Text)
    stk_requisito = db.Column(db.Text)

    def to_json(self):
        return{"id": self.stk_id, "parteInteressada": self.stk_nome, "expectativasInteresse": self.stk_expectativa, "requisitos": self.stk_requisito}