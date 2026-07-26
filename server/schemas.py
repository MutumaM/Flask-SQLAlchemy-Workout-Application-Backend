from marshmallow import Schema, fields

class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    equipment_needed = fields.Bool()

exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)


class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    duration_minutes = fields.Int(required=True)
    notes = fields.Str()

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)


class WorkoutExercisesSchema(Schema):
    id = fields.Int(dump_only=True)
    workout_id = fields.Int(required=True)
    exercise_id = fields.Int(required=True)
    reps = fields.Int()
    sets = fields.Int()
    duration_seconds = fields.Int()

    # nested = show the full related object, not just its id, when outputting
    exercise = fields.Nested(ExerciseSchema, dump_only=True)

workout_exercises_schema = WorkoutExercisesSchema()
workout_exercises_schema_many = WorkoutExercisesSchema(many=True)