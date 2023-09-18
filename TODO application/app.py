from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Dictionary to store todo items with dates
todo_list = {}

@app.route('/')
def index():
    return render_template('index.html', todo_list=todo_list)

@app.route('/add', methods=['POST'])
def add():
    todo_item = request.form['todo_item']
    date_added = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if date_added not in todo_list:
        todo_list[date_added] = []

    todo_list[date_added].append({'task': todo_item, 'completed': False})
    return redirect(url_for('index'))

@app.route('/remove', methods=['POST'])
def remove():
    completed_tasks = request.form.getlist('completed_task')
    for task in completed_tasks:
        date, index = task.split('|')
        todo_list[date][int(index)]['completed'] = True

    # Remove completed tasks
    for date in list(todo_list.keys()):
        todo_list[date] = [task for task in todo_list[date] if not task['completed']]

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
