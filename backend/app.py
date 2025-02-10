from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import datetime

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configure Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'supersecretkey'

# Initialize Extensions
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    priority = db.Column(db.String(20), nullable=False)
    due_date = db.Column(db.String(20), nullable=False)

# Routes
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    new_user = User(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and user.password == data['password']:
        access_token = create_access_token(identity=user.id, expires_delta=datetime.timedelta(days=1))
        return jsonify({'access_token': access_token})
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/tasks', methods=['GET', 'POST'])
@jwt_required()
def tasks():
    user_id = get_jwt_identity()
    if request.method == 'POST':
        data = request.json
        new_task = Task(user_id=user_id, title=data['title'], priority=data['priority'], due_date=data['due_date'])
        db.session.add(new_task)
        db.session.commit()
        return jsonify({'message': 'Task added successfully'}), 201
    tasks = Task.query.filter_by(user_id=user_id).all()
    return jsonify([{'id': t.id, 'title': t.title, 'priority': t.priority, 'due_date': t.due_date} for t in tasks])

@app.route('/tasks/<int:task_id>', methods=['PUT', 'DELETE'])
@jwt_required()
def update_delete_task(task_id):
    user_id = get_jwt_identity()
    task = Task.query.filter_by(id=task_id, user_id=user_id).first()
    if not task:
        return jsonify({'message': 'Task not found'}), 404
    if request.method == 'PUT':
        data = request.json
        task.title = data.get('title', task.title)
        task.priority = data.get('priority', task.priority)
        task.due_date = data.get('due_date', task.due_date)
        db.session.commit()
        return jsonify({'message': 'Task updated successfully'})
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted successfully'})

# Initialize Database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    with app.app_context():  # Ensure Flask has an application context
        db.create_all()  # Initialize database tables
    app.run(debug=True)

