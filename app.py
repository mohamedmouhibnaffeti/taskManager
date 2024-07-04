from flask import Flask, render_template
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
def index(request):
    if request.method == 'POST':
        taskContent = request.form[('')]
    else:
        return render_template("index.html")

# Function to create all tables within the application context
def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    # Create all tables before running the app
    create_tables()
    app.run(debug=True)
