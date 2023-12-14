from ..resourcesProjeto import stakeholderProjeto, projeto

def init_app(app):
    stakeholderProjeto.init_app(app)
    projeto.init_app(app)