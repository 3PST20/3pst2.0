from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Projeto(db.Model):
    __tablename__ = 'projeto'
    id = db.Column(db.Integer, primary_key=True)

    nomeProjeto = db.Column(db.String(140), nullable=False)
    processoSEIProjeto = db.Column(db.String(140), nullable=False)
    responsavelProjeto = db.Column(db.String(140))
    unidadeResponsavel = db.Column(db.String(140))
    unidadeExecutora = db.Column(db.String(140))
    categoriaProjeto = db.Column(db.String(140))
    situacaoProjeto = db.Column(db.String(140))
    situacaoTAP = db.Column(db.String(140))

    stakeholder = db.relationship('Stakeholder', backref='projeto', lazy='dynamic', passive_deletes=True)
    identificacao = db.relationship('Identificacao', backref='projeto', lazy='dynamic', passive_deletes=True)

    def __repr__(self):
        return f"Projeto('{self.nomeProjeto}', '{self.processoSEIProjeto}', '{self.responsavelProjeto}', '{self.unidadeResponsavel}', '{self.unidadeExecutora}', '{self.categoriaProjeto}', '{self.situacaoProjeto}', '{self.situacaoTAP}')"

class Identificacao(db.Model):
    __tablename__ = 'identificacao'
    ident_id = db.Column(db.Integer, primary_key=True)
    projeto_id = db.Column(db.Integer, db.ForeignKey('projeto.id', ondelete='CASCADE'))

    protocoloSEIUltimoTAP = db.Column(db.String(140))
    programaAssociado = db.Column(db.String(140))
    processoSEIPrograma = db.Column(db.String(140))
    duracaoEstimadaProjeto = db.Column(db.String(140))
    dataInicioProjeto = db.Column(db.DateTime)
    dataConclusaoProjeto = db.Column(db.DateTime)
    aprovacaoUORG = db.Column(db.DateTime)
    aprovacaoPortfolio = db.Column(db.DateTime)
    carregamentoSIGE3P = db.Column(db.DateTime)
    objetoProjeto = db.Column(db.Text)
    descricaoProjeto = db.Column(db.Text)
    prioridadeINPE = db.Column(db.String(140))
    evidenciaPriorizacao = db.Column(db.String(140))
    tipoParceria = db.Column(db.String(140))
    situacaoParceria = db.Column(db.String(140))
    processoSEIParceria = db.Column(db.String(140))
    propriedadeIntelectual = db.Column(db.String(140))
    faixaCustoTotalProjeto = db.Column(db.String(140))
    recursosFinanceiros = db.Column(db.String(140))

class Stakeholder(db.Model):
    #atributos conforme o modelo físico
    __tablename__ = 'stakeholder'
    stk_id = db.Column(db.Integer, primary_key=True)
    projeto_id = db.Column(db.Integer, db.ForeignKey('projeto.id', ondelete='CASCADE'))

    stk_parteInteressada = db.Column(db.Text)
    stk_expectativa = db.Column(db.Text)
    stk_requisito = db.Column(db.Text)

    def __repr__(self):
        return f"Projeto('{self.stk_parteInteressada}', '{self.stk_expectativa}', '{self.stk_requisito}')"