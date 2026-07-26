from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()
from sqlalchemy.ext.associationproxy import association_proxy


class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    equipment_needed = db.Column(db.Boolean, default=False)
    workout_exercises = db.relationship(
        'WorkoutExercises',
        back_populates='exercise',
        cascade='all, delete-orphan'  
    )
    workouts = association_proxy('workout_exercises', 'workout')


    @validates('name')
    def validate_name(self, key, name):
        if not name or len(name.strip()) == 0:
            raise ValueError('Exercise name cannot be empty')
        return name

    @validates('category')
    def validate_category(self, key, category):
        allowed = ['Strength', 'Cardio', 'Flexibility', 'Balance']
        if category not in allowed:
            raise ValueError(f'Category must be one of {allowed}')
        return category



class Workout(db.Model):
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text)

    workout_exercises = db.relationship(
        'WorkoutExercises',
        back_populates='workout',
        cascade='all, delete-orphan'
    )
    exercises = association_proxy('workout_exercises', 'exercise')

    @validates('duration_minutes')
    def validate_duration(self, key, duration_minutes):
        if duration_minutes <= 0:
            raise ValueError('Duration must be greater than 0 minutes')
        return duration_minutes

class WorkoutExercises(db.Model):
    __tablename__ = 'workout_exercises'

    __table_args__ = (
        db.CheckConstraint('reps >= 0', name='check_reps_non_negative'),
        db.CheckConstraint('sets >= 0', name='check_sets_non_negative'),
    )

    id = db.Column(db.Integer, primary_key=True)

    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)

    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    duration_seconds = db.Column(db.Integer)

    workout = db.relationship('Workout', back_populates='workout_exercises')
    exercise = db.relationship('Exercise', back_populates='workout_exercises')