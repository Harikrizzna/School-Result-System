import json

# Simple data storage
students = []

# Function to load data from JSON file
def load_from_file():
    try:
        with open("Results.json", "r") as file:
            data = json.load(file)
            global students
            students = data
    except FileNotFoundError:
        print("No previous data found. Starting fresh.")
    except json.JSONDecodeError:
        print("Error reading the JSON file. Starting fresh.")

# Function to Save Data to JSON file
def save_to_file():
    with open("Results.json", "w") as file:
        json.dump(students, file, indent=4)

# Function to Add a Student
def add_student():
    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    try:
        roll_number = int(roll_number)
    except ValueError:
        print("Roll number must be an integer.")
        return
    students.append({
        "name": name,
        "roll_number": roll_number,
        "marks": {}
    })
    print("Student " + name + " with Roll Number " + str(roll_number) + " added.")

# Function to Enter Marks
def enter_marks():
    roll_number = input("Enter roll number: ")
    subject = input("Enter subject: ")
    marks = input("Enter marks: ")
    try:
        roll_number = int(roll_number)
        marks = int(marks)
    except ValueError:
        print("Roll number and marks must be integers.")
        return
    
    for student in students:
        if student["roll_number"] == roll_number:
            student["marks"][subject] = marks
            print("Marks for " + subject + " updated for Roll Number " + str(roll_number) + ".")
            return
    print("Student with Roll Number " + str(roll_number) + " not found.")

# Function to Display Student Results
def display_student_result():
    roll_number = input("Enter roll number: ")
    try:
        roll_number = int(roll_number)
    except ValueError:
        print("Roll number must be an integer.")
        return
    
    for student in students:
        if student["roll_number"] == roll_number:
            print("Results for " + student["name"] + " (Roll Number: " + str(roll_number) + "):")
            total_marks = sum(student["marks"].values())
            subjects = len(student["marks"])
            percentage = (total_marks / (subjects * 100)) * 100 if subjects > 0 else 0
            print("Total Marks: " + str(total_marks) + ", Percentage: " + str(round(percentage, 2)))
            return
    print("Student with Roll Number " + str(roll_number) + " not found.")

# Main menu
load_from_file()  # Load data from file at the start

while True:
    print("\n--- School Result System ---")
    print("1. Add Student")
    print("2. Enter Marks")
    print("3. Display Student Result")
    print("4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        enter_marks()
    elif choice == '3':
        display_student_result()
    elif choice == '4':
        save_to_file()  # Save data to file before exiting
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
