from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        taskContent = request.form['content']
        newTask = Todo(content=taskContent)
        try:
            db.session.add(newTask)
            db.session.commit()
            return redirect('/')
        except:
            return "Error creating task"
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template("index.html", tasks=tasks)

@app.route("/delete/<int:id>")
def deleteTask(id):
    taskToDelete = Todo.query.get_or_404(id)
    try:
        db.session.delete(taskToDelete)
        db.session.commit()
        return redirect('/')
    except:
        return "Error deleting task"

@app.route("/update/<int:id>", methods=['GET', 'POST'])
def updateTask(id):
    return ''

def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    create_tables()
    app.run(debug=True)
