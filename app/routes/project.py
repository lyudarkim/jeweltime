from flask import Blueprint, jsonify, request
from app import db

from app.models.project import Project
from app.models.account import Account


projects_bp = Blueprint("projects", __name__, url_prefix="/projects")