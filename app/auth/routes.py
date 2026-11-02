from flask import Blueprint, render_template

bp_auth = Blueprint(
    'bp_auth',
    __name__,
    template_folder='templates'
)

@bp_auth.route('/')
def login():
    return render_template('login.html')

@bp_auth.route('/inicio')
def inicio():
    return render_template('index.html')