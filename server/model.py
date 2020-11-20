from app import db


class Referrer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)


class LeadPac(db.Model):
    id = db.Column(db.String(64), primary_key=True)
    referrer_id = db.Column(db.Integer)
    name = db.Column(db.String(120))
    first_name = db.Column(db.String(120))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    zip_code = db.Column(db.String(10))
    work_field = db.Column(db.String(40))
    heat_system = db.Column(db.String(40))
    household_nb = db.Column(db.Integer)
    household_wage = db.Column(db.Integer)
    eligible = db.Column(db.Boolean)


if __name__ == "__main__":
    db.create_all()
