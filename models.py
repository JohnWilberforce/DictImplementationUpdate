from gyinyase import db


class Items(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=10), nullable=False, unique=True)
    vehicle_no = db.Column(db.String(length=10), nullable=False, unique=True)
    contact = db.Column(db.String(length=10), nullable=False, unique=True)

    def __repr__(self):
        return f'Item {self.name}'
