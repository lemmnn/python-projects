while True :
    print("-------------------------")
    print(" .... NOTES MANAGER .... ")
    print(" 1. Create a note")
    print(" 2. View note")
    print(" 3. Delete the note")
    print(" 4. Exit")

    choice = input("Enter your choice (1-3) :")

    if choice == "1" :
        note = input("Enter your note :")
        try :
            with open("notes.txt", "a") as file:
                file.write(note + "\n")
            print("the note has been saved :)")

        except Exception as e:
            print("Oops .. something went wrong", e)

    elif choice == "2":
        try:
            with open("notes.txt","r") as file:
                notes = file.readlines()

            if not notes:
                print("No notes has been found luv")

            else :
                for i in notes:
                    print(note.strip())

        except FileNotFoundError:
            print("The file was not found ")

    elif choice == "4":
        print("thanks for using")
        break

    elif choice == "3":
        confirm = input("Are you sure you want to delete all notes? (y/n): ")
        
        if confirm == "y":
            open("notes.txt", "w").close()
            print("All notes deleted.")
            
        else:
            print("Cancelled.")

    else:
        print("invalid choice")