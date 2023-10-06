from flask_sqlalchemy import SQLAlchemy
from core.app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
db = SQLAlchemy(app)