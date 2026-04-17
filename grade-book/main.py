grade_book= {}

def average_marks(marks) :
    if len(marks) ==0:
        print("No marks in the register")
    return sum(marks)/ len(marks)

def grade(avg):
    if avg >=95 :
        return "A+"
    elif avg >= 90 :
        return "A"
    elif avg >= 75 :
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "F"
    
while True :
    print(" -------------------- ")
    print("      GRADE BOOK      ")
    print(" 1. Add student name")
    print(" 2. Add marks ")
    print(" 3. View report")
    print(" 4. Exit")

    choice = input("Enter your choice (1-4):")

    if choice == "1":
        name = input("Enter the student name :")
        if name in grade_book:
            print("Student name is registered already.")
        else :
            grade_book[name]=[]
            print("Student name has been recorded!")

    elif choice == "2":
        name = input("Enter the student name :")
        if name in grade_book:
            marks = int(input("Enter your marks :"))
            grade_book[name].append(marks)
            print("Marks have been recorded!")
        else:
            print("Student has not been registered.")

    elif choice == "3":
        name = input("Enter the student name :")
        if name in grade_book:
            marks = grade_book[name]
            
            if len(marks) == 0:
                print("No marks available for this student.")

            avg = average_marks(marks)
            grade = grade(avg)

            print("\n--- Student Report ---")
            print("Name:", name)
            print("Marks:", marks)
            print(f"Average: {avg:.2f}")
            print("Grade:", grade)

        else:
            print("Student not found!")

    


