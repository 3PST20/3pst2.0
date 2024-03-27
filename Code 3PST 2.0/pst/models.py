from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Projeto(db.Model):
    __tablename__ = 'projeto'
    id = db.Column(db.Integer, primary_key=True)

    nomeProjeto = db.Column(db.String(140), nullable=False)
    processoSEIProjeto = db.Column(db.String(140), nullable=False)
    responsavelProjeto = db.Column(db.String(140), nullable=False)
    unidadeResponsavel = db.Column(db.String(140), nullable=False)
    unidadeExecutora = db.Column(db.String(140), nullable=False)
    categoriaProjeto = db.Column(db.String(140), nullable=False)
    situacaoProjeto = db.Column(db.String(140), nullable=False)
    situacaoTAP = db.Column(db.String(140), nullable=False)

    identificacao = db.relationship('Identificacao', backref='projeto', lazy='dynamic', passive_deletes=True)
    alinha1 = db.relationship('Alinhamento1', backref='projeto', lazy='dynamic', passive_deletes=True)
    alinha2 = db.relationship('Alinhamento2', backref='projeto', lazy='dynamic', passive_deletes=True)
    gera_impacto = db.relationship('GeracaoImpacto', backref='projeto', lazy='dynamic', passive_deletes=True)
    descri_detalhe = db.relationship('DescricaoDetalhada', backref='projeto', lazy='dynamic', passive_deletes=True)
    stakeholder = db.relationship('Stakeholder', backref='projeto', lazy='dynamic', passive_deletes=True)
    escopo = db.relationship('Escopo', backref='projeto', lazy='dynamic', passive_deletes=True)
    equipe = db.relationship('Equipe', backref='projeto', lazy='dynamic', passive_deletes=True)
    custos = db.relationship('Custos', backref='projeto', lazy='dynamic', passive_deletes=True)
    riscos = db.relationship('Riscos', backref='projeto', lazy='dynamic', passive_deletes=True)
    historico = db.relationship('Historico', backref='projeto', lazy='dynamic', passive_deletes=True)

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
    dataInicioProjeto = db.Column(db.Date)
    dataConclusaoProjeto = db.Column(db.Date)
    aprovacaoUORG = db.Column(db.Date)
    aprovacaoPortfolio = db.Column(db.Date)
    carregamentoSIGE3P = db.Column(db.Date)
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

    def __repr__(self):
        return f"Identificacao('{self.protocoloSEIUltimoTAP}', '{self.programaAssociado}', '{self.processoSEIPrograma}', '{self.duracaoEstimadaProjeto}')"

class Alinhamento1(db.Model):
    __tablename__ = 'alinhamento1'
    id = db.Column(db.Integer, primary_key=True)
    projeto_id = db.Column(db.Integer, db.ForeignKey('projeto.id', ondelete='CASCADE'))
    
    objetivosEstrategicos = db.Column(db.String(140))
    metasEstrategicas = db.Column(db.String(140))
    periodoAlinha1 = db.Column(db.String(140))
    politicaNacional = db.Column(db.Text)
    programaPPA = db.Column(db.String(140))
    periodoProgramaPPA = db.Column(db.String(140))
    evidenciaAlinha1ProgramaPPA = db.Column(db.Text)
    objetivoPPA = db.Column(db.String(140))
    periodoObjetivoPPA = db.Column(db.String(140))
    evidenciaAlinha1ObjetivoPPA = db.Column(db.Text)

    def __repr__(self):
        return f"Alinhamento1('{self.objetivosEstrategicos}', '{self.metasEstrategicas}', '{self.periodoAlinha1}', '{self.politicaNacional}', '{self.programaPPA}', '{self.objetivoPPA}')"
        
