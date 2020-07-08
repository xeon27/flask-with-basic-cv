from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
  

app = Flask(__name__)
app.config.from_object(Config)

from app.main import bp as main_bp
from app.errors import bp as errors_bp

app.register_blueprint(main_bp)
app.register_blueprint(errors_bp)

bootstrap = Bootstrap(app)