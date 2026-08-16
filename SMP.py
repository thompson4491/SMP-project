

import json


class student:
    def __init__(self, id, name, age, grade):
        self.id = id
        self.name = name
        self.age = age
        self.grade = grade

all_students = []

def load_data():
    try:
        f = open("students.txt", "r")
        data = json.load(f)
        f.close()
        for item in data:
            s = student(item['id'], item['name'], item['age'], item['grade'])
            all_students.append(s)
        print("Data loaded successfully")
    except:
        print("No saved file found starting fresh")

def save_data():
    temp_list = []
    for s in all_students:
        temp_list.append({
            "id": s.id,
            "name": s.name,
            "age": s.age,
            "grade": s.grade
        })
    f = open("students.txt", "w")
    json.dump(temp_list, f)
    f.close()
    print("Saved to students.txt")

def add_student():
    print("\n Add Student")
    id = input("Enter ID: ")
    
    for s in all_students:
        if s.id == id:
            print("That ID is taken")
            return

    name = input("Enter Name: ")
    while True:
        try:
            age = int(input("Enter Age: "))
            break
        except:
            print("Invalid data type")
            
    grade = input("Enter Grade: ")
    new_s = student(id, name, age, grade)
    all_students.append(new_s)
    print("Added!")

def view_students():
    print("\nALL STUDENTS")
    if len(all_students) == 0:
        print("Nothing here yet.")
    else:
        for s in all_students:
            print("ID: " + str(s.id) + " | Name: " + s.name + " | Age: " + str(s.age) + " | Grade: " + s.grade)

def search_student():
    print("\nSEARCH")
    search = input("Enter ID or Name: ")
    found = False
    for s in all_students:
        if search.lower() in s.id.lower() or search.lower() in s.name.lower():
            print("Found: ID: " + str(s.id) + " | Name: " + s.name + " | Age: " + str(s.age) + " | Grade: " + s.grade)
            found = True
    if found == False:
        print("No student found matching that.")

def update_student():
    print("\nUPDATE")
    id = input("Enter ID of student to edit: ")
    for s in all_students:
        if s.id == id:
            print("Found " + s.name)
            new_name = input("New name (or press Enter to skip): ")
            if new_name != "":
                s.name = new_name
            
            new_age = input("New age (or press Enter to skip): ")
            if new_age != "":
                try:
                    s.age = int(new_age)
                except:
                    print("Invalid age entered, keeping old age.")
            
            new_grade = input("New grade (or press Enter to skip): ")
            if new_grade != "":
                s.grade = new_grade
            print("Updated!")
            return
    print("ID not found.")

def delete_student():
    print("\nDELETE")
    id = input("Enter ID to delete: ")
    for s in all_students:
        if s.id == id:
            all_students.remove(s)
            print("Deleted successfully!")
            return
    print("Could not find student with that ID.")


load_data()

while True:
    print("\n" + "="*20)
    print("STUDENT SYSTEM")
    print("1. Add Student")
    print("2. View All")
    print("3. Search")
    print("4. Update")
    print("5. Delete")
    print("6. Save")
    print("7. Exit")
    print("="*20)
    
    choice = input("Choice (1-7): ")
    
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
        save_data()
    elif choice == "7":
        save_data()
        print("Bye!")
        break
    else:
        print("Invalid choice, enter 1 to 7")