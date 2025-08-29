"""Database utilities for the generator."""
from pathlib import Path
import json
from peewee import SqliteDatabase

from . import models

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "db.sqlite3"
DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "exercises.json"

def connect_to_db():
    db = SqliteDatabase(DB_PATH)
    models._db.initialize(db)
    return db


def create_tables():
    db = models._db.obj
    db.create_tables([
        models.Exercise,
        models.Session,
        models.Block,
        models.ExerciseBlock,
        models.Tag,
        models.ExerciseTag,
        models.SessionTag,
    ])


def load_initial_data():
    if not DATA_FILE.exists():
        return
    with DATA_FILE.open() as f:
        data = json.load(f)
    for item in data:
        models.Exercise.get_or_create(name=item["name"], defaults=item)
