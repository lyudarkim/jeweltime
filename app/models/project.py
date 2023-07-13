from app import db
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy import PickleType


class Project(db.Model):
    project_id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(100))
    description = db.Column(db.String(250))
    started_at = db.Column(db.DateTime, nullable=False)
    completed_at = db.Column(db.DateTime, nullable=True)
    hours_spent = db.Column(db.Float)
    materials_cost = db.Column(db.Float)
    materials = db.Column(MutableList.as_mutable(PickleType),default=[])
    metals = db.Column(MutableList.as_mutable(PickleType),default=[])
    gemstones = db.Column(MutableList.as_mutable(PickleType),default=[])
    shape = db.Column(db.String(100))
    jewelry_type = db.Column(db.String(100))
    account_id = db.Column(db.Integer, db.ForeignKey('account.account_id'), nullable=True)


    def to_dict(self):
        return \
            {
                "id": self.project_id,
                "project_name": self.project_name,
                "description": self.description,
                "started_at": self.started_at,
                "materials": self.materials,
                "hours_spent": self.hours_spent,
                "metals": self.metals,
                "gemstones": self.gemstones,
                "jewelry_type": self.jewelry_type,
                "shape": self.shape
            }