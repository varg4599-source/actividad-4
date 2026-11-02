from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():

    app = Flask(__name__, template_folder='templates')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bd_anuncios.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from app.auth.routes import bp_auth
    from app.usuarios.routes import bp_usuario
    from app.categorias.routes import bp_categoria
    from app.anuncios.routes import bp_anuncio
    app.register_blueprint(bp_auth)
    app.register_blueprint(bp_usuario)
    app.register_blueprint(bp_categoria)
    app.register_blueprint(bp_anuncio)

    return app