from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page (e.g., city.html)
@app.route('/') #@app.route('/') maps the root URL (i.e., http://localhost:5000/
@app.route('/city')
def city():
    return render_template('city.html')

# Route for the forest page (e.g., forest.html)
@app.route('/forest')
def forest():
    return render_template('forest.html')

# Route for the river page (e.g., river.html)
@app.route('/river')
def river():
    return render_template('river.html')

# Route for the seaside page (e.g., seaside.html)
@app.route('/seaside')
def seaside():
    return render_template('seaside.html')

# Route for the space page (e.g., space.html)
@app.route('/space')
def space():
    return render_template('space.html')

# Error handling for 404 Not Found
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handling for 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Run the app in debug mode
    app.run(debug=True)


#timer part goes here

from flask import jsonify

# Timer end point
@app.route('/timer-end', methods=['POST'])
def timer_end():
    return jsonify({"status": "success", "message": "Time's Up, Great Job!"})


# to-list

@app.route('/todo')
def todo():
    return render_template('todo.html')

from flask_sqlalchemy import SQLAlchemy

# Initialize the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/todo_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for To-Do items
class TodoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Task {self.id}: {self.task}>'

# Create the database
with app.app_context():
    db.create_all()


from flask import request, jsonify

@app.route('/add-todo', methods=['POST'])
def add_todo():
    task_data = request.json
    new_task = TodoItem(task=task_data['task'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"status": "success", "task": new_task.task})

@app.route('/get-todos', methods=['GET'])
def get_todos():
    todos = TodoItem.query.all()
    return jsonify([{"id": todo.id, "task": todo.task} for todo in todos])

@app.route('/delete-todo/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todo = TodoItem.query.get(id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
        return jsonify({"status": "success", "message": "Task deleted"})
    return jsonify({"status": "error", "message": "Task not found"}), 404

