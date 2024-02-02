from pst2.resourcesProjeto import stakeholderProjeto, projeto
from pst2.resourcesUsuario import usuario

def init_app(app):
    stakeholderProjeto.init_app(app)
    projeto.init_app(app)
    usuario.init_app(app)