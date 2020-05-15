from flask import render_template

from app.todo.services import TodoService
from flask import Blueprint

todo1 = Blueprint('todo1', __name__)


@todo1.route("/")
def hello_world():
    homeActive = "active"
    return render_template('home.html', homeActive=homeActive)


@todo1.route("/todo")
def todo():
    result = TodoService.get_all_todos()
    todoActive = "active"
    return render_template("todo.html", todoActive=todoActive, result=result)



