import os
from flask import Flask, jsonify, request, make_response, render_template
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, Car, car_features, Feature
from dotenv import load_dotenv

load_dotenv()
from flask_cors import CORS

app = Flask(
    __name__,
    static_url_path='',
    static_folder='../client/build',
    template_folder='../client/build'
)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///automobile.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

CORS(app)

migrate = Migrate(app, db)
db.init_app(app)



@app.route('/')
@app.route('/<int:id>')
def index(id=0
          ):
    return render_template("index.html")
@app.route('/cars')
def cars():
    cars=[]
    for car in Car.query.all():
        car_dict={
            "id":car.id,
            "name":car.name,
            "model":car.model,
            "image":car.image,
            
        }
        cars.append(car_dict)
        response=make_response(
            jsonify(cars),
            200
             )
    return response
@app.route('/cars/<int:id>',methods=['GET','PATCH','DELETE'])
def car_by_id(id):
    car=Car.query.filter_by(id=id).first()
    if request.method == 'GET':
        if car:
            car_data={
            "id":car.id,
            "name":car.name,
            "model":car.model,
            "image":car.image
            }
            response=make_response(
              jsonify(car_data),
              200
            )
        # response.headers['content-Type']='application/json'
            return response
        else:
            # Return the error JSON response with appropriate HTTP status code
            return {
                'error': 'car not found'
            }, 404
    elif request.method == 'PATCH':
        for attr in request.form:
            setattr(car, attr, request.form.get(attr))
            
        db.session.add(car)
        db.session.commit()

        car_dict = car.to_dict()

        response = make_response(
                jsonify(car_dict),
                200
            )

        return response
    
    elif request.method == 'DELETE':
            db.session.delete(car)
            db.session.commit()

            response_body = {
                "delete_successful": True,
                "message": "Car deleted."    
            }

            response = make_response(
                jsonify(response_body),
                200
            )

            return response
    

@app.route('/features', methods=['GET', 'POST'])
def features():
    if request.method == 'GET':
        features = Feature.query.all()
        feature_data = [
            {
                "id": feature.id,
                "name": feature.name,
                "description": feature.description,
                "image": feature.image
            }
            for feature in features
        ]
        return jsonify(feature_data), 200

    elif request.method == 'POST':
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON"}), 400

        name = data.get('name')
        description = data.get('description')
        image = data.get('image')

        if not name or not description or not image:
            return jsonify({"error": "Missing required fields"}), 400

        new_feature = Feature(name=name, description=description, image=image)
        db.session.add(new_feature)
        db.session.commit()

        feature_dict = {
            "id": new_feature.id,
            "name": new_feature.name,
            "description": new_feature.description,
            "image": new_feature.image
        }

        return jsonify(feature_dict), 201
@app.route('/cars', methods=['GET', 'POST'])
def handle_cars():
    if request.method == 'GET':
        cars = []
        for car in Car.query.all():
            car_dict = {
                "id": car.id,
                "name": car.name,
                "model": car.model,
                "image": car.image
            }
            cars.append(car_dict)
        response = make_response(jsonify(cars), 200)
        return response
    elif request.method == 'POST':
        data = request.get_json()
        new_car = Car(
            name=data.get("name"),
            model=data.get("model"),
            image=data.get("image")
        )
        db.session.add(new_car)
        db.session.commit()
        car_dict = {
            "id": new_car.id,
            "name": new_car.name,
            "model": new_car.model,
            "image": new_car.image
        }
        response = make_response(jsonify(car_dict), 201)
        return response

if __name__ == '__main__':
    app.run(port=5555)