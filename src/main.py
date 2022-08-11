"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Users, People, Favorite_people, Planets, Favorite_planets

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


### ______________ ENDPOINTS SEGUN INSTRUCCIONES: _____________ ###

# [GET] /users Listar todos los usuarios del blog
@app.route('/users', methods=['GET'])
def get_users():

    users = Users.query.all()
    print(users)
    all_users = list(map(lambda x: x.serialize(), users))
    print(all_users)
    return jsonify(all_users), 200

# [GET] /people Listar todos los registros de people en la base de datos
@app.route('/people', methods=['GET'])
def get_people():

    people = People.query.all()
    all_people = list(map(lambda x: x.serialize(), people))

    return jsonify(all_people), 200

# [GET] /people/<int:people_id> Listar la información de una sola people
@app.route('/people/<int:people_id>', methods=['GET'])
def get_people_unit(people_id):

    people1 = People.query.get(people_id)
    people1_ser = people1.serialize()

    return jsonify(people1_ser), 200

# [GET] /users/favorites Listar todos los favoritos que pertenecen al usuario actual.
@app.route('/users/favorites', methods=['GET'])  
def get_favs():

    favorite_people = Favorite_people.query.filter_by(user_id=1)
    favorite_people_ser = list(map(lambda x: x.serialize(), favorite_people))

    # favorite_planets = Favorite_planets.query.filter_by(user_id=1)
    # favorite_planets_ser = list(map(lambda x: x.serialize(), favorite_planets))

    # resultado = users_people_favorites_ser + users_planets_favorites_ser
    # return jsonify(resultado), 200

    return jsonify(favorite_people_ser), 200
    
# [POST] /favorite/people/<int:people_id> Añade una nueva people favorita al usuario actual con el people.id = people_id.
@app.route('/favorite/people/<int:people_id>', methods=['POST'])
def post_favorite_people():

    request_body = request.get_json()

    peoplefav1 = Favorite_people(name = request_body["name"], url = request_body["url"], height = request_body["height"], mass = request_body["mass"], hair_color = request_body["hair_color"], skin_color = request_body["skin_color"], eye_color = request_body["eye_color"], birth_year = request_body["birth_year"], gender = request_body["gender"], created = request_body["created"], edited = request_body["edited"], homeworld = request_body["homeworld"])
    
    db.session.add(people1)
    db.session.commit()

    return jsonify(request_body_people), 200

# [POST] /favorite/planet/<int:planet_id> Añade un nuevo planet favorito al usuario actual con el planet id = planet_id.

# [DELETE] /favorite/planet/<int:planet_id> Elimina un planet favorito con el id = planet_id`.
# [DELETE] /favorite/people/<int:people_id> Elimina una people favorita con el id = people_id.






# [GET] /planets Listar los registros de planets en la base de datos
# [GET] /planets/<int:planet_id> Listar la información de un solo planet

@app.route('/favorite/people', methods=['GET'])  
def get_favpeople():

    favorite_people = Favorite_people.query.all()
    favorite_people_ser = list(map(lambda x: x.serialize(), favorite_people))
    return jsonify(favorite_people_ser), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):

    user1 = Users.query.get(user_id)
    user1_ser = user1.serialize()

    return jsonify(user1_ser), 200

@app.route('/users', methods=['POST'])
def post_user():

    request_body_user = request.get_json()

    user1 = Users(username = request_body_user["username"], email = request_body_user["email"], password = request_body_user["password"])
    db.session.add(user1)
    db.session.commit()

    return jsonify(request_body_user), 200

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):

    request_body_user = request.get_json()

    user1 = User.query.get(user_id)
    if user1 is None:
        raise APIException('User not found', status_code=404)
    if "id" in request_body_user:
        user1.id = request_body_user["id"]
    if "name" in request_body_user:
        user1.name = request_body_user["name"]
    if "email" in request_body_user:
        user1.email = request_body_user["email"]
    db.session.commit()

    return jsonify("ok"), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def del_user(user_id):

    request_body_user = request.get_json()

    user1 = Users.query.get(user_id)
    if user1 is None:
        raise APIException('User not found', status_code=404)
    db.session.delete(user1)
    db.session.commit()

    return jsonify("ok"), 200

@app.route('/user', methods=['DELETE'])
def del_all_users(): #borra todos los usuarios

    request_body_user = request.get_json()

    users = Users.query.all()
    for item in users:
        db.session.delete(item)
    db.session.commit()

    return jsonify("ok"), 200

### _________ People: _________ ###





@app.route('/people', methods=['POST'])
def post_people():

    request_body_people = request.get_json()

    people1 = People(name = request_body_people["name"], url = request_body_people["url"], height = request_body_people["height"], mass = request_body_people["mass"], hair_color = request_body_people["hair_color"], skin_color = request_body_people["skin_color"], eye_color = request_body_people["eye_color"], birth_year = request_body_people["birth_year"], gender = request_body_people["gender"], created = request_body_people["created"], edited = request_body_people["edited"], homeworld = request_body_people["homeworld"])
    
    db.session.add(people1)
    db.session.commit()

    return jsonify(request_body_people), 200

