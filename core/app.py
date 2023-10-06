from flask import Flask,Blueprint
from flask_sqlalchemy import SQLAlchemy
from models.books import *
from models.customers import *
from models.loans import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
db = SQLAlchemy(app)


book_blueprint = Blueprint('book', __name__)
customer_blueprint = Blueprint('customer', __name__)
loan_blueprint = Blueprint('loan', __name__)

app.register_blueprint(book_blueprint, url_prefix='/books')
app.register_blueprint(customer_blueprint, url_prefix='/customers')
app.register_blueprint(loan_blueprint, url_prefix='/loans')


