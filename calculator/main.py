def addition(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    if num2==0:
        print("Not divisible ..")
    return num1 / num2

num1 = int(input("Enter first input : "))
num2 = int(input("Enter second input : "))

while True: 
    print(" ---------------------------- ")
    print("       Digi - calculator      ")
    print("  1. Addition ")
    print("  2. Subtraction")
    print("  3. Multiplication")
    print("  4. Division")
    print("  0. Exiting .. ")
    print(" ---------------------------- ")

    choice = int(input(" Please enter your choice : "))

    if choice == 1:
        result = addition(num1,num2)
        print(f"the additon of {num1} and {num2} is {result}")

    elif choice == 2:
        result = sub(num1,num2)
        print(f"the subtraction of {num1} and {num2} is {result}")

    elif choice == 3:
        result = multiply(num1,num2)
        print(f"the multiplication of {num1} and {num2} is {result}")

    elif choice == 4:
        result = divide(num1,num2)
        print(f"the division of {num1} and {num2} is {result}")

    elif choice == 0:
        print("Exiting thank you for using :)")
        break

    else : 
        print("Invalid choice ")

    change = input("Do you want to change your numbers? (y/n) :")
    if change.lower() == "y":
        num1 = int(input("Enter first input : "))
        num2 = int(input("Enter second input : "))

    else : 
        print("Noted !")

