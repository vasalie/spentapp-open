from models import db

class Tbl_Records(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    date     = db.Column(db.Integer)
    location = db.Column(db.String(100))
    category = db.Column(db.String(100))
    value    = db.Column(db.Integer)
    type     = db.Column(db.String(50))
    convert  = db.Column(db.Integer)
    note     = db.Column(db.String(200))

    def __repr__(self):
        return f'<Records {self.name}>'


