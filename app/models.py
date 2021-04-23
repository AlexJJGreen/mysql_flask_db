from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class population(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    comment = db.Column(db.Float(precision=2))
