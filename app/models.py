from app import db

class Brand(db.Model):
    name = db.Column(db.String(128), primary_key=True)

class Base(db.Model):
    __abstract__  = True

    name = db.Column(db.String(128), primary_key=True)
    price = db.Column(db.Integer, primary_key=True)

    ram = db.Column(db.Integer, primary_key=True)
    storage = db.Column(db.Integer, primary_key=True)

    resolution = db.Column(db.Integer, primary_key=True)
    screen = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Integer, primary_key=True)

    link = db.Column(db.Text, primary_key=True)

    date_created = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

class Laptop(Base):
    __tablename__ = 'laptop'

    def __init__(self, name, price, ram, storage, resolution, screen, weight):
        self.name = name
        self.price = price
        self.ram = ram
        self.storage = storage
        self.resolution = resolution
        self.screen = screen
        self.weight = weight

    def __repr__(self):
        return '<Laptop %r>' % (self.name)       
