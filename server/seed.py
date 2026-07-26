#!/usr/bin/env python3

from datetime import date
from app import app
from models import db, Exercise, Workout, WorkoutExercises

with app.app_context():

	# reset data and add new example data, committing to db 

    print("Clearing existing data...")
    WorkoutExercises.query.delete()
    Workout.query.delete()
    Exercise.query.delete()


    print("Seeding exercises...")
    push_up = Exercise(name="Push-up", category="Strength", equipment_needed=False)
    squat = Exercise(name="Squat", category="Strength", equipment_needed=False)
    running = Exercise(name="Running", category="Cardio", equipment_needed=False)
    plank = Exercise(name="Plank", category="Balance", equipment_needed=False)

    db.session.add_all([push_up, squat, running, plank])
    db.session.commit()


    print("Seeding workouts...")
    workout_1 = Workout(date=date(2026, 7, 20), duration_minutes=45, notes="Morning strength session")
    workout_2 = Workout(date=date(2026, 7, 22), duration_minutes=30, notes="Quick cardio")

    db.session.add_all([workout_1, workout_2])
    db.session.commit()

    print("Seeding workout_exercises...")
    we_1 = WorkoutExercises(workout=workout_1, exercise=push_up, reps=12, sets=3)
    we_2 = WorkoutExercises(workout=workout_1, exercise=squat, reps=15, sets=3)
    we_3 = WorkoutExercises(workout=workout_1, exercise=plank, sets=3, duration_seconds=60)
    we_4 = WorkoutExercises(workout=workout_2, exercise=running, duration_seconds=1800)

    db.session.add_all([we_1, we_2, we_3, we_4])
    db.session.commit()

    print("Seeding complete!")