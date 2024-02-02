from flask import render_template, request
from pst2 import app
from pst2.models import db, Projeto, Stakeholder
from pst2.views import gera_response

def cadastrar_projeto(request):
    nomeProjeto = request.form.get('nomeProjeto')
    processoSEIProjeto = request.form.get('processoSEIProjeto')

    projeto = Projeto(nomeProjeto=nomeProjeto, processoSEIProjeto=processoSEIProjeto)
    db.session.add(projeto)
    db.session.commit()  # Commit antes de acessar o ID

    return projeto

# Cadastrar
@app.route('/cadastroProjeto', methods=['POST'])
# @app.route('/novoProjeto/<int:projeto_id>', methods=['POST'])
def cria_projeto():
    try:
        projeto = cadastrar_projeto(request)

        # Acessar o ID do projeto após o commit
        projeto_id = projeto.id

        # Parâmetros stakeholders
        stakeholder_params = {
            'projeto_id': projeto_id,
            'stk_parteInteressada': request.form.get('stk_parteInteressada'),
            'stk_expectativa': request.form.get('stk_expectativa'),
            'stk_requisito': request.form.get('stk_requisito')
        }
        stakeholder = Stakeholder(**stakeholder_params)
        db.session.add(stakeholder)
        db.session.commit()

        # Incluir o ID do projeto no JSON
        response_data = {
            "projeto": {
                "id": projeto_id,
                "stakeholders": stakeholder.to_json()
            },
            "mensagem": "Salvo com sucesso"
        }

        return gera_response(201, "projeto", response_data, 'Salvo com sucesso')
    except Exception as e:
        print(e)
        db.session.rollback()
        return gera_response(400, "projeto", {}, 'Erro ao cadastrar')

# Cadastrar atrvés da listagem
@app.route('/novoProjeto/<int:projeto_id>', methods=['POST'])
def novo_projeto(projeto_id):
    try:
        # projeto = cadastrar_projeto(request)
        cria_projeto(projeto_id)

    except Exception as e:
        print(e)
        db.session.rollback()
        return gera_response(400, "projeto", {}, 'Erro ao cadastrar')


# Atualizar
@app.route('/atualizaProjeto/<int:projeto_id>', methods=['PUT'])
def atualiza_projeto(projeto_id):
    try:
        # Buscar projeto existente
        projeto = Projeto.query.get(projeto_id)
        if projeto is None:
            return gera_response(404, "projeto", {}, 'Projeto não encontrado')

        # Atualizar dados do projeto
        projeto.nomeProjeto = request.form.get('nomeProjeto')
        projeto.processoSEIProjeto = request.form.get('processoSEIProjeto')

        # Atualizar dados do stakeholder (FK)
        stakeholder = Stakeholder.query.filter_by(projeto_id=projeto.id).first()
        if stakeholder is not None:
            stakeholder.stk_parteInteressada = request.form.get('stk_parteInteressada')
            stakeholder.stk_expectativa = request.form.get('stk_expectativa')
            stakeholder.stk_requisito = request.form.get('stk_requisito')

        db.session.commit()

        return gera_response(200, "projeto", {"stakeholders": stakeholder.to_json()}, 'Salvo com sucesso')
    except Exception as e:
        print(e)
        db.session.rollback()
        return gera_response(400, "projeto", {}, 'Erro ao salvar')

# Deletar
@app.route('/deletaProjeto/<int:projeto_id>', methods=['DELETE'])
def deleta_projeto(projeto_id):
    try:
        projeto = Projeto.query.get(projeto_id)
        if projeto is None:
            return gera_response(404, "projeto", {}, 'Projeto não encontrado')

        db.session.delete(projeto)
        db.session.commit()

        return gera_response(200, "projeto", {}, 'Deletado com sucesso')
    except Exception as e:
        print(e)
        db.session.rollback()
        return gera_response(400, "projeto", {}, 'Erro ao deletar')
