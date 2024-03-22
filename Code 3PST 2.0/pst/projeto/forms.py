from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, DateField
from wtforms.validators import DataRequired, Optional

class ProjetoForm(FlaskForm):
    #identificacao
    nomeProjeto = StringField('Nome do Projeto', validators=[DataRequired()])
    processoSEIProjeto = StringField('Processo SEI do Projeto', validators=[DataRequired()])
    protocoloSEIUltimoTAP = StringField('Protocolo SEI da última versão do TAP que foi aprovada para compor o Portfólio Institucional')
    programaAssociado = SelectField('Programa Associado', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
    processoSEIPrograma = SelectField('Processo SEI do Programa Associado', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
    responsavelProjeto = SelectField('Responsável pelo Projeto', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')], validators=[DataRequired()])
    unidadeResponsavel = SelectField('Unidade Responsável', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')], validators=[DataRequired()])
    unidadeExecutora = SelectField('Unidade(s) Executora(s)', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')], validators=[DataRequired()])
    categoriaProjeto = SelectField('Categoria do Projeto', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')], validators=[DataRequired()])
    situacaoProjeto = SelectField('Situação do Projeto', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')], validators=[DataRequired()])
    duracaoEstimadaProjeto = StringField('Duração Estimada do Projeto (meses)')
    situacaoTAP = SelectField('Situação do TAP', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')], validators=[DataRequired()])
    dataInicioProjeto = DateField('Data de Início do Projeto', format='%Y-%m-%d', validators=[Optional()])
    dataConclusaoProjeto = DateField('Data de Conclusão do Projeto', format='%Y-%m-%d', validators=[Optional()])
    aprovacaoUORG = DateField('Aprovação da UORG', format='%Y-%m-%d', validators=[Optional()])
    aprovacaoPortfolio = DateField('Aprovação para Portfólio INPE', format='%Y-%m-%d', validators=[Optional()])
    carregamentoSIGE3P = DateField('Carregamento no SIGE3P', format='%Y-%m-%d', validators=[Optional()])
    objetoProjeto = TextAreaField('Objeto do Projeto')
    descricaoProjeto = TextAreaField('Descrição do Projeto')
    prioridadeINPE = SelectField('Prioridade INPE', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
    evidenciaPriorizacao = StringField('Evidência da priorização pelo INPE')
    tipoParceria = SelectField('Tipo de Parceria', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
    situacaoParceria = SelectField('Situação da Parceria', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
    processoSEIParceria = StringField('Processo SEI da Parceria')
    propriedadeIntelectual = SelectField('Propriedade Intelectual', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
    faixaCustoTotalProjeto = SelectField('Faixa de Custo Total do Projeto', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
    recursosFinanceiros = SelectField('Recursos Financeiros Disponiveis', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])

    #alinhamento1
    objetivosEstrategicos = SelectField('Objetivos Estratégicos do INPE', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
    metasEstrategicas = SelectField('Metas Estratégicas do INPE', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
    periodoAlinha1 = SelectField('Período Estratégico do INPE', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
    politicaNacional = TextAreaField('Política Nacacional de Inovação e Política de Inovação do INPE')
    programaPPA = SelectField('Programa PPA', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
    periodoProgramaPPA = SelectField('Período do Programa PPA', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
    evidenciaAlinha1ProgramaPPA = TextAreaField('Evidência do Alinhamento do Programa PPA')
    objetivoPPA = SelectField('Objetivo do PPA', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
    periodoObjetivoPPA = SelectField('Período do Objetivo do PPA', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
    evidenciaAlinha1ObjetivoPPA = TextAreaField('Evidência do Alinhamento do Objetivo do PPA')

    #alinhamento2
    areaPrioritariaENCTI = SelectField('Área Prioritária ENCTI', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
    periodoAlinha2 = SelectField('Período da Área Prioritária ENCTI', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
    evidenciaAlinha2AreaPrioritaria = TextAreaField('Evidência do Alinhamento da Área Prioritária ENCTI')
    objetivosDesenvolvimento = SelectField('Objetivos de Desenvolvimento Sustentável - Agenda 2030 ONU', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
    evidenciaAlinha2Objetivos = TextAreaField('Evidência do Alinhamento dos Objetivos de Desenvolvimento Sustentável - Agenda 2030 ONU')
    mapaEstrategico = SelectField('Mapa Estratégico do MCTI 2020-2030', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
    evidenciaAlinha2MapaEstrategico = TextAreaField('Evidência do Alinhamento do Mapa Estratégico do MCTI 2020-2030')
    eixosDiretrizesEstrategia = SelectField('Eixos e Diretrizes da Estratégia Nacional de Desenvolvimento Econômico e Social', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
    evidenciaAlinha2EixosDiretrizes = TextAreaField('Evidência do Alinhamento dos Eixos e Diretrizes da Estratégia Nacional de Desenvolvimento Econômico e Social')
    areaTematicaMCTI = SelectField('Área Temática MCTI', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
    evidenciaAlinha2AreaTematica = TextAreaField('Evidência do Alinhamento da Área Temática MCTI')
    areaTecnologiasPrioritarias = SelectField('Área de Tecnologias Prioritárias', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
    evidenciaAlinha2AreaTecnologias = TextAreaField('Evidência do Alinhamento da Área de Tecnologias Prioritárias')
    politicasPublicas = SelectField('Políticas Públicas', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
    outrasPoliticasPublicas = TextAreaField('Outras Políticas Públicas')
    evidenciaAlinha2OutrasPoliticasPublicas = TextAreaField('Evidência do Alinhamento de Outras Políticas Públicas')
    impactado = SelectField('Impactado', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
    justificativa = TextAreaField('Justificativa')
    estrategia = SelectField('Estratégia - Objetivo Estratégico', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])

    #geracaoImpacto
    perspectivaPopulacao = TextAreaField('Perspectiva População Brasileira')
    missaoMCTI = TextAreaField('Missão MCTI')
    perspectivaGestaoMCTI = TextAreaField('Perspectiva Alta Gestão MCTI')
    perspectivaGestaoINPE = TextAreaField('Perspectiva Alta Gestão INPE')
    perspectivaUORG = TextAreaField('Perspectiva UORG Responsável')
    perspectivaOrgaos = TextAreaField('Perspectiva Órgãos Controle')
    metasPoliticasPublicas = TextAreaField('Metas Políticas Públicas')
    
    #Descrição detalhada
    descricaoProdutosServicos = TextAreaField('Descrição do(s) produto(s)/ serviço(s) que será(ão) entregues')
    justificativaDescricao = TextAreaField('Justificativa do projeto')
    resultadosEsperados = TextAreaField('Resultados esperados')
    capacidadeTecnica = TextAreaField('Capacidade técnica operacional')
    publicoAlvo = TextAreaField('Público alvo')
    objetivoGeral = TextAreaField('Objetivo geral')
    objetivosEspecificos = TextAreaField('Objetivos específicos')
    metasProjetoCriterios = TextAreaField('Metas do projeto e critérios de sucesso relacionados')
    trlAtual = SelectField('TRL atual', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
    trlEsperado = SelectField('TRL esperado ao fim do projeto', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
    trlFinal = SelectField('TRL final', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
    requisitosEncerramento = TextAreaField('Requisitos para encerramento do projeto')
    sustentabilidade = TextAreaField('Sustentabilidade')
    objetivoDescricao = TextAreaField('Objetivo do Projeto')
    descricaoCatalogoInstitucional = TextAreaField('Descrição do Projeto para compor o Catálogo Institucional')

    #Stakeholders
    stk_parteInteressada = StringField('Parte interessada')
    stk_expectativa = StringField('Expectativas e interesses')
    stk_requisito = StringField('Requisitos')

    #Escopo
    premissasProjeto = TextAreaField('Premissas do projeto')
    restricoesProjeto = TextAreaField('Restrições do projeto')
    escopoProjeto = TextAreaField('Escopo do projeto')
    exclusoesProjeto = TextAreaField('Exclusões (não escopo do projeto)')
    fatoresExternos = TextAreaField('Fatores externos')

    #Equipe
    nomeProfissional = SelectField('Nome Profissional', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
    vinculoINPE = StringField('Vinculo INPE')
    organizacoesExterna = SelectField('Organização Externa', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
    nomeProfissionalExterno = SelectField('Nome Profissional Externo', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])

    #Custos
    codigoAreaOrcamento = SelectField('Código da área orçamentária', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
    orcamentoProjeto = TextAreaField('Estruturado orçamento do projeto')
    custoEstimado = StringField('Custo total estimado(R$)')
    observacaoCustoEstimado = StringField('Observações sobre o Custo total estimado(R$)')
    disponibilidadeOrcamentaria = SelectField('Disponibilidade Orçamentária/Financeira e Parcerias Captação de Recursos Próprios', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
    valorDisponivel = StringField('Valor Disponível')
    instituicao = SelectField('Instituição', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])

    #Riscos
    riscosProjeto = TextAreaField('Riscos do Projeto')

    #Histórico
    evento = StringField('Evento')
    dataRegistro = DateField('Data do registro', format='%Y-%m-%d', validators=[Optional()])
    responsavelRegistro = SelectField('Responsável pelo registro', choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])

    salvar = SubmitField('Salvar')
