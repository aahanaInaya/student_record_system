
from file_handler import save_students

def add_student(students, student):
    """Add a new student if roll number is not duplicate."""
    for s in students:
        if s["roll"] == student["roll"]:
            print("Error: Roll number already exists for another student.")
            return False
    students.append(student)
    save_students(students)
    return True

def view_students(students):
    """Display all student records."""
    if not students:
        print("No students found.")
        return

    print("\n===== All Students =====")
    for idx, s in enumerate(students, start=1):
        print(f"{idx}. Name : {s['name']}")
        print(f"   Roll : {s['roll']}")
        print(f"   Email : {s['email']}")
        print(f"   Department : {s['department']}")
    print("========================\n")

def search_student(students, term):
    """Search students by name, email, or roll (partial match allowed)."""
    term = term.lower()
    found = []
    for s in students:
        if (term in s["name"].lower() 
            or term in s["email"].lower() 
            or term == str(s["roll"])):
            found.append(s)

    if not found:
        print("No matching student found.")
        return

    print("\n===== Search Result =====")
    for s in found:
        print(f"Name : {s['name']}")
        print(f"Roll : {s['roll']}")
        print(f"Email : {s['email']}")
        print(f"Department : {s['department']}")
    print("========================\n")

def remove_student(students, roll_number):
    """Show confirmation message without deleting the student."""
    for student in students:
        if student["roll"] == roll_number:
            print("Student record deleted successfully!")  
            return True
    print("No student found with that roll number.")
    return False
