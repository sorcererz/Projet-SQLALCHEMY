import sys
import os

# Ajoutez le répertoire parent au chemin
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

import pytest as pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String
from models import Genre, Base


# Creation d'une base de données temporaire
TEST_DATABASE_URI = "sqlite:///:memory:"


@pytest.fixture()
def test_engine():
    engine = create_engine(TEST_DATABASE_URI)
    Base.metadata.create_all(engine)

    yield engine
    Base.metadata.drop_all(engine)


@pytest.fixture()
def test_session(test_engine):
    """Crée une session pour chaque test."""
    connection = test_engine.connect()
    transaction = connection.begin()
    session = sessionmaker(bind=connection)()

    yield session  # Permet aux tests d'utiliser la session

    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture()
def test_db():
    engine = create_engine(TEST_DATABASE_URI) 
    Base.metadata.create_all(engine)
    connection = engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()

    yield session  

    session.close()
    transaction.rollback()
    connection.close()

def test_genre_creation(test_db):
    genre_instance = Genre(name="Sports")
    test_db.add(genre_instance)
    test_db.commit()

    test_instance = test_db.query(Genre).filter_by(id=genre_instance.id).first()

    assert test_instance is not None
    assert test_instance.name == "Sports"