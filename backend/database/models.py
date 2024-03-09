from datetime import datetime
from database.db import db


class Todo(db.Model):
    """Todo model representing a todo item in the database."""

    __tablename__ = 'todo'

    # Columns for the 'todo' table
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=True)
    completed = db.Column(db.Boolean, default=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        """String representation of the Todo model."""
        return f"<TodoItem {self.title}>"

    def as_dict(self):
        """Return a dictionary representation of the Todo model."""
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'completed': self.completed,
            'created': self.created.isoformat(),  # Convert datetime to ISO format
        }
