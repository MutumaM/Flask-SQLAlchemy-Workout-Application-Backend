# Workout Tracker API

A backend REST API for a workout tracking app used by personal trainers. Built with Flask, SQLAlchemy, and Marshmallow. Trainers can manage reusable exercises, log workouts, and track sets, reps, and duration for each exercise in a workout.

## Description

- **Exercises** — reusable exercise definitions (name, category, equipment needed)
- **Workouts** — a logged session with a date, duration, and notes
- **Workout Exercises** — links a workout to an exercise with reps, sets, and/or duration

Endpoints: `GET/POST /workouts`, `GET/DELETE /workouts/<id>`, `GET/POST /exercises`, `GET/DELETE /exercises/<id>`, `POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises`

## Requirements

- Python 3.8.13+
- Pip, Git

## Installation

```bash
git clone <your-repo-url>
cd workout-application
python3 -m venv .venv
source .venv/bin/activate
pip install flask==2.2.2 flask-migrate==3.1.0 flask-sqlalchemy==3.0.3 werkzeug==2.2.2 importlib-metadata==6.0.0 importlib-resources==5.10.0 marshmallow==3.20.1

cd server
flask db init
flask db migrate -m "create tables"
flask db upgrade head
python seed.py
```

## Running

From `server/`:

```bash
export FLASK_DEBUG=1
flask run
```

API runs at `http://localhost:5000`. Test with Thunder Client, Postman, or `curl`:

```bash
curl http://localhost:5555/exercises
```
