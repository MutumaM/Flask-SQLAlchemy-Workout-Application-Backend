from flask import Flask, make_response
from flask_migrate import Migrate

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
    return {"message": "list all workouts - coming soon"}, 200

@app.route('/workouts/<int:id>', methods=['GET'])
def get_workout(id):
    return {"message": f"show workout {id} - coming soon"}, 200

@app.route('/workouts', methods=['POST'])
def create_workout():
    return {"message": "create workout - coming soon"}, 201

@app.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    return {"message": f"delete workout {id} - coming soon"}, 200

# Exercises

@app.route('/exercises', methods=['GET'])
def get_exercises():
    return {"message": "list all exercises - coming soon"}, 200

@app.route('/exercises/<int:id>', methods=['GET'])
def get_exercise(id):
    return {"message": f"show exercise {id} - coming soon"}, 200

@app.route('/exercises', methods=['POST'])
def create_exercise():
    return {"message": "create exercise - coming soon"}, 201

@app.route('/exercises/<int:id>', methods=['DELETE'])
def delete_exercise(id):
    return {"message": f"delete exercise {id} - coming soon"}, 200

#  Workout <-> Exercise link 

@app.route('/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises', methods=['POST'])
def add_exercise_to_workout(workout_id, exercise_id):
    return {"message": f"add exercise {exercise_id} to workout {workout_id} - coming soon"}, 201


if __name__ == '__main__':
    app.run(port=5555, debug=True)