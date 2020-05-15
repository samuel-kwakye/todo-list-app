from app.todo.model import Todo

class TodoService:

    @staticmethod
    def get_all_todos():
        try:
            todo_data = Todo.objects
        except Exception as ex:
            print("Exception Occurred | {0}".format(str(ex)))
        return todo_data
