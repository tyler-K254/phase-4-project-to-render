from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
db = SQLAlchemy()
car_features = db.Table(
    "car_features",  # Update the table name here
    db.Column("car_id", db.ForeignKey("cars.id"), primary_key=True),
    db.Column("feature_id", db.ForeignKey("features.id"), primary_key=True),
    db.Column("transmission", db.String),
    db.Column("created_at", db.DateTime, server_default=db.func.now()),
    db.Column("updated_at", db.DateTime, onupdate=db.func.now()),
)
class Car(db.Model, SerializerMixin):
    __tablename__ = 'cars'
    serialize_rules = ('-car_features.cars',)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    features = db.relationship('Feature', secondary=car_features, backref='car', viewonly=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updates_at = db.Column(db.DateTime, onupdate=db.func.now())
    # @validates('name')
    # def validate_name(self,key,name):
    #     if not name:
    #         raise ValueError("Name must be present")
    #     if not isinstance(name, str):
    #         raise ValueError('Name must be a string.')
    #     return name
    # @validates('image')
    # def validate_image(self, key, image):
    #     if 'http' not in image:
    #         raise ValueError("Provide correct image url")
    #     return image
class Feature(db.Model, SerializerMixin):
    __tablename__ = 'features'
    serialize_rules = ('-car_features.features',)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updates_at = db.Column(db.DateTime, onupdate=db.func.now())
    cars = db.relationship('Car', secondary=car_features, backref='feature', overlaps="car,features")
    # @validates('description')
    # def validate_description(self,key,description):
    #     if len(description) < 25:
    #         raise ValueError("Description must be atleast 250 characters long")
    #     return description
# class CarFeature(db.Model, SerializerMixin):
#     __tablename__ = 'car_features'
#     serialize_rules = ('-car.car_features', '-feature.car_features',)
#     id = db.Column(db.Integer, primary_key=True)
#     transmission = db.Column(db.String)
#     feature_id = db.Column(db.Integer, db.ForeignKey('features.id'), nullable=False)
#     car_id = db.Column(db.Integer, db.ForeignKey('cars.id'), nullable=False)
#     created_at = db.Column(db.DateTime, server_default=db.func.now())
#     updates_at = db.Column(db.DateTime, onupdate=db.func.now())
    # @validates('transmission')
    # def validate_transmission(self,key,transmission):
    #     valid_transmission = ['automatic', 'manual']
    #     if transmission not in valid_transmission:
    #         raise ValueError("Invalid transmission type")
    #     return transmission