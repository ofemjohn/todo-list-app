from flask import Flask, jsonify, request
from database.db import DB, db
from database.models import Todo

app = Flask(__name__)
DB = DB(app)


# Create endpoint to add a new todo

@app.route('/api/todos', methods=['POST'])
def add_todo():
    data = request.json

    # Check for required fields
    required_fields = ['title', 'content', 'completed']
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        return jsonify({'message': f"Missing required fields: {', '.join(missing_fields)}"}), 400  # Bad request

    new_todo = Todo(
        title=data['title'],
        content=data['content'],
        completed=data['completed']
    )

    # Ensure the database session is available during the operation
    with app.app_context():
        DB.save(new_todo)
        return jsonify({'message': 'Todo created successfully', 'todo': new_todo.as_dict()}), 201


# Create endpoint to get all todos


@app.route('/api/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    todo_list = [todo.as_dict() for todo in todos]
    return jsonify({'todos': todo_list})

# Create endpoint to get a specific todo by ID


@app.route('/api/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if todo:
        return jsonify(todo.as_dict())
    else:
        return jsonify({'error': 'Todo not found'}), 404

# Create endpoint to update a todo by ID


@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404

    data = request.json

    todo.title = data.get('title', todo.title)
    todo.content = data.get('content', todo.content)
    todo.completed = data.get('completed', todo.completed)

    DB.save(todo)
    return jsonify({'message': 'Todo updated successfully', 'todo': todo.as_dict()})

# Create endpoint to delete a todo by ID


@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404

    DB.delete(todo)
    return jsonify({'message': 'Todo deleted successfully'})


if __name__ == '__main__':
    DB.create_all()
    app.run(debug=True, port=5000)
