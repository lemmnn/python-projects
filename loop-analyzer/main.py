n=int(input("enter a number:"))
while True:
    print("----------------------")
    print("1. Even or odd number")
    print("2. Type of number")
    print("3. Factorial")
    print("4. Prime or not")
    print("5. EXit")
    a=int(input("Enter your choice (1-4):"))

    if a==1:
        if n%2==0:
            print(f"The number {n} is even")
        else:
            print(f"The number {n} is odd")

    elif a==2:
        if n>0 :
            print(f"The number {n} is positive")
        elif n==0:
            print("The number is neither positive or negative")
        else : 
            print(f"The number {n} is negative")

    elif a==3:
        if n < 0:
            print("Factorial not defined for negative numbers")
        else:
            fact = 1
            for i in range(1, n+1):
                fact = fact * i
            print(f"The factorial of {n} is {fact}")

    elif a==4:
        if n <= 1:
            print("Not prime")
        else:
            for i in range(2, n):
                if n % i == 0:
                    print("Not prime")
                    break
            else:
                print("Prime")

    elif a==5:
        print("Exiting ..")
        break

    else :
        print("Invalid input")

