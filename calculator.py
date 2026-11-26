import math
history = []
print("=" * 45)
print("       CALCX - SMART CALCULATOR")
print("=" * 45)
while True:
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Percentage")
    print("8. Even or Odd Checker")
    print("9. View History")
    print("0. Exit")
    choice = input("\nEnter your choice: ")
    if choice == "0":
        print("\nThank you for using CalcX!🧮")
        break
    elif choice == "1":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = a + b
        print(f"Result: {result}")
        history.append(f"{a} + {b} = {result}")
    elif choice == "2":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = a - b
        print(f"Result: {result}")
        history.append(f"{a} - {b} = {result}")
    elif choice == "3":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = a * b
        print(f"Result: {result}")
        history.append(f"{a} * {b} = {result}")
    elif choice == "4":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if b != 0:
            result = a / b
            print(f"Result: {result}")
            history.append(f"{a} / {b} = {result}")
        else:
            print("Error: Cannot divide by zero!")
    elif choice == "5":
        a = float(input("Enter base: "))
        b = float(input("Enter exponent: "))
        result = a ** b
        print(f"Result: {result}")
        history.append(f"{a} ** {b} = {result}")
    elif choice == "6":
        a = float(input("Enter number: "))
        if a >= 0:
            result = math.sqrt(a)
            print(f"Square Root: {result}")
            history.append(f"Square root of {a} = {result}")
        else:
            print("Error: Negative number not allowed!")
    elif choice == "7":
        a = float(input("Enter total amount: "))
        b = float(input("Enter percentage: "))
        result = (a * b) / 100
        print(f"{b}% of {a} = {result}")
        history.append(f"{b}% of {a} = {result}")
    elif choice == "8":
        a = int(input("Enter a number: "))
        if a % 2 == 0:
            print(f"{a} is Even")
        else:
            print(f"{a} is Odd")
    elif choice == "9":
        print("\n--- Calculation History ---")
        if history:
            for item in history:
                print(item)
        else:
            print("No calculations yet!")
    else:
        print("Invalid choice! Please try again.")
print("\nHave a great day!😊")
