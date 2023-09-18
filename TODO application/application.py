from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
todos = []


@app.route('/')
def index():
    return render_template('index.html', todos=todos)


@app.route('/add', methods=['POST'])
def add_todo():
    description = request.form.get('description')
    date = request.form.get('date')
    completed = False
    todo = {'description': description, 'date': date, 'completed': completed}
    todos.append(todo)
    return redirect(url_for('index'))


@app.route('/remove_completed', methods=['POST'])
def remove_completed():
    global todos
    todos = [todo for todo in todos if not todo['completed']]
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
