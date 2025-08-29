"""Data models using Peewee ORM."""
from datetime import datetime
from peewee import (
    Model, CharField, TextField, BooleanField, IntegerField,
    FloatField, DateTimeField, ForeignKeyField, DatabaseProxy
)

# Database proxy to be initialized in database.connect_to_db
_db = DatabaseProxy()


class BaseModel(Model):
    class Meta:
        database = _db


class Exercise(BaseModel):
    name = CharField(unique=True)
    category = CharField()
    pattern = CharField()
    muscles_main = TextField()
    equipment = CharField()
    level = CharField()
    unilateral = BooleanField(default=False)
    technique_difficulty = IntegerField(default=1)
    is_cardio = BooleanField(default=False)
    contraindications = TextField(null=True)
    coaching_notes = TextField(null=True)
    video_path = CharField(null=True)


class Session(BaseModel):
    name = CharField(null=True)
    type = CharField()
    duration = IntegerField()  # minutes
    format = CharField()
    objective = CharField()
    focus = CharField()
    volume_factor = FloatField(default=1.0)
    variability = IntegerField(default=50)
    intensity_bias = IntegerField(default=50)
    warmup = BooleanField(default=True)
    cooldown = BooleanField(default=True)
    date_created = DateTimeField(default=datetime.utcnow)
    locked = BooleanField(default=False)
    notes = TextField(null=True)


class Block(BaseModel):
    session = ForeignKeyField(Session, backref="blocks")
    block_type = CharField()
    order = IntegerField()
    duration = IntegerField(default=0)  # seconds
    work_desc = TextField(null=True)
    instructions = TextField(null=True)
    rest_after = IntegerField(default=0)  # seconds


class ExerciseBlock(BaseModel):
    block = ForeignKeyField(Block, backref="block_exercises")
    exercise = ForeignKeyField(Exercise, backref="exercise_blocks")
    order = IntegerField()
    reps_or_time = CharField()


class Tag(BaseModel):
    name = CharField(unique=True)


class ExerciseTag(BaseModel):
    exercise = ForeignKeyField(Exercise, backref="tags")
    tag = ForeignKeyField(Tag, backref="exercise_tags")


class SessionTag(BaseModel):
    session = ForeignKeyField(Session, backref="tags")
    tag = ForeignKeyField(Tag, backref="session_tags")
