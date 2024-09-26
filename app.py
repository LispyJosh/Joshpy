from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Initialize the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mexicanroco98yt@localhost:5432/todo_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for To-Do items
class TodoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    eta = db.Column(db.String(50), nullable=True)
    priority = db.Column(db.String(20), nullable=True)
    due_date = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return f'<Task {self.id}: {self.task}>'


# Create the database
with app.app_context():
    db.create_all()

# Route for the home page (city.html)
@app.route('/')
@app.route('/city')
def city():
    return render_template('city.html')

# Route for the forest page
@app.route('/forest')
def forest():
    return render_template('forest.html')

# Route for the river page
@app.route('/river')
def river():
    return render_template('river.html')

# Route for the seaside page
@app.route('/seaside')
def seaside():
    return render_template('seaside.html')

# Route for the space page
@app.route('/space')
def space():
    return render_template('space.html')

# Route for the to-do page
@app.route('/todo')
def todo():
    return render_template('todo.html')

# Add a to-do item
@app.route('/add-todo', methods=['POST'])
def add_todo():
    task_data = request.json
    new_task = TodoItem(
        task=task_data['task'], 
        eta=task_data['eta'], 
        priority=task_data['priority'], 
        due_date=task_data['due_date']
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify({
        "status": "success", 
         "id": new_task.id,
        "task": new_task.task, 
        "eta": new_task.eta, 
        "priority": new_task.priority, 
        "due_date": new_task.due_date
    })

# Get all to-do items
@app.route('/get-todos', methods=['GET'])
def get_todos():
    todos = TodoItem.query.all()
    return jsonify([{
        "id": todo.id, 
        "task": todo.task, 
        "eta": todo.eta, 
        "priority": todo.priority, 
        "due_date": todo.due_date
    } for todo in todos])

# Delete a to-do item
@app.route('/delete-todo/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todo = TodoItem.query.get(id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
        return jsonify({"status": "success", "message": "Task deleted"})
    return jsonify({"status": "error", "message": "Task not found"}), 404

# Timer endpoint (placeholder for the timer feature)
@app.route('/timer-end', methods=['POST'])
def timer_end():
    return jsonify({"status": "success", "message": "Time's Up, Great Job!"})

# Error handling for 404 Not Found
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handling for 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
