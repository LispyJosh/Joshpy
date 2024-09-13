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

@app.route('/to-do')
def todo():
    return render_template('to-do.html')





