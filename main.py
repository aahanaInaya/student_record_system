from student import add_student, view_students, search_student, remove_student
from file_handler import load_students, save_students

def main():
    print("Welcome to the Student Record Management System!")

    # Load existing students from file
    students = load_students()
    print("Loading student records from students.json... Done!\n")

    while True:
        print("=========== MENU ===========")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Remove Student")
        print("5. Exit")
        print("============================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Enter Student Name: ").strip()
            if not name:
                print("Error: Name cannot be empty.")
                continue

            roll_input = input("Enter Roll Number: ").strip()
            if not roll_input.isdigit():
                print("Error: Roll number must be an integer.")
                continue
            roll = int(roll_input)

            email = input("Enter Email: ").strip()
            if not email:
                print("Error: Email cannot be empty.")
                continue

            department = input("Enter Department: ").strip()
            if not department:
                print("Error: Department cannot be empty.")
                continue

            student = {
                "name": name,
                "roll": roll,
                "email": email,
                "department": department
            }

            add_student(students, student)
            save_students(students)
            print("Student record added successfully!\n")

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            term = input("Enter search term (name/email/roll): ").strip()
            if not term:
                print("Error: Search term cannot be empty.")
                continue
            search_student(students, term)

        elif choice == "4":
            roll_input = input("Enter the roll number of the student to delete: ").strip()
            if not roll_input.isdigit():
                print("Error: Roll number must be an integer.")
                continue
            roll = int(roll_input)

            confirm = input(f"Are you sure you want to delete student with roll number {roll}? (y/n): ").lower()
            if confirm == "y":
                remove_student(students, roll)
            else:
                print("Deletion cancelled.\n")

        elif choice == "5":
            print("Thank you for using the Student Record Management System. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 5.\n")

if __name__ == "__main__":
    main()
