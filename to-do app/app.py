tasks=[]
try:
    with open("tasks.txt", "r") as file:
        tasks = file.read().splitlines()
except:
    tasks =[]

while True:
    print("1. Add tasks")
    print("2. View tasks")
    print("3. Exit")
    print("4. Delete tasks")

    choice = input("enter your choice (1-4):")

    if choice == "1":
        task = input("Enter your tasks:")
        tasks.append(task)

        with open("tasks.txt", "w") as file:
            for g in tasks:
                file.write(g + "\n")

    elif choice == "2":
        if len(tasks) == 0:
            print("no task yet")
        else:
            for i, j in enumerate(tasks,1):
                print(i,j)

    elif choice == "3":
        print("thanks for using")
        break
    
    elif choice == "4":
        if len(tasks) == 0:
            print("no tasks yet")
        else:
            try:
                delete=int(input("enter the task no to delete:"))
                tasks.pop(delete-1)
                for i, j in enumerate(tasks,1):
                    print(i,j)

                with open("tasks.txt", "w") as file:
                    for g in tasks :
                        file.write(g +"\n")
            except:
                print("Invalid input")

    else:
        print("invalid choice")
    
