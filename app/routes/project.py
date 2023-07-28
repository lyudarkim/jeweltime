from flask import Blueprint, jsonify, request
from app import db

from app.models.project import Project
from app.models.account import Account


projects_bp = Blueprint("projects", __name__, url_prefix="/projects")

@projects_bp.route("", methods=['POST'])
def create_project():
    print("Inside create project@@@@@@@@@")
    ACCOUNT_ID = "accountId"
    request_body = request.get_json()
    #request_account_id = int(accountId)
    if not ACCOUNT_ID in request_body:
        return {}, 400
    
    project = {
        "accountId": request_body[ACCOUNT_ID],
        "projectId": 111,
        "projectName": request_body["projectName"],
        "description": request_body["description"],
        "startedAt": request_body["startedAt"],
        "completedAt": request_body["completedAt"],
        "hoursSpent": request_body["hoursSpent"],
        "materialsCost": request_body["materialsCost"],
        "materials": request_body["materials"],
        "metals": request_body["metals"],
        "gemstones": request_body["gemstones"],
        "shape": request_body["shape"],
        "jewelryType": request_body["jewelryType"],
        "notes": request_body["notes"]
    }
    return {"project": project}, 201


@projects_bp.route("", methods=['GET'])
def get_projects():

    ACCOUNT_ID = "accountId"
    request_body = request.get_json()

    if not ACCOUNT_ID in request_body:
        return {}, 400

    projects = [
            {
            "accountId": request_body[ACCOUNT_ID],
            "projectId": 111,
            "projectName": "ring",
            "description": "ring with diamonds",
            "startedAt": "01/01/23",
            "completedAt": "01/03/23",
            "hoursSpent": 30,
            "materialsCost": 100,
            "materials": "gold, diamonds",
            "metals": "gold",
            "gemstones": "diamonds",
            "shape": "circular",
            "jewelryType": "ring",
            "notes": "None"
            },
            {
            "accountId": request_body[ACCOUNT_ID],
            "projectId": 112,
            "projectName": "chain",
            "description": "golfen necklace",
            "startedAt": "01/04/23",
            "completedAt": "01/07/23",
            "hoursSpent": 30,
            "materialsCost": 100,
            "materials": "gold",
            "metals": "gold",
            "gemstones": "none",
            "shape": "string",
            "jewelryType": "necklace",
            "notes": "none"
            }
        ]

    return {"projects": projects}, 200


# @projects_bp.route("/<project_id>", methods=["DELETE"])
# def delete_one_project(project_id):
    
#     id = int(project_id)
#     project_to_delete: Project.query.get(id)

    # db.session.delete(project_to_delete)
    # db.session.commit()

    # project_name = project_to_delete.project_name

    # return {"details": f'Project {project_id} "{project_name}" successfully deleted'}, 200





