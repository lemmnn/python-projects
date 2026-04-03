
n=int(input("Enter the number of entries:"))

for i in range(n):
    Name=input("Enter your name:")
    while True:
        Age=input("Enter your age:")
        if Age.isdigit() and 1 <= int(Age) <= 120:
            break
        else:
            print("invalid .. ")
    
    while True:
        Call=input("Enter your phoneno:")
        if Call.isdigit() and len(Call)==10:
            break
        else:
            print("invalid number range ..")

    b_g=["A+","A-","B+","B-","O+","O-","AB+","AB-"]
    while True:
        blood=input("Enter your blood type:")
        if blood in b_g:
            break
        else:
            print("enter valid blood group ..")

    while True:
        dob=input("Enter your dob(dd-mm-yyyy):")
        if len(dob)==10 and dob[2]=='-' and dob[5]=='-':
            break
        else:
            print("enter valid format dob .. ")
            
            
    print("---------------------------")
    print("        INFO CARD          ")
    print(f"{'Name:':15}{Name}")
    print(f"{'Age:':15}{Age}")
    print(f"{'Phone-no:':15}{Call}")
    print(f"{'Blood type:':15}{blood}")
    print(f"{'Date of birth:':15}{dob}")
    print("---------------------------")
