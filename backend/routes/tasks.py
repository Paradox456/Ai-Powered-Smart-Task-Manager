from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from database import db, Task

tasks_bp = Blueprint("tasks_bp", __name__)

# Create a Task
@tasks_bp.route("/tasks", methods=["POST"])
@jwt_required()
def create_task():
    data = request.get_json()
    title = data.get("title")
    description = data.get("description", "")
    priority = data.get("priority", "medium")

    if not title:
        return jsonify({"error": "Task title is required"}), 400

    current_user = get_jwt_identity()
    new_task = Task(title=title, description=description, priority=priority, user_id=current_user)

    db.session.add(new_task)
    db.session.commit()

    return jsonify({"message": "Task created successfully", "task": new_task.to_dict()}), 201

# Get All Tasks for Logged-in User
@tasks_bp.route("/tasks", methods=["GET"])
@jwt_required()
def get_tasks():
    current_user = get_jwt_identity()
    tasks = Task.query.filter_by(user_id=current_user).all()
    return jsonify([task.to_dict() for task in tasks]), 200

# Update a Task
@tasks_bp.route("/tasks/<int:task_id>", methods=["PUT"])
@jwt_required()
def update_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()
    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.priority = data.get("priority", task.priority)

    db.session.commit()
    return jsonify({"message": "Task updated successfully", "task": task.to_dict()}), 200

# Delete a Task
@tasks_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
@jwt_required()
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted successfully"}), 200

