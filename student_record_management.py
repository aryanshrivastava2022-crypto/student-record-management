students = {}

while True:
    print("\n🎓 Student Record Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        marks = input("Enter Marks: ")

        students[roll_no] = {
            "name": name,
            "marks": marks
        }

        print("✅ Student record added successfully!")

    elif choice == "2":
        if not students:
            print("No student records found.")
        else:
            print("\n📋 Student Records")
            for roll_no, details in students.items():
                print(f"Roll No: {roll_no}")
                print(f"Name: {details['name']}")
                print(f"Marks: {details['marks']}")
                print("-" * 20)

    elif choice == "3":
        roll_no = input("Enter Roll Number to search: ")

        if roll_no in students:
            print("\n🎓 Student Found")
            print(f"Name: {students[roll_no]['name']}")
            print(f"Marks: {students[roll_no]['marks']}")
        else:
            print("❌ Student not found.")

    elif choice == "4":
        roll_no = input("Enter Roll Number to delete: ")

        if roll_no in students:
            del students[roll_no]
            print("🗑️ Student record deleted successfully!")
        else:
            print("❌ Student not found.")

    elif choice == "5":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice. Please try again.")
