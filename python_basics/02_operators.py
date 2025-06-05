# Q1: Calculate the area of a rectangle with length = 10 and width = 5.
length = 10
width = 5
# Arithmetic Operators
area = length * width  # Multiplication
perimeter = 2 * (length + width)  # Addition and Multiplication
print(f"Area of the rectangle: {area}")  # Output: Area of the rectangle: 50
print(f"Perimeter of the rectangle: {perimeter}")  # Output: Perimeter of the rectangle: 30

# Q2: What is the result of 2 raised to the power 5?
print(f"{5**2}")

# Q3: Calculate the average of three numbers: 72, 88, and 91.
numbers = [72, 88, 91]
average = sum(numbers) / len(numbers)  # Sum and Division
print(f"Average of the numbers: {average}")  # Output: Average of the numbers: 83.66666666666667

# Q4: Is 15 greater than 20? Is 15 less than or equal to 15?
is_greater = 15 > 20  # Greater than
is_less_equal = 15 <= 15  # Less than or equal to
print(f"Is 15 greater than 20? {is_greater}")  # Output: Is 15 greater than 20? False
print(f"Is 15 less than or equal to 15? {is_less_equal}")  # Output: Is 15 less than or equal to 15? True

# Q5: Compare two strings: "Python" and "python". Are they equal?
string_comparison = "Python" == "python"  # Equality
print(f"Are 'Python' and 'python' equal? {string_comparison}")  # Output: Are 'Python' and 'python' equal? False

# Q6: Check if the square of 5 is equal to 25.
is_square_equal = (5 ** 2) == 25  # Exponentiation and Equality
print(f"Is the square of 5 equal to 25? {is_square_equal}")  # Output: Is the square of 5 equal to 25? True

# Q7: Suppose has_passport = True and has_ticket = False.
#     Can a person travel? (has_passport and has_ticket)
has_passport = True
has_ticket = False
can_travel = has_passport and has_ticket  # Logical AND
print(f"Can a person travel? {can_travel}")  # Output: Can a person travel? False

# Q8: If temperature is 25, check if it’s a good day (between 20 and 30 inclusive).
temperature = 25
is_good_day = 20 <= temperature <= 30  # Logical AND with comparison
print(f"Is it a good day? {is_good_day}")  # Output: Is it a good day? True

# Q9: Set a variable `count = 10`. Use += and -= to increase and decrease it.
count = 10
count += 5  # Increase by 5
print(f"Count after increase: {count}")  # Output: Count after increase: 15
count -= 3  # Decrease by 3
print(f"Count after decrease: {count}")  # Output: Count after decrease: 12

# Q10: Simulate a bank account balance update with += and -=.
balance = 1000  # Initial balance
deposit = 200  # Amount to deposit
withdrawal = 150  # Amount to withdraw
balance += deposit  # Deposit money 
print(f"Balance after deposit: {balance}")  # Output: Balance after deposit: 1200
balance -= withdrawal  # Withdraw money
print(f"Balance after withdrawal: {balance}")  # Output: Balance after withdrawal: 1050

 