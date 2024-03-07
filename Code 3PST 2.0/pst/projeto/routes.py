from flask import (render_template, url_for, flash, redirect, Blueprint)
from pst.models import db, Projeto
from pst.projeto.forms import ProjetoForm

projeto = Blueprint('projeto', __name__)

@projeto.route("/listagemProjetos", methods=['GET'])
def listar_projetos():
    projeto = Projeto
    return render_template('listagemProjetos.html', title='Listagem de Projetos', projeto=projeto)

@projeto.route("/cadastrarProjeto", methods=['GET', 'POST'])
def novo_projeto():
    form = ProjetoForm()
    if form.validate_on_submit():
        projeto = Projeto(nomeProjeto=form.nomeProjeto.data, processoSEIProjeto=form.processoSEIProjeto.data)
        db.session.add(projeto)
        db.session.commit()
        flash('Projeto criado com sucesso!', 'success')
        return redirect(url_for('projeto.listar_projetos'))
    return render_template('cadastrarProjeto.html', title='Novo Projeto', form=form)