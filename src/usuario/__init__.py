from flask import Blueprint

iniciousuario = Blueprint('iniciousuario', __name__, url_prefix='/usuario', template_folder='templates')

evaluacion = Blueprint('evaluacion', __name__, url_prefix='/usuario', template_folder='templates')

informacion = Blueprint('informacion', __name__, url_prefix='/usuario', template_folder='templates')

lista = Blueprint('lista', __name__, url_prefix='/usuario', template_folder='templates')

avance = Blueprint('avance', __name__, url_prefix='/usuario', template_folder='templates')

promedio = Blueprint('promedio', __name__, url_prefix='/usuario', template_folder='templates')

relacion = Blueprint('relacion', __name__, url_prefix='/usuario', template_folder='templates')

from . import routes