from flask import (render_template, url_for, flash, redirect,
                    request, abort, Blueprint)
from pst import db
from pst.models import Alinhamento1, Alinhamento2, Custos, DescricaoDetalhada, Equipe, Escopo, GeracaoImpacto, Historico, Projeto, Riscos, Stakeholder, Identificacao
from pst.projeto.forms import ProjetoForm
from datetime import datetime

projeto = Blueprint('projeto', __name__)

@projeto.route("/listagemProjetos", methods=['GET'])
def listar_projetos():
    """
    Retorna uma página HTML com a listagem de projetos.
    Autor: Ana Carolina das Neves
    Data: 22/03/2024

    :return: Página HTML com a listagem de projetos.
    :rtype: flask.Response
    """
    projeto = Projeto
    return render_template('listagemProjetos.html', title='Listagem de Projetos', projeto=projeto)

def cadastrar_projeto(form):
    projeto = Projeto(nomeProjeto=form.nomeProjeto.data, processoSEIProjeto=form.processoSEIProjeto.data, responsavelProjeto=form.responsavelProjeto.data, 
                      unidadeResponsavel=form.unidadeResponsavel.data, unidadeExecutora=form.unidadeExecutora.data, categoriaProjeto=form.categoriaProjeto.data, 
                      situacaoProjeto=form.situacaoProjeto.data, situacaoTAP=form.situacaoTAP.data)
    db.session.add(projeto)
    db.session.commit()  # Commit antes de acessar o ID

    return projeto

