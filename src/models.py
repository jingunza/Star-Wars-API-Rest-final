from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    favorite_people = db.relationship("Favorite_people", backref='users', lazy=True)
    favorite_planets = db.relationship("Favorite_planets", backref='users', lazy=True)

    def __repr__(self):
        return f'{self.name}'

    def serialize(self):
        return {    # do not serialize the password, its a security breach
            "id": self.id,
            "name": self.name,
            "email": self.email,
            # "favorite_people": list(map(lambda x: x.serialize(), self.favorite_people))
        }

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    url = db.Column(db.String(250), nullable=False)
    height = db.Column(db.Integer, nullable=True)
    mass = db.Column(db.Integer, nullable=True)
    hair_color = db.Column(db.String(250), nullable=True)
    skin_color = db.Column(db.String(250), nullable=True)
    eye_color = db.Column(db.String(250), nullable=True)
    birth_year = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.String(250), nullable=True)
    created = db.Column(db.String(250), nullable=True) 
    edited = db.Column(db.String(250), nullable=True)
    homeworld = db.Column(db.String(250), nullable=True) #, ForeignKey('planets.uid')
    favorite_people = db.relationship("Favorite_people", backref='people', lazy=True)

    def __repr__(self):
        return f'{self.name}'

    def serialize(self):
        return {
            "id": self.id,
            "name" : self.name,
            "url" : self.url,
            "height" : self.height,
            "mass" : self.mass,
            "hair_color" : self.hair_color,
            "skin_color" : self.skin_color,
            "eye_color" : self.eye_color,
            "birth_year" : self.birth_year,
            "gender" : self.gender,
            "created" : self.created, 
            "edited" : self.edited,
            "homeworld" : self.homeworld,
        }

class Favorite_people(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True, nullable=False)
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'), primary_key=True, nullable=False)

    def __repr__(self):
        return f'{Users.query.get(self.user_id).name, People.query.get(self.people_id).name}'

    def serialize(self):
        return {
            "user_id": self.user_id,
            "user_name": Users.query.get(self.user_id).name,
            "people_id": self.people_id,
            "people_name": People.query.get(self.people_id).name,
            "url" : People.query.get(self.people_id).url,
            "height" : People.query.get(self.people_id).height,
            "mass" : People.query.get(self.people_id).mass,
            "hair_color" : People.query.get(self.people_id).hair_color,
            "skin_color" : People.query.get(self.people_id).skin_color,
            "eye_color" : People.query.get(self.people_id).eye_color,
            "birth_year" : People.query.get(self.people_id).birth_year,
            "gender" : People.query.get(self.people_id).gender,
            "created" : People.query.get(self.people_id).created, 
            "edited" : People.query.get(self.people_id).edited,
            "homeworld" : People.query.get(self.people_id).homeworld
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    url = db.Column(db.String(250), nullable=False)
    diameter = db.Column(db.Integer)
    rotation_period = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    gravity = db.Column(db.Integer)
    population = db.Column(db.Integer)
    climate = db.Column(db.String(250))
    terrain = db.Column(db.String(250))
    surface_water = db.Column(db.Integer)
    created = db.Column(db.Integer) 
    edited = db.Column(db.Integer)
    favorite_planets = db.relationship("Favorite_planets", backref='planets', lazy=True)

    def __repr__(self):
        return f'{self.name}'

    def serialize(self):
        return {
            "id": self.id,
            "name" : self.name,
            "url" : self.url,
            "diameter" : self.diameter,
            "rotation_period" : self.rotation_period,
            "orbital_period" : self.orbital_period,
            "gravity" : self.gravity,
            "population" : self.population,
            "climate" : self.climate,
            "terrain" : self.terrain,
            "surface_water" : self.surface_water,
            "created" : self.created, 
            "edited" : self.edited,
        }

class Favorite_planets(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True, nullable=False) 
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'), primary_key=True, nullable=False)

    def __repr__(self):
        return f'{Users.query.get(self.user_id).name, Planets.query.get(self.planet_id).name}'

    def serialize(self):
        return {
            "user_id": self.user_id,
            "user_name": Users.query.get(self.user_id).name,
            "planet_id": self.planet_id,
            "planet_name": Planets.query.get(self.planet_id).name,
            "url" : Planets.query.get(self.planet_id).url,
            "diameter" : Planets.query.get(self.planet_id).diameter,
            "rotation_period" : Planets.query.get(self.planet_id).rotation_period,
            "orbital_period" : Planets.query.get(self.planet_id).orbital_period,
            "gravity" : Planets.query.get(self.planet_id).gravity,
            "population" : Planets.query.get(self.planet_id).population,
            "climate" : Planets.query.get(self.planet_id).climate,
            "terrain" : Planets.query.get(self.planet_id).terrain,
            "surface_water" : Planets.query.get(self.planet_id).surface_water,
            "created" : Planets.query.get(self.planet_id).created, 
            "edited" : Planets.query.get(self.planet_id).edited
        }