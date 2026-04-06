tasks=[]

while True:
    print(" ---------------------------- ")
    print("         TO-DO LIST           ")
    print(" ---------------------------- ")
    print("  1. Add tasks ")
    print("  2. Display tasks")
    print("  3. Remove tasks")
    print("  4. Exit")
    print(" ---------------------------- ")
    
    choice = int(input(" Please enter your choice : "))

    if choice ==1:
        order=input("Enter a task :")
        tasks.append(order)

    elif choice == 2:
        if len(tasks) == 0:
            print( "No task to display ^^")
        else :
            for i in range(len(tasks)):
                print(i+1,".", tasks[i])

    elif choice == 3:
        if len(tasks) == 0:
            print(" No tasks to remove ^^")
        else:
            for i in range(len(tasks)):
                print(i+1,".", tasks[i])
            remove=int(input("Enter task number :"))
            
            if remove > 0 and remove <= len(tasks) :
                tasks.pop(remove-1)
                print("Task has been removed !")

            else :
                print("Task number not found :(")

    elif choice == 4:
        print("thank you for using ^_^")
        break

    else:
        print("Invalid choicce ~")       





    

