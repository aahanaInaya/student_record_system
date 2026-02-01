import json

FILE_NAME = "students.json"

def load_students():
    """Load student records from the JSON file."""
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_students(students):
    """Save the student records to the JSON file."""
    with open(FILE_NAME, "w") as f:
        json.dump(students, f, indent=4)
