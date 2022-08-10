from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# user_people = db.Table('user_people',
#     db.Column('people_id', db.Integer, db.ForeignKey('people.id'), primary_key=True),
#     db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True)
# )

class Favorite_people(db.Model):
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'), primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True, nullable=False)

    def __repr__(self):
        return f'{Users.query.get(self.user_id).name, People.query.get(self.people_id).name}'  ## People.query.get(self.people_id) : este es el objeto!!, name es la columna

    def serialize(self):
        return {
            "user_id": self.user_id,
            "people_id": self.people_id,
            # "relacion": Users.query.get(self.user_id).name +', '+ People.query.get(self.people_id).name
        }

# user_planets = db.Table('user_planets',
#     db.Column('planet_id', db.Integer, db.ForeignKey('planets.id'), primary_key=True),
#     db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True)
# )

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    favorite_people = db.relationship("Favorite_people", backref='users', lazy=True)
    # user_people = db.relationship('People', secondary=user_people, lazy='subquery') # , backref=db.backref('users', lazy=True)
    # favorite_planets = db.relationship("Favorite_planets", backref='users', lazy=True) 
    # user_planets = db.relationship('Planets', secondary=user_planets, lazy='subquery', backref=db.backref('users', lazy=True))

    def __repr__(self):
        return f'{self.name}' ##'<Users %r>' % self.name

    def serialize(self):
        return {    # do not serialize the password, its a security breach
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "favorite_people": list(map(lambda x: x.serialize(), self.favorite_people)),     ###  se usan ???
            # "favorite_planets": list(map(lambda x: x.serialize(), self.favorite_planets)),       ###  se usan ???
            # "user_people": list(map(lambda x: x.serialize(), self.user_people))       ###  se usan ???
            # "user_people": self.user_people
            # "user_planets": list(map(lambda x: x.serialize(), self.user_planets))      ###  se usan ???
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
    # user_people = db.relationship('Users', secondary=user_people, lazy='subquery') #, backref=db.backref('people', lazy=True)

    def __repr__(self):
        return f'{self.name}' # <People %r>' % self.people_name

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

# class Favorite_people(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True, nullable=False)
#     people_id = db.Column(db.Integer, db.ForeignKey('people.id'), primary_key=True, nullable=False)
#     ## combinar dos columnas como id ??

#     def __repr__(self):
#         return f'{People.query.get(self.people_id).name}'  ## People.query.get(self.people_id) : este es el objeto!!, name es la columna

#     def serialize(self):
#         return {
#             "id": self.id,
#             "user_id": self.user_id,
#             "people_id": self.people_id
#         }

# class Planets(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(250), nullable=False)
#     url = db.Column(db.String(250), nullable=False)
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
#     favorite_planets = db.relationship("Favorite_planets", backref='planets', lazy=True)

#     def __repr__(self):
#         return f'{self.name}' # '<Planets %r>' % self.planet_name

#     def serialize(self):
#         return {
#             "id": self.id,
#             "name" : self.name,
#             "url" : self.url,
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
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) # , primary_key=True
#     planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=False) #, primary_key=True

#     def __repr__(self):
#         return f'{Planets.query.get(self.planet_id).name}' # '<Favorite_planets %r>' % self.own_id

#     def serialize(self):
#         return {
#             "id": self.id,
#             "user_id": self.user_id,
#             "planet_id": self.planet_id,
#         }