@app.route('/people/<int:people_id>', methods=['PUT'])
def update_people(people_id):

    request_body_people = request.get_json()

    people1 = People.query.get(people_id)
    if people1 is None:
        raise APIException('Person not found', status_code=404)
    if "id" in request_body_people:
        People.id = request_body_people["id"]
    if "name" in request_body_people:
        People.name = request_body_people["name"]
    if "url" in request_body_people:
        People.url = request_body_people["url"]
    if "height" in request_body_people:
        People.height = request_body_people["height"]
    if "mass" in request_body_people:
        People.mass = request_body_people["mass"]
    if "hair_color" in request_body_people:
        People.hair_color = request_body_people["hair_color"]
    if "skin_color" in request_body_people:
        People.skin_color = request_body_people["skin_color"]
    if "eye_color" in request_body_people:
        People.eye_color = request_body_people["eye_color"]
    if "birth_year" in request_body_people:
        People.birth_year = request_body_people["birth_year"]
    if "gender" in request_body_people:
        People.gender = request_body_people["gender"]
    if "created" in request_body_people:
        People.created = request_body_people["created"]
    if "edited" in request_body_people:
        People.edited = request_body_people["edited"]
    if "homeworld" in request_body_people:
        People.homeworld = request_body_people["homeworld"]
 
    db.session.commit()

    return jsonify("ok"), 200

@app.route('/people/<int:people_id>', methods=['DELETE'])
def del_people(people_id):

    request_body_people = request.get_json()

    people1 = People.query.get(people_id)
    if people1 is None:
        raise APIException('Person not found', status_code=404)
    db.session.delete(people1)
    db.session.commit()

    return jsonify("ok"), 200

@app.route('/people', methods=['DELETE'])
def del_all_people(): #borra todos los personajes

    request_body_people = request.get_json()

    people = People.query.all()
    for item in people:
        db.session.delete(item)
    db.session.commit()

    return jsonify("ok"), 200

# ### _________ Planets: ___________ ### user/3/favorites/people/1

# @app.route('/planets', methods=['GET'])
# def get_planets():

#     planets = Planets.query.all()
#     all_planets = list(map(lambda x: x.serialize(), planets))

#     return jsonify(all_planets), 200

# @app.route('/planets/<int:planets_id>', methods=['GET'])
# def get_planets_unit(planets_id):

#     planets1 = Planets.query.get(planets_id)
#     planets1_ser = planets1.serialize()

#     return jsonify(planets1_ser), 200

# @app.route('/planets', methods=['POST'])
# def post_planets():

#     request_body_planets = request.get_json()

#     planets1 = Planets(name = request_body_planets["name"], url = request_body_planets["url"], diameter = request_body_planets["diameter"], rotation_period = request_body_planets["rotation_period"], orbital_period = request_body_planets["orbital_period"], gravity = request_body_planets["gravity"], population = request_body_planets["population"], climate = request_body_planets["climate"], terrain = request_body_planets["terrain"], surface_water = request_body_planets["surface_water"], created = request_body_planets["created"], edited = request_body_planets["edited"])

#     db.session.add(planets1)
#     db.session.commit()

#     return jsonify(request_body_planets), 200

# @app.route('/planets/<int:planets_id>', methods=['PUT'])
# def update_planets(planets_id):

#     request_body_planets = request.get_json()

#     planets1 = Planets.query.get(planets_id)
#     if planets1 is None:
#         raise APIException('User not found', status_code=404)
#     if "id" in request_body_planets:
#         Planets.id = request_body_planets["id"]
#     if "name" in request_body_planets:
#         Planets.name = request_body_planets["name"]
#     if "url" in request_body_planets:
#         Planets.url = request_body_planets["url"]
#     if "height" in request_body_planets:
#         Planets.height = request_body_planets["height"]
#     if "mass" in request_body_planets:
#         Planets.mass = request_body_planets["mass"]
#     if "hair_color" in request_body_planets:
#         Planets.hair_color = request_body_planets["hair_color"]
#     if "skin_color" in request_body_planets:
#         Planets.skin_color = request_body_planets["skin_color"]
#     if "eye_color" in request_body_planets:
#         Planets.eye_color = request_body_planets["eye_color"]
#     if "birth_year" in request_body_planets:
#         Planets.birth_year = request_body_planets["birth_year"]
#     if "gender" in request_body_planets:
#         Planets.gender = request_body_planets["gender"]
#     if "created" in request_body_planets:
#         Planets.created = request_body_planets["created"]
#     if "edited" in request_body_planets:
#         Planets.edited = request_body_planets["edited"]
#     if "homeworld" in request_body_planets:
#         Planets.homeworld = request_body_planets["homeworld"]
 
#     db.session.commit()

#     return jsonify("ok"), 200

# @app.route('/planets/<int:planets_id>', methods=['DELETE'])
# def del_planets(planets_id):

#     request_body_planets = request.get_json()

#     planets1 = Planets.query.get(planets_id)
#     if planets1 is None:
#         raise APIException('User not found', status_code=404)
#     db.session.delete(planets1)
#     db.session.commit()

#     return jsonify("ok"), 200

# @app.route('/planets', methods=['DELETE'])
# def del_all_planets(): #borra todos los personajes

#     request_body_planets = request.get_json()

#     planets = Planets.query.all()
#     for item in planets:
#         db.session.delete(item)
#     db.session.commit()

#     return jsonify("ok"), 200



# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)