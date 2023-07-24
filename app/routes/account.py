from flask import Blueprint, jsonify, request
from app import db

from app.models.project import Project
from app.models.account import Account


accounts_bp = Blueprint("accounts", __name__, url_prefix="/accounts")


@accounts_bp.route("", methods=['POST'])
def create_account():
    print(f"@@@@@@@@@@@@@@@@@ {request}")
    request_body = request.get_json()
    print(f"request body: {request_body}")
    # try:
    #     new_account = Account(first_name=request_body["first_name"], 
    #         last_name=request_body["last_name"], email=request_body["email"], 
    #         zipcode=request_body["zipcode"])
    # except KeyError:
    #     return {
    #         "details": "Invalid data"
    #         }, 400

    # db.session.add(new_account)
    # db.session.commit()

    # return {"account": new_account.to_dict()}, 201
    account = {
        "first_name": "Angie",
        "last_name": "Contreras",
        "email": "gjhgdjhg@fgsj.com",
        "zipcode": 98011
    }

    return {"account": account}, 201


@accounts_bp.route("", methods=['GET'])
def get_accounts():

    accounts = Account.query.all()

    accounts_response = [account.to_dict() for account in accounts]
    return jsonify(accounts_response), 200


@accounts_bp.route("/<account_id>", methods=['PUT'])
def update_one_account(account_id):

    request_body = request.get_json()
    if not "email" in request_body:
        return {}, 400
    else:
        print(f"Received body, {request_body} with account id: {account_id}")
        print("Email updated")
        return {"account": request_body}, 200