class Alinhamento2(db.Model):
    __tablename__ = 'alinhamento2'
    id = db.Column(db.Integer, primary_key=True)
    projeto_id = db.Column(db.Integer, db.ForeignKey('projeto.id', ondelete='CASCADE'))

    areaPrioritariaENCTI = db.Column(db.String(140))
    periodoAlinha2 = db.Column(db.String(140))
    evidenciaAlinha2AreaPrioritaria = db.Column(db.String(140))
    objetivosDesenvolvimento = db.Column(db.String(140))
    evidenciaAlinha2Objetivos = db.Column(db.String(140))
    mapaEstrategico = db.Column(db.String(140))
    evidenciaAlinha2MapaEstrategico = db.Column(db.String(140))
    eixosDiretrizesEstrategia = db.Column(db.String(140))
    evidenciaAlinha2EixosDiretrizes = db.Column(db.String(140))
    areaTematicaMCTI = db.Column(db.String(140))
    evidenciaAlinha2AreaTematica = db.Column(db.String(140))
    areaTecnologiasPrioritarias = db.Column(db.String(140))
    evidenciaAlinha2AreaTecnologias = db.Column(db.String(140))
    politicasPublicas = db.Column(db.String(140))
    outrasPoliticasPublicas = db.Column(db.String(140))
    evidenciaAlinha2OutrasPoliticasPublicas = db.Column(db.String(140))
    impactado = db.Column(db.String(140))
    justificativa = db.Column(db.String(140))
    estrategia = db.Column(db.String(140))

    def __repr__(self):
        return f"Alinhamento2('{self.areaPrioritariaENCTI}', '{self.periodoAlinha2}', '{self.evidenciaAlinha2AreaPrioritaria}', '{self.objetivosDesenvolvimento}', '{self.mapaEstrategico}', '{self.eixosDiretrizesEstrategia}', '{self.areaTematicaMCTI}', '{self.areaTecnologiasPrioritarias}', '{self.politicasPublicas}', '{self.outrasPoliticasPublicas}', '{self.impactado}', '{self.justificativa}', '{self.estrategia}')"
    
class GeracaoImpacto(db.Model):
    __tablename__ = 'geracao_impacto'
    id = db.Column(db.Integer, primary_key=True)
    projeto_id = db.Column(db.Integer, db.ForeignKey('projeto.id', ondelete='CASCADE'))

    perspectivaPopulacao = db.Column(db.Text)
    missaoMCTI = db.Column(db.String(140))
    perspectivaGestaoMCTI = db.Column(db.String(140))
    perspectivaGestaoINPE = db.Column(db.String(140))
    perspectivaUORG = db.Column(db.Text)
    perspectivaOrgaos = db.Column(db.Text)
    metasPoliticasPublicas = db.Column(db.Text)

    def __repr__(self):
        return f"GeracaoImpacto('{self.missaoMCTI}', '{self.perspectivaGestaoMCTI}', '{self.perspectivaGestaoINPE}')"
    
class DescricaoDetalhada(db.Model):
    __tablename__ = 'descricao_detalhada'
    id = db.Column(db.Integer, primary_key=True)
    projeto_id = db.Column(db.Integer, db.ForeignKey('projeto.id', ondelete='CASCADE'))

    descricaoProdutosServicos = db.Column(db.Text)
    justificativaDescricao = db.Column(db.String(140))
    resultadosEsperados = db.Column(db.String(140))
    capacidadeTecnica = db.Column(db.String(140))
    publicoAlvo = db.Column(db.String(140))
    objetivoGeral = db.Column(db.String(140))
    objetivosEspecificos = db.Column(db.Text)
    metasProjetoCriterios = db.Column(db.Text)
    trlAtual = db.Column(db.String(80))
    trlEsperado = db.Column(db.String(80))
    trlFinal = db.Column(db.String(80))
    requisitosEncerramento = db.Column(db.String(140))
    sustentabilidade = db.Column(db.String(140))
    objetivoDescricao = db.Column(db.String(140))
    descricaoCatalogoInstitucional = db.Column(db.String(140))

    def __repr__(self):
        return f"DescricaoDetalhada('{self.justificativaDescricao}', '{self.resultadosEsperados}', '{self.perspectivaGestaoINPE}')"

