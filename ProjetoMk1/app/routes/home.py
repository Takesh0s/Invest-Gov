from flask import Blueprint, render_template

bp = Blueprint('home_blueprint', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@bp.route('/detalhe')
def detalhe():
    return render_template('detalhe.html')

@bp.route('/detalhes')
def detalhes():
    return render_template('detalhes.html')