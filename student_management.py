import json
import os

STUDENT_FILE = "students.json"

def load_students():
    
    if not os.path.exists(STUDENT_FILE):
        return []
    with open(STUDENT_FILE, "r") as f:
        return json.load(f)

def save_students(students):
    
    with open(STUDENT_FILE, "w") as f:
        json.dump(students, f, indent=4)

def add_student():
    students = load_students()

    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    save_students(students)
    print(" Student added successfully!\n")


def view_students():
    students = load_students()

    if not students:
        print("No student records found.\n")
        return

    print("\n----- Student List -----")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, Age: {s['age']}, Course: {s['course']}")
    print()


def search_student():
    students = load_students()
    sid = input("Enter Student ID to search: ")

    for s in students:
        if s["id"] == sid:
            print("\n----- Student Found -----")
            print(f"ID: {s['id']}\nName: {s['name']}\nAge: {s['age']}\nCourse: {s['course']}\n")
            return

    print(" Student not found.\n")


def update_student():
    students = load_students()
    sid = input("Enter Student ID to update: ")

    for s in students:
        if s["id"] == sid:
            print("\nEnter new details (leave blank to keep old value)")
            name = input(f"New Name ({s['name']}): ") or s['name']
            age = input(f"New Age ({s['age']}): ") or s['age']
            course = input(f"New Course ({s['course']}): ") or s['course']

            s['name'] = name
            s['age'] = age
            s['course'] = course

            save_students(students)
            print(" Student updated successfully!\n")
            return

    print(" Student not found.\n")


def delete_student():
    students = load_students()
    sid = input("Enter Student ID to delete: ")

    for s in students:
        if s["id"] == sid:
            students.remove(s)
            save_students(students)
            print("🗑️ Student deleted successfully!\n")
            return

    print(" Student not found.\n")


def main():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.\n")


if __name__ == "__main__":
    main()
