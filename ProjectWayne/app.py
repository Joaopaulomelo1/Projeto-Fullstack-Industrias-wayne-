from flask import Flask
from extensions import db, login_manager

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'wayne-industries-gotham-secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wayne.db'

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from routes.auth import auth_bp
    from routes.resources import resources_bp
    from routes.dashboard import dashboard_bp
    from routes.users import users_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(resources_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(users_bp)

    with app.app_context():
        from models import User, Resource
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)