@projeto.route("/cadastrarProjeto", methods=['GET', 'POST'])
def novo_projeto():
    """
    Rota para cadastrar um novo projeto.

    Método GET: Retorna o formulário para cadastrar um novo projeto.
    Método POST: Processa o formulário submetido para cadastrar o projeto.

    :return: Página HTML para cadastrar um novo projeto ou redireciona para a listagem de projetos após o cadastro.
    :rtype: flask.Response
    """
    form = ProjetoForm()
    if form.validate_on_submit():
        projeto = cadastrar_projeto(form)
        
        # Parâmetros Identificação
        identificacao_params = {
            'projeto_id': projeto.id,
            'protocoloSEIUltimoTAP': form.protocoloSEIUltimoTAP.data,
            'programaAssociado': form.programaAssociado.data,
            'processoSEIPrograma': form.processoSEIPrograma.data,
            'duracaoEstimadaProjeto': form.duracaoEstimadaProjeto.data,
            'dataInicioProjeto': form.dataInicioProjeto.data,
            'dataConclusaoProjeto': form.dataConclusaoProjeto.data,
            'aprovacaoUORG': form.aprovacaoUORG.data,
            'aprovacaoPortfolio': form.aprovacaoPortfolio.data,
            'carregamentoSIGE3P': form.carregamentoSIGE3P.data,
            'objetoProjeto': form.objetoProjeto.data,
            'descricaoProjeto': form.descricaoProjeto.data,
            'prioridadeINPE': form.prioridadeINPE.data,
            'evidenciaPriorizacao': form.evidenciaPriorizacao.data,
            'tipoParceria': form.tipoParceria.data,
            'situacaoParceria': form.situacaoParceria.data,
            'processoSEIParceria': form.processoSEIParceria.data,
            'propriedadeIntelectual': form.propriedadeIntelectual.data,
            'faixaCustoTotalProjeto': form.faixaCustoTotalProjeto.data,
            'recursosFinanceiros': form.recursosFinanceiros.data
        }
        
        identificacao = Identificacao(**identificacao_params)
        db.session.add(identificacao)

        #paramêtros alinhamento 1
        alinha1_params = {
            'projeto_id': projeto.id,
            'objetivosEstrategicos': form.objetivosEstrategicos.data,
            'metasEstrategicas': form.metasEstrategicas.data,
            'periodoAlinha1': form.periodoAlinha1.data,
            'politicaNacional': form.politicaNacional.data,
            'programaPPA': form.programaPPA.data,
            'periodoProgramaPPA': form.periodoProgramaPPA.data,
            'evidenciaAlinha1ProgramaPPA': form.evidenciaAlinha1ProgramaPPA.data,
            'objetivoPPA': form.objetivoPPA.data,
            'periodoObjetivoPPA': form.periodoObjetivoPPA.data,
            'evidenciaAlinha1ObjetivoPPA': form.evidenciaAlinha1ObjetivoPPA.data,
        }
        alinha1 = Alinhamento1(**alinha1_params)
        db.session.add(alinha1)

        #paramêtros alinhamento 2
        alinha2_params = {
            'projeto_id': projeto.id,
            'areaPrioritariaENCTI': form.areaPrioritariaENCTI.data,
            'periodoAlinha2': form.periodoAlinha2.data,
            'evidenciaAlinha2AreaPrioritaria': form.evidenciaAlinha2AreaPrioritaria.data,
            'objetivosDesenvolvimento': form.objetivosDesenvolvimento.data,
            'evidenciaAlinha2Objetivos': form.evidenciaAlinha2Objetivos.data,
            'mapaEstrategico': form.mapaEstrategico.data,
            'evidenciaAlinha2MapaEstrategico': form.evidenciaAlinha2MapaEstrategico.data,
            'eixosDiretrizesEstrategia': form.eixosDiretrizesEstrategia.data,
            'evidenciaAlinha2EixosDiretrizes': form.evidenciaAlinha2EixosDiretrizes.data,
            'areaTematicaMCTI': form.areaTematicaMCTI.data,
            'evidenciaAlinha2AreaTematica': form.evidenciaAlinha2AreaTematica.data,
            'areaTecnologiasPrioritarias': form.areaTecnologiasPrioritarias.data,
            'evidenciaAlinha2AreaTecnologias': form.evidenciaAlinha2AreaTecnologias.data,
            'politicasPublicas': form.politicasPublicas.data,
            'outrasPoliticasPublicas': form.outrasPoliticasPublicas.data,
            'evidenciaAlinha2OutrasPoliticasPublicas': form.evidenciaAlinha2OutrasPoliticasPublicas.data,
            'impactado': form.impactado.data,
            'justificativa': form.justificativa.data,
            'estrategia': form.estrategia.data
        }
        alinha2 = Alinhamento2(**alinha2_params)
        db.session.add(alinha2)

        #paramêtros geração impacto
        gera_impacto_params = {
            'projeto_id': projeto.id,
            'perspectivaPopulacao': form.perspectivaPopulacao.data,
            'missaoMCTI': form.missaoMCTI.data,
            'perspectivaGestaoMCTI': form.perspectivaGestaoMCTI.data,
            'perspectivaGestaoINPE': form.perspectivaGestaoINPE.data,
            'perspectivaUORG': form.perspectivaUORG.data,
            'perspectivaOrgaos': form.perspectivaOrgaos.data,
            'metasPoliticasPublicas': form.metasPoliticasPublicas.data
        }
        gera_impacto = GeracaoImpacto(**gera_impacto_params)
        db.session.add(gera_impacto)

        #paramêtros descrição detalhada
        descri_detalhe_params = {
            'projeto_id': projeto.id,
            'descricaoProdutosServicos': form.descricaoProdutosServicos.data,
            'justificativaDescricao': form.justificativaDescricao.data,
            'resultadosEsperados': form.resultadosEsperados.data,
            'capacidadeTecnica': form.capacidadeTecnica.data,
            'publicoAlvo': form.publicoAlvo.data,
            'objetivoGeral': form.objetivoGeral.data,
            'objetivosEspecificos': form.objetivosEspecificos.data,
            'metasProjetoCriterios': form.metasProjetoCriterios.data,
            'trlAtual': form.trlAtual.data,
            'trlEsperado': form.trlEsperado.data,
            'trlFinal': form.trlFinal.data,
            'requisitosEncerramento': form.requisitosEncerramento.data,
            'sustentabilidade': form.sustentabilidade.data,
            'objetivoDescricao': form.objetivoDescricao.data,
            'descricaoCatalogoInstitucional': form.descricaoCatalogoInstitucional.data
        }
        descri_detalhe = DescricaoDetalhada(**descri_detalhe_params)
        db.session.add(descri_detalhe)

        # Parâmetros Stakeholders
        stakeholder_params = {
            'projeto_id': projeto.id,
            'stk_parteInteressada': form.stk_parteInteressada.data,
            'stk_expectativa': form.stk_expectativa.data,
            'stk_requisito': form.stk_requisito.data
        }
        stakeholder = Stakeholder(**stakeholder_params)
        db.session.add(stakeholder)

        #paramêtros escopo
        escopo_params = {
            'projeto_id': projeto.id,
            'premissasProjeto': form.premissasProjeto.data,
            'restricoesProjeto': form.restricoesProjeto.data,
            'escopoProjeto': form.escopoProjeto.data,
            'exclusoesProjeto': form.exclusoesProjeto.data,
            'fatoresExternos': form.fatoresExternos.data
        }
        escopo = Escopo(**escopo_params)
        db.session.add(escopo)

        #paramêtros equipe
        equipe_params = {
            'projeto_id': projeto.id,
            'nomeProfissional': form.nomeProfissional.data,
            'vinculoINPE': form.vinculoINPE.data,
            'organizacoesExterna': form.organizacoesExterna.data,
            'nomeProfissionalExterno': form.nomeProfissionalExterno.data
        }
        equipe = Equipe(**equipe_params)
        db.session.add(equipe)

        #paramêtros custos e plano orçamentário
        custos_params = {
            'projeto_id': projeto.id,
            'codigoAreaOrcamento': form.codigoAreaOrcamento.data,
            'orcamentoProjeto': form.orcamentoProjeto.data,
            'custoEstimado': form.custoEstimado.data,
            'observacaoCustoEstimado': form.observacaoCustoEstimado.data,
            'disponibilidadeOrcamentaria': form.disponibilidadeOrcamentaria.data,
            'valorDisponivel': form.valorDisponivel.data,
            'instituicao': form.instituicao.data,
        }
        custos = Custos(**custos_params)
        db.session.add(custos)
        
        #paramêtros riscos
        riscos_params = {
            'projeto_id': projeto.id,
            'riscosProjeto': form.riscosProjeto.data
        }
        riscos = Riscos(**riscos_params)
        db.session.add(riscos)

        #paramêtros histórico
        historico_params = {
            'projeto_id': projeto.id,
            'evento': form.evento.data,
            'dataRegistro': form.dataRegistro.data,
            'responsavelRegistro': form.responsavelRegistro.data
        }
        historico = Historico(**historico_params)
        db.session.add(historico)
        
        db.session.commit()
        flash('Projeto criado com sucesso!')
        return redirect(url_for('projeto.listar_projetos'))
    return render_template('cadastrarProjeto.html', title='Novo Projeto', form=form)