class Stakeholder(db.Model):
    #atributos conforme o modelo físico
    __tablename__ = 'stakeholder'
    stk_id = db.Column(db.Integer, primary_key=True)
    projeto_id = db.Column(db.Integer, db.ForeignKey('projeto.id', ondelete='CASCADE'))

    stk_parteInteressada = db.Column(db.Text)
    stk_expectativa = db.Column(db.Text)
    stk_requisito = db.Column(db.Text)

    def __repr__(self):
        return f"Stakeholder('{self.stk_parteInteressada}', '{self.stk_expectativa}', '{self.stk_requisito}')"
    
class Escopo(db.Model):
    __tablename__ = 'escopo'
    id = db.Column(db.Integer, primary_key=True)
    projeto_id = db.Column(db.Integer, db.ForeignKey('projeto.id', ondelete='CASCADE'))
    
    premissasProjeto = db.Column(db.Text)
    restricoesProjeto = db.Column(db.Text)
    escopoProjeto = db.Column(db.Text)
    exclusoesProjeto = db.Column(db.Text)
    fatoresExternos = db.Column(db.Text)

    def __repr__(self):
        return f"Escopo('{self.premissasProjeto}', '{self.restricoesProjeto}', '{self.escopoProjeto}', '{self.exclusoesProjeto}', '{self.fatoresExternos}')"
    
class Equipe(db.Model):
    __tablename__ = 'equipe'
    id = db.Column(db.Integer, primary_key=True)
    projeto_id = db.Column(db.Integer, db.ForeignKey('projeto.id', ondelete='CASCADE'))

    nomeProfissional = db.Column(db.String(140))
    vinculoINPE = db.Column(db.String(140))
    organizacoesExterna = db.Column(db.String(140))
    nomeProfissionalExterno = db.Column(db.String(140))

    def __repr__(self):
        return f"Escopo('{self.nomeProfissional}', '{self.vinculoINPE}', '{self.organizacoesExterna}', '{self.nomeProfissionalExterno}')"

class Custos(db.Model):
    __tablename__ = 'custos'
    id = db.Column(db.Integer, primary_key=True)
    projeto_id = db.Column(db.Integer, db.ForeignKey('projeto.id', ondelete='CASCADE'))

    codigoAreaOrcamento = db.Column(db.String(80))
    orcamentoProjeto = db.Column(db.Text)
    custoEstimado = db.Column(db.String(140))
    observacaoCustoEstimado = db.Column(db.String(140))
    disponibilidadeOrcamentaria = db.Column(db.String(140))
    valorDisponivel = db.Column(db.String(140))
    instituicao = db.Column(db.String(140))

    def __repr__(self):
        return f"Custos('{self.codigoAreaOrcamento}', '{self.custoEstimado}', '{self.observacaoCustoEstimado}')"
    
class Riscos(db.Model):
    __tablename__ = 'riscos'
    id = db.Column(db.Integer, primary_key=True)
    projeto_id = db.Column(db.Integer, db.ForeignKey('projeto.id', ondelete='CASCADE'))

    riscosProjeto = db.Column(db.Text)

    def __repr__(self):
        return f"Riscos('{self.riscosProjeto}')"
    
class Historico(db.Model):
    __tablename__ = 'historico'
    id = db.Column(db.Integer, primary_key=True)
    projeto_id = db.Column(db.Integer, db.ForeignKey('projeto.id', ondelete='CASCADE'))

    evento = db.Column(db.String(140))
    dataRegistro = db.Column(db.Date)
    responsavelRegistro = db.Column(db.String(140))

    def __repr__(self):
        return f"Riscos('{self.evento}', '{self.dataRegistro}', '{self.responsavelRegistro}')"