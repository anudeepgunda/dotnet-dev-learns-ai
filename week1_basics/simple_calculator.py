num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
if(division == 0):
    print("Division by zero is not allowed.")
elif(division != 0):
    print(f"Division: {division}")
else:
    print("Invalid operation")