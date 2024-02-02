from flask import render_template, request
from pst2.models import Stakeholder, db
from pst2.views import gera_response

def init_app(app):
    #método para cadastrar o stakeholder
    @app.route('/cadastraStakeholder', methods=['POST'])
    def cria_stakeholder():
        #variaveis conforme o models
        stk_nome = request.form.get('stk_nome')
        stk_expectativa = request.form.get('stk_expectativa')
        stk_requisito = request.form.get('stk_requisito')

        try:
            stk = Stakeholder(stk_nome=stk_nome, stk_expectativa=stk_expectativa, stk_requisito=stk_requisito)
            db.session.add(stk)
            db.session.commit()

            return gera_response(201, "stakeholder", stk.to_json(), 'Salvo com sucesso')
        except Exception as e:
            print(e)
            db.session.rollback()
            return gera_response(400, "stakeholder", {}, 'Erro ao cadastrar')
