
from flask import Flask
from flask_mongoengine import MongoEngine
from app.config import config


app = Flask(__name__)

app.config['MONGODB_DB'] = config.MONGODB_DB
app.config['MONGODB_HOST'] = config.MONGODB_HOST
app.config['MONGODB_PORT'] = config.MONGODB_PORT
app.config['MONGODB_USERNAME'] = config.MONGODB_USERNAME
app.config['MONGODB_PASSWORD'] = config.MONGODB_PASSWORD

db = MongoEngine(app)

from app.todo.controller import todo1

app.register_blueprint(todo1)

