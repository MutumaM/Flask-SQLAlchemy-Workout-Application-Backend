from marshmallow import Schema, fields, validate, validates, ValidationError

class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, error="Exercise name cannot be empty"))
    category = fields.Str(
        required=True,
        validate=validate.OneOf(
            ['Strength', 'Cardio', 'Flexibility', 'Balance'],
            error="Category must be one of: {choices}"
        )
    )
    equipment_needed = fields.Bool()

exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)


class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    duration_minutes = fields.Int(
        required=True,
        validate=validate.Range(min=1, error="Duration must be greater than 0 minutes")
    )
    notes = fields.Str()
workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)


class WorkoutExercisesSchema(Schema):
    id = fields.Int(dump_only=True)
    workout_id = fields.Int(required=True)
    exercise_id = fields.Int(required=True)
    reps = fields.Int(validate=validate.Range(min=0, error="Reps cannot be negative"))
    sets = fields.Int(validate=validate.Range(min=0, error="Sets cannot be negative"))
    duration_seconds = fields.Int()

    exercise = fields.Nested(ExerciseSchema, dump_only=True)

workout_exercises_schema = WorkoutExercisesSchema()
workout_exercises_schema_many = WorkoutExercisesSchema(many=True)