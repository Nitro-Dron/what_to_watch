# what_to_watch/opinions_app/__init__.py

import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Создаем экземпляр приложения
app = Flask(__name__)

# Настраиваем конфигурацию напрямую из переменных окружения
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URI', 'sqlite:///db.sqlite3')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DROPBOX_TOKEN'] = os.getenv('DROPBOX_TOKEN')

# Создаем экземпляры расширений
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# isort: off
# fmt: off

from . import cli_commands, error_handlers, views, models, forms
from . import api_views
# fmt: on
# isort: on
