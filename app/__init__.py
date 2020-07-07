from flask import Flask
from flask_nav import Nav
from flask_bootstrap import Bootstrap
from config import Config
from app.nav import topbar
  

app = Flask(__name__)
app.config.from_object(Config)

bootstrap = Bootstrap(app)

from app import routes