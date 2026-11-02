from flask import Blueprint, render_template

bp_categoria = Blueprint(
    'bp_categoria',
    __name__,
    template_folder='templates'
)

@bp_categoria.route('/categorias')
def index():
    return render_template('categoria/index.html')

@bp_categoria.route('/categorias/create')
def create():
    return render_template('categoria/create.html')

@bp_categoria.route('/categorias/edit/<int:id>')
def edit(id):
    return render_template('categoria/edit.html')

@bp_categoria.route('/categorias/delete/<int:id>')
def delete(id):
    return render_template('categoria/elimin.html')
