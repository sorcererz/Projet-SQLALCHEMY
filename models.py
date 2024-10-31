from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Initialisation
Base = declarative_base()
engine = create_engine('sqlite:///data/vgsales.db')

# Définition des tables
class Publisher(Base):
    __tablename__ = 'publishers'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)

    # Relation avec Game (One-to-Many)

class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)

    # Relation avec Game (One-to-Many)

class Platform(Base):
    __tablename__ = 'platforms'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)

    # Relation avec Game (One-to-Many)
    # games = relationship("Game", back_populates="platform")

class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    year = Column(Integer)
    publisher_id = Column(Integer, ForeignKey('publishers.id'))
    genre_id = Column(Integer, ForeignKey('genres.id'))
    platform_id = Column(Integer, ForeignKey('platforms.id'))

    # Relations vers Publisher, Genre, et Platform
    publisher = relationship("Publisher", back_populates="games")
    genre = relationship("Genre", back_populates="games")
    platform = relationship("Platform", back_populates="games")
    
    # Relation avec Sales (One-to-Many)
    # sales = relationship("Sales", back_populates="game")

class Sales(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('games.id'))
    na_sales = Column(Float)    # Ventes en Amérique du Nord
    eu_sales = Column(Float)    # Ventes en Europe
    jp_sales = Column(Float)    # Ventes au Japon
    other_sales = Column(Float) # Ventes dans les autres régions

    # Relation avec Game (Many-to-One)
    # game = relationship("Game", back_populates="sales")

# # Créer les tables dans la base de données
# Base.metadata.create_all(engine)

testGenre = Genre()
testGenre.name = 'toto'
print(testGenre.__dict__)
