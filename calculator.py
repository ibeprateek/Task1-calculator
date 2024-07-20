number1 = float(input("Please enter the first number: "))
number2 = float(input("Please enter the second number: "))

print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operation = input("Enter the number of your chosen operation: ")

if operation == "1":
    result = number1 + number2
elif operation == "2":
    result = number1 - number2
elif operation == "3":
    result = number1 * number2
elif operation == "4":
    if number2 != 0:
        result = number1 / number2
    else:
        print("Error: Division by zero is not allowed.")
        exit()
else:
    print("Invalid operation. Please choose a number between 1 and 4.")
    exit()

print("The result is: " + str(result))