from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

user_people = db.Table('user_people',
    db.Column('people_id', db.Integer, db.ForeignKey('people.people_id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
)

# user_planets = db.Table('user_planets',
#     db.Column('planet_id', db.Integer, db.ForeignKey('planets.planet_id'), primary_key=True),
#     db.Column('user_id', db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
# )

class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), unique=True, nullable=False)
    user_email = db.Column(db.String(120), unique=True, nullable=False)
    user_password = db.Column(db.String(80), unique=False, nullable=False)
    favorite_people = db.relationship("Favorite_people", backref='users', lazy=True) 
    user_people = db.relationship('People', secondary=user_people, lazy='subquery', backref=db.backref('users', lazy=True))
    # user_planets = db.relationship('Planets', secondary=user_planets, lazy='subquery', backref=db.backref('users', lazy=True))

    def __repr__(self):
        return f'{self.user_name}' ##'<Users %r>' % self.user_name

    def serialize(self):
        return {    # do not serialize the password, its a security breach
            "user_id": self.user_id,
            "user_name": self.user_name,
            "user_email": self.user_email,
            "favorite_people": list(map(lambda x: x.serialize(), self.favorite_people)),
            # "user_people": list(map(lambda x: x.serialize(), self.user_people))       ###  se usan ???
            # "user_planets": list(map(lambda x: x.serialize(), self.user_planets))      ###  se usan ???
        }

class People(db.Model):
    people_id = db.Column(db.Integer, primary_key=True)
    people_name = db.Column(db.String(250), unique=True, nullable=False)
    people_url = db.Column(db.String(250), nullable=False)
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
        return '<People %r>' % self.people_name

    def serialize(self):
        return {
            "people_id": self.people_id,
            "people_name" : self.people_name,
            "people_url" : self.people_url,
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
            # "favorite_people": list(map(lambda x: x.serialize(), self.favorite_people)),
        }

class Favorite_people(db.Model):
    own_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False) 
    people_id = db.Column(db.Integer, db.ForeignKey('people.people_id'), nullable=False)
    ## combinar dos columnas como id 

    def __repr__(self):
        return f'El nombre del favorito es {People.query.get(self.people_id).people_name}'  ## People.query.get(self.people_id) : este es el objeto

    def serialize(self):
        return {
            "own_id": self.own_id,
            "user_id": self.user_id,
            "people_id": self.people_id,
        }

# class Planets(db.Model):
#     planet_id = db.Column(db.Integer, primary_key=True)
#     planet_name = db.Column(db.String(250), nullable=False)
#     planet_url = db.Column(db.String(250), nullable=False)
#     diameter = db.Column(db.Integer)
#     rotation_period = db.Column(db.Integer)
#     orbital_period = db.Column(db.Integer)
#     gravity = db.Column(db.Integer)
#     population = db.Column(db.Integer)
#     climate = db.Column(db.String(250))
#     terrain = db.Column(db.String(250))
#     surface_water = db.Column(db.Integer)
#     created = db.Column(db.Integer) 
#     edited = db.Column(db.Integer)
#     favorite_planets = db.relationship("favorite_planets", backref='planets', lazy=True)

#     def __repr__(self):
#         return '<Planets %r>' % self.planet_name

#     def serialize(self):
#         return {
#             "planet_id": self.planet_id,
#             "planet_name" : self.planet_name,
#             "planet_url" : self.planet_url,
#             "diameter" : self.diameter,
#             "rotation_period" : self.rotation_period,
#             "orbital_period" : self.orbital_period,
#             "gravity" : self.gravity,
#             "population" : self.population,
#             "climate" : self.climate,
#             "terrain" : self.terrain,
#             "surface_water" : self.surface_water,
#             "created" : self.created, 
#             "edited" : self.edited,
#         }

# class Favorite_planets(db.Model):
#     own_id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer) # , db.ForeignKey("users.user_id") , primary_key=True
#     planet_id = db.Column(db.Integer) # , db.ForeignKey("planets.planet_id") , primary_key=True

#     def __repr__(self):
#         return '<Favorite_planets %r>' % self.own_id

#     def serialize(self):
#         return {
#             "own_id": self.own_id,
#             "user_id": self.user_id,
#             "planet_id": self.planet_id,
#         }