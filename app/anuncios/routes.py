from flask import Blueprint, render_template

bp_anuncio = Blueprint(
    'bp_anuncio',
    __name__,
    template_folder='templates'
)

@bp_anuncio.route('/anuncios')
def index():
    return render_template('anuncio/index.html')

@bp_anuncio.route('/anuncios/create')
def create():
    return render_template('anuncio/create.html')

@bp_anuncio.route('/anuncios/edit/<int:id>')
def edit(id):
    return render_template('anuncio/edit.html')

@bp_anuncio.route('/anuncios/delete/<int:id>')
def delete(id):
    return render_template('anuncio/elimin.html')