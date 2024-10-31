from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Initialisation
Base = declarative_base()
engine = create_engine('sqlite:///data/vgsales.db')

# Définition des tables
class Publisher(Base):
    __tablename__ = 'publishers'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

class Platform(Base):
    __tablename__ = 'platforms'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    genre_id = Column(Integer, ForeignKey('genres.id'), nullable=False)

    # Relation avec Genre
    genre = relationship("Genre", back_populates="games")

# Ajout de la relation inverse pour Genre (biderectionnelle)
# Genre.games = relationship("Game", back_populates="genre")

class Sales(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    other_sales = Column(DECIMAL(15, 2))
    na_sales = Column(DECIMAL(15, 2))
    eu_sales = Column(DECIMAL(15, 2))
    jp_sales = Column(DECIMAL(15, 2))
    year_sale = Column(Integer)
    platform_id = Column(Integer, ForeignKey('platforms.id'), nullable=False)
    publisher_id = Column(Integer, ForeignKey('publishers.id'), nullable=False)
    game_id = Column(Integer, ForeignKey('games.id'), nullable=False)

    # Relations avec Game, Platform, et Publisher
    game = relationship("Game", back_populates="sales")
    platform = relationship("Platform")
    publisher = relationship("Publisher")

# Relation inverse entre Game et Sales (bidirectionnelle)
# Game.sales = relationship("Sales", back_populates="game")

# Créer les tables dans la base de données
Base.metadata.create_all(engine)