from flask import Response, render_template, url_for
from pst2 import app
import json
from pst2.models import Projeto, Stakeholder

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

# @app.route("/login")
# def login():
#     return render_template("login.html")

@app.route("/cadastrarconta")
def cadConta():
    return render_template("cadastrarconta.html")

@app.route("/detalhesperfil")
def detalhesPefil():
    return render_template("detalhesperfil.html")

@app.route("/cadastrarprojeto")
def cadProjeto():
    return render_template("cadastrarprojeto.html")

@app.route("/cadastrarprograma")
def cadPrograma():
    return render_template("cadastrarprograma.html")

@app.route("/cadastrarservico")
def cadServico():
    return render_template("cadastrarservico.html")

@app.route("/cadastrarcolaboradorinpe")
def cadColaboradorInpe():
    return render_template("cadastrarcolaboradorinpe.html")

@app.route("/cadastrarcolaboradorexterno")
def cadColaboradorExterno():
    return render_template("cadastrarcolaboradorexterno.html")

@app.route("/cadastrarorganizacaoexterna")
def cadOrganizacao():
    return render_template("cadastrarorganizacaoexterna.html")

@app.route("/listarprograma")
def lisPrograma():
    return render_template("listarprograma.html")

@app.route("/listarservico")
def lisServico():
    return render_template("listarservico.html")

@app.route("/catalogodeiniciativasinstitucionais")
def catalogoIniciativas():
    return render_template("catalogodeiniciativasinstitucionais.html")

@app.route("/projetosxprogramas")
def projetosxprogramas():
    return render_template("projetosxprogramas.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/listarprojeto", methods=['GET'])
def seleciona_projetos():
    proj_list = Projeto.query.all()
    return render_template("listarprojeto.html", projetos=proj_list)  
    # return render_template("listarprojeto.html")

@app.route("/atualizarprojeto/<id>", methods=['GET', 'POST'])
def atualiza_Projeto(id):
    projeto_list = Projeto.query.filter_by(id=id).first()
    stk_list = Stakeholder.query.filter_by(projeto_id=id).first()
    return render_template("atualizarprojeto.html", projeto=projeto_list, stakeholder=stk_list) 

@app.route("/novoProjeto/<id>", methods=['GET', 'POST'])
def novo_Projeto(id):
    projeto_list = Projeto.query.filter_by(id=id).first()
    stk_list = Stakeholder.query.filter_by(projeto_id=id).first()
    return render_template("cadastrarprojeto.html", projeto=projeto_list, stakeholder=stk_list) 

def gera_response(status, nome_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_conteudo] = conteudo
    if(mensagem):
        body['mensagem'] = mensagem
    return Response(json.dumps(body), status=status, mimetype='application/json')