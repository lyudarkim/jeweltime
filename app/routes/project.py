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
    return project, 201


@projects_bp.route("/<projectId>", methods=['PUT'])
def update_one_account(projectId):
    request_body = request.get_json()
    request_project_id = int(projectId)

    if request_project_id != request_body["projectId"]:
        return {}, 401
    elif not "accountId" in request_body:
        return {}, 401
    else:
        print(f"Received body, {request_body} with project id: {projectId}")

        return request_body, 200

@projects_bp.route("/<project_id>", methods=["DELETE"])
def delete_one_project(project_id):

    return {"details": f'Project {project_id} successfully deleted'}, 200





