from flask import Blueprint, jsonify, request
from app import db

from app.models.project import Project
from app.models.account import Account


accounts_bp = Blueprint("accounts", __name__, url_prefix="/accounts")


@accounts_bp.route("", methods=['POST'])
def create_account():
    request_body = request.get_json()
    try:
        new_account = Account(first_name=request_body["first_name"], last_name=request_body["last_name"], email=request_body["email"], zipcode=request_body["zipcode"])
    except KeyError:
        return {
            "details": "Invalid data"
            }, 400

    db.session.add(new_account)
    db.session.commit()

    return {"account": new_account.to_dict()}, 201