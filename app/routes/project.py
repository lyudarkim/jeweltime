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

    return {"project": new_project.to_dict()}, 201


@projects_bp.route("", methods=['GET'])
def get_projects():

    projects = Project.query.all()

    projects_response = [project.to_dict() for project in projects]
    return jsonify(projects_response), 200


@projects_bp.route("/<project_id>", methods=["DELETE"])
def delete_one_project(project_id):
    
    id = int(project_id)
    project_to_delete: Project.query.get(id)

    db.session.delete(project_to_delete)
    db.session.commit()

    project_name = project_to_delete.project_name

    return {"details": f'Project {project_id} "{project_name}" successfully deleted'}, 200





