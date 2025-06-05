from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Float, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(String(60), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(120), nullable=False)
    last_name: Mapped[str] = mapped_column(String(120), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    favorite_people = relationship('Favorite_People', lazy=True)
    favorite_planets = relationship('Favorite_Planets', lazy=True)


    def serialize(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "first_name": self.first_name,
            "last_name": self.last_name,            
            "email": self.email,
            "is_active": self.is_active,
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    __tablename__ = 'people'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(60), nullable=False)
    gender: Mapped[str] = mapped_column(String(60), nullable=False)
    skin_color: Mapped[str] = mapped_column(String(60), nullable=False)
    hair_color: Mapped[str] = mapped_column(String(60), nullable=False)
    height: Mapped[Float] = mapped_column(Float, nullable=False)    
    eye_color: Mapped[str] = mapped_column(String(60), nullable=False)
    mass: Mapped[Float] = mapped_column(Float, nullable=False)
    birth_year: Mapped[str] = mapped_column(String(60), nullable=False)
    favorite_people = relationship('Favorite_People', lazy=True)


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "skin_color": self.skin_color,
            "hair_color": self.hair_color,
            "height": self.height,
            "eye_color": self.eye_color,
            "mass": self.mass,
            "birth_year": self.birth_year,
        }

class Planets(db.Model):   
    __tablename__ = 'planets'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(60), unique=True, nullable=False)
    climate: Mapped[str] = mapped_column(String(60), nullable=False)
    surfece_water: Mapped[Float] = mapped_column(Float, nullable=False)
    diameter: Mapped[int] = mapped_column(Integer, nullable=False)
    rotation_period: Mapped[int] = mapped_column(Integer, nullable=False)
    terrain: Mapped[str] = mapped_column(String(60), nullable=False)
    gravity: Mapped[str] = mapped_column(String(60), nullable=False)
    orbital_period: Mapped[int] = mapped_column(Integer, nullable=False)
    population: Mapped[int] = mapped_column(Integer, nullable=False)   
    favorite_planets = relationship('Favorite_Planets', backref='planets', lazy=True)
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "surfece_water": self.surfece_water,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "terrain": self.terrain,
            "gravity": self.gravity,
            "orbital_period": self.orbital_period,
            "population": self.population,
        }

class Favorite_People(db.Model):
    __tablename__ = 'favorite_people'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    people_id: Mapped[int] = mapped_column(ForeignKey('people.id'), nullable=False)
   

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "people_id": self.people_id        
        }

class Favorite_Planets(db.Model):   
    __tablename__ = 'favorite_planets'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    planet_id: Mapped[int] = mapped_column(ForeignKey('planets.id'), nullable=False)
    
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id
        }
