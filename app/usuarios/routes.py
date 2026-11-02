from flask import Blueprint, render_template

bp_usuario = Blueprint(
    'bp_usuario',
    __name__,
    template_folder='templates'
)

# Consultar usuarios
@bp_usuario.route('/usuarios')
def index():
    return render_template('usuario/index.html')

# Registrar usuario
@bp_usuario.route('/usuarios/create')
def create():
    return render_template('usuario/create.html')

# Modificar usuario
@bp_usuario.route('/usuarios/edit/<int:id>')
def edit(id):
    return render_template('usuario/edit.html')

# Eliminar usuario
@bp_usuario.route('/usuarios/delete/<int:id>')
def delete(id):
    return render_template('usuario/elimin.html')