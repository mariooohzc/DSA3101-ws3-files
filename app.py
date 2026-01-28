from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary in-memory storage for tasks
todos = [{"task": "Learn Flask", "done": False}, {"task": "Build a Docker Image", "done": False}]

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    todo = request.form.get('todo')
    if todo:
        todos.append({"task": todo, "done": False})
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(todos):
        todos.pop(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    # host="0.0.0.0" is critical for Docker to map ports correctly
    app.run(host="0.0.0.0", port=5000)
