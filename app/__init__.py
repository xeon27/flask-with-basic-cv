from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
  

bootstrap = Bootstrap()


def create_app(config_class=Config):
    # Create flask app instance
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Attach bootstrap
    bootstrap.init_app(app)

    # Register blueprints
    from app.main import bp as main_bp
    from app.errors import bp as errors_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(errors_bp)

    
    return app