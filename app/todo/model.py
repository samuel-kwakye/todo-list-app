from app.application import db
import datetime

class Todo(db.Document):
    """Class for Todo Model"""
    name = db.StringField(required=True)
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<Todo %r>' % self.id

    def to_dict(self):

        dict_obj = {}

        for column, value in self._fields.items():
            dict_obj[column] = getattr(self, column)

        if "id" in dict_obj:
            dict_obj["id"] = str(dict_obj["id"])

        return dict_obj
