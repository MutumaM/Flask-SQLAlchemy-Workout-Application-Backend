from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from schemas import (
    exercise_schema, exercises_schema,
    workout_schema, workouts_schema,
    workout_exercises_schema
)
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

# Define Routes here

# Workouts 

@app.route('/workouts', methods=['GET'])
def get_workouts():
    workouts = Workout.query.all()
    return jsonify(workouts_schema.dump(workouts)), 200

@app.route('/workouts/<int:id>', methods=['GET'])
def get_workout(id):
    workout = Workout.query.get(id)
    if not workout:
        return jsonify({"error": "Workout not found"}), 404

    result = workout_schema.dump(workout)
    result['workout_exercises'] = [
        workout_exercises_schema.dump(we) for we in workout.workout_exercises
    ]
    return jsonify(result), 200

@app.route('/workouts', methods=['POST'])
def create_workout():
    data = request.get_json()

    errors = workout_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    try:
        new_workout = Workout(
            date=data['date'],
            duration_minutes=data['duration_minutes'],
            notes=data.get('notes', '')
        )
        db.session.add(new_workout)
        db.session.commit()
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    return jsonify(workout_schema.dump(new_workout)), 201

@app.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    workout = Workout.query.get(id)
    if not workout:
        return jsonify({"error": "Workout not found"}), 404

    db.session.delete(workout)
    db.session.commit()
    return jsonify({"message": "Workout deleted"}), 200

# Exercises

@app.route('/exercises', methods=['GET'])
def get_exercises():
    exercises = Exercise.query.all()
    return jsonify(exercises_schema.dump(exercises)), 200

@app.route('/exercises/<int:id>', methods=['GET'])
def get_exercise(id):
    exercise = Exercise.query.get(id)
    if not exercise:
        return jsonify({"error": "Exercise not found"}), 404
    return jsonify(exercise_schema.dump(exercise)), 200

@app.route('/exercises', methods=['POST'])
def create_exercise():
    data = request.get_json()

    errors = exercise_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    try:
        new_exercise = Exercise(
            name=data['name'],
            category=data['category'],
            equipment_needed=data.get('equipment_needed', False)
        )
        db.session.add(new_exercise)
        db.session.commit()
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    return jsonify(exercise_schema.dump(new_exercise)), 201

@app.route('/exercises/<int:id>', methods=['DELETE'])
def delete_exercise(id):
    exercise = Exercise.query.get(id)
    if not exercise:
        return jsonify({"error": "Exercise not found"}), 404

    db.session.delete(exercise)
    db.session.commit()
    return jsonify({"message": "Exercise deleted"}), 200
#  Workout <-> Exercise link 

@app.route('/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises', methods=['POST'])
def add_exercise_to_workout(workout_id, exercise_id):
    return {"message": f"add exercise {exercise_id} to workout {workout_id} - coming soon"}, 201


if __name__ == '__main__':
    app.run(port=5555, debug=True)