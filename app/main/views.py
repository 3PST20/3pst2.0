from flask import Response, render_template, url_for
import json

def init_app(app):
    @app.route("/")
    def index():
        return render_template("index.html")

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
        # proj_list = Projeto.query.all()
        # return render_template("listarprojeto.html", projetos=proj_list)  
        return render_template("listarprojeto.html")

def gera_response(status, nome_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_conteudo] = conteudo
    if(mensagem):
        body['mensagem'] = mensagem
    return Response(json.dumps(body), status=status, mimetype='application/json')