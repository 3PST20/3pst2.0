from flask import render_template, request, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required
from pst2 import bcrypt, app
from pst2.models import db, Usuario
from pst2.views import gera_response

# Cadastrar
@app.route('/cadastraUsuario', methods=['POST'])
def cria_usuario():
    try:
        data = request.json
        nome = data.get('nome')
        email = data.get('email')
        tipoUsuario = data.get('tipoUsuario')
        senha = data.get('senha')

        if not senha:
            return gera_response(400, "usuario", {}, 'A senha não pode ser vazia')

        hashed_password = bcrypt.generate_password_hash(senha).decode('utf-8')
        usuario = Usuario(nome=nome, email=email, tipoUsuario=tipoUsuario, senha=hashed_password)
        db.session.add(usuario)
        db.session.commit()

        return gera_response(201, "usuario", usuario.to_json(), 'Salvo com sucesso')
    except Exception as e:
        print(e)
        db.session.rollback()
        return gera_response(400, "usuario", {}, 'Erro ao cadastrar')

@app.route('/login', methods=['POST', 'GET'])
def login():
    # return render_template("login.html")
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        usuario = Usuario.query.filter_by(email=email).first()

        if not usuario or not bcrypt.check_password_hash(usuario.senha, senha):
            return gera_response(401, 'usuario', {}, 'Email ou senha inválidos')
        
        login_user(usuario)
        return redirect(url_for('index'))
    return render_template("login.html")

# # Atualizar
# @app.route('/atualizaProjeto/<int:projeto_id>', methods=['PUT'])
# def atualiza_projeto(projeto_id):
#     try:
#         # Buscar projeto existente
#         projeto = Projeto.query.get(projeto_id)
#         if projeto is None:
#             return gera_response(404, "projeto", {}, 'Projeto não encontrado')

#         # Atualizar dados do projeto
#         projeto.nomeProjeto = request.form.get('nomeProjeto')
#         projeto.processoSEIProjeto = request.form.get('processoSEIProjeto')

#         # Atualizar dados do stakeholder associado
#         stakeholder = Stakeholder.query.filter_by(projeto_id=projeto.id).first()
#         if stakeholder is not None:
#             stakeholder.stk_parteInteressada = request.form.get('stk_parteInteressada')
#             stakeholder.stk_expectativa = request.form.get('stk_expectativa')
#             stakeholder.stk_requisito = request.form.get('stk_requisito')

#         db.session.commit()

#         return gera_response(200, "projeto", {"stakeholders": stakeholder.to_json()}, 'Salvo com sucesso')
#     except Exception as e:
#         print(e)
#         db.session.rollback()
#         return gera_response(400, "projeto", {}, 'Erro ao salvar')

# # Deletar
# @app.route('/deletaProjeto/<int:projeto_id>', methods=['DELETE'])
# def deleta_projeto(projeto_id):
#     try:
#         projeto = Projeto.query.get(projeto_id)
#         if projeto is None:
#             return gera_response(404, "projeto", {}, 'Projeto não encontrado')

#         db.session.delete(projeto)
#         db.session.commit()

#         return gera_response(200, "projeto", {}, 'Deletado com sucesso')
#     except Exception as e:
#         print(e)
#         db.session.rollback()
#         return gera_response(400, "projeto", {}, 'Erro ao deletar')
