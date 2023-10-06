from create_db import create_library_database 

# create_library_database()

from flask import Flask


app = Flask(__name__)

from models.books import books_blueprint
from models.customers import customers_blueprint
from models.customers import customers_blueprint

app.register_blueprint(books_blueprint)
app.register_blueprint(customers_blueprint)



