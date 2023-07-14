from flask import Blueprint, jsonify, request
from app import db

from app.models.project import Project
from app.models.account import Account


projects_bp = Blueprint("projects", __name__, url_prefix="/projects")


@projects_bp.route("", methods=['POST'])
def create_project():
    request_body = request.get_json()
    try:
        new_project = Project(project_name=request_body["project_name"], description=request_body["description"], started_at=request_body["started_at"], hours_spent=request_body["hours_spent"], materials_cost=request_body["materials_cost"], materials=request_body["materials"], metals=["metals"], gemstones=request_body["gemstones"], shape=request_body["shape"], jewelry_type=request_body["jewelry_type"])
    except KeyError:
        return {
            "details": "Invalid data"
            }, 400

    db.session.add(new_project)
    db.session.commit()

    return {"account": new_project.to_dict()}, 201


