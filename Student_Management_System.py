students = []


def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    city = input("Enter student city: ")
    hobby = input("Enter student hobby: ")

    subjects = {}

    while True:
        subject = input("Enter subject name (or 'done' to finish): ")
        if subject.lower() == "done":
            break
        grade = input("Enter grade for the subject: ")
        subjects[subject] = grade

    student = {
        "name": name,
        "age": age,
        "city": city,
        "hobby": hobby,
        "subjects": subjects,
    }

    students.append(student)
    print("Student added successfully!")


def view_students():
    if not students:
        print("No students found.")
    else:
        for student in students:
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("City:", student["city"])
            print("Hobby:", student["hobby"])
            print("Subjects:")
            for subject, grade in student["subjects"].items():
                print(f"  {subject}: {grade}")
            print()


def update_student():
    name = input("Enter the name of the student to update: ")
    for student in students:
        if student["name"] == name:
            print("Student found. Enter new details:")
            student["name"] = input("Enter new name: ")
            student["age"] = int(input("Enter new age: "))
            student["city"] = input("Enter new city: ")
            student["hobby"] = input("Enter new hobby: ")
            print("Student details updated successfully!")
            return
    print("Student not found.")


def delete_student():
    name = input("Enter the name of the student to delete: ")
    for student in students:
        if student["name"] == name:
            students.remove(student)
            print("Student deleted successfully!")
            return
    print("Student not found.")


def search_student():
    name = input("Enter the name of the student to search: ")
    for student in students:
        if student["name"] == name:
            print("Student found. Details:")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("City:", student["city"])
            print("Hobby:", student["hobby"])
            print("Subjects:")
            for subject, grade in student["subjects"].items():
                print(f"  {subject}: {grade}")
            return
    print("Student not found.")


def calculate_average_grade():
    name = input("Enter the name of the student to calculate average grade: ")
    for student in students:
        if student["name"] == name:
            grades = [int(grade) for grade in student["subjects"].values()]
            average_grade = sum(grades) / len(grades)
            print(f"Average grade for {name}: {average_grade}")
            return
    print("Student not found.")


def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Calculate Average Grade")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            search_student()
        elif choice == "6":
            calculate_average_grade()
        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()
