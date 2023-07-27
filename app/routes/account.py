from flask import Blueprint, jsonify, request
from app import db

from app.models.project import Project
from app.models.account import Account
from app.models.signin import Signin

accounts_bp = Blueprint("accounts", __name__, url_prefix="/accounts")


@accounts_bp.route("", methods=['POST'])
def create_account():
    print(f"@@@@@@@@@@@@@@@@@ {request}")
    request_body = request.get_json()
    print(f"request body: {request_body}")
    
    if "accountId" in request_body:
        return {}, 400
    
    account = {
        "accountId": 123,
        "firstName": request_body["firstName"],
        "lastName": request_body["lastName"],
        "email": request_body["email"],
        "zipcode": request_body["zipcode"]
    }
    return {"account": account}, 201


@accounts_bp.route("", methods=['GET'])
def get_accounts():

    account = {
        "accountId": 123,
        "firstName": "Angie",
        "lastName": "Contreras",
        "email": "gjhgdjhg@fgsj.com",
        "zipcode": 98011
    }
    return {"account": account}, 200


@accounts_bp.route("/<accountId>", methods=['PUT'])
def update_one_account(accountId):
    request_body = request.get_json()
    request_account_id = int(accountId)
    if not "email" in request_body:
        return {}, 400
    elif request_account_id != request_body["accountId"]:
        return {}, 401
    else:
        print(f"Received body, {request_body} with account id: {accountId}")
        print("Email updated")
        return {"account": request_body}, 200
    

# Route to test sign in
signin_bp = Blueprint("signin", __name__, url_prefix="/signin")
@signin_bp.route("", methods=['POST'])
def authenticate_user_info():
    USER = "user"
    PASSWORD = "password"
    print("Inside signnin!@@@@@@")
    userInfo = {USER: "Angie123tdd", PASSWORD: "ryrtyry123"}
    request_body = request.get_json()
    
    print(request_body)

    if userInfo[USER] == request_body[USER] \
        and userInfo[PASSWORD] == request_body[PASSWORD]:

        account = {
        "accountId": 123,
        "firstName": "Angie",
        "lastName": "Contreras",
        "email": "gjhgdjhg@fgsj.com",
        "zipcode": 98011
        }
        return {"account": account}, 200
    else:
        return "Wrong user", 400


test_bp = Blueprint("test", __name__, url_prefix="/test")
@test_bp.route("", methods=['POST'])
def mytest():
    request_body = request.get_json()
    
    print("Received:", request_body)
    return {
        "result": "ok"
        }, 200
