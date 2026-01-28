import redis
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Connect to Redis. Hostname is 'redis' because that's the service name in our compose file.
db = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def index():
    # Fetch all tasks from a Redis list named 'todos'
    todos = db.lrange('todos', 0, -1)
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    todo = request.form.get('todo')
    if todo:
        db.rpush('todos', todo) # Add to the end of the Redis list
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete(index):
    # Get the value at that index and remove it
    todo_val = db.lindex('todos', index)
    if todo_val:
        db.lrem('todos', 1, todo_val)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
