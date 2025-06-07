# Q1: Write a program that checks if a number is positive, negative, or zero.
def checktype(number):
    if(number==0):
        print("The number is zero")
    elif(number%2==0):
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
checktype(10)

# Q2: Ask the user to input their age and print if they are a minor, adult, or senior.
def check_age(age):
    if age < 18:
        print("You are a minor.")
    elif 18 <= age < 65:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")

age_input = input("Enter your age: ")
check_age(int(age_input))

# Q3: Given a temperature value in Celsius, print whether it’s cold (<10), warm (10–25), or hot (>25).
def check_temperature(celsius):
    if celsius < 10:
        print("It's cold.")
    elif 10 <= celsius <= 25:
        print("It's warm.")
    else:
        print("It's hot.")
temperature_input = input("Enter temperature in Celsius: ")
check_temperature(float(temperature_input))

# Q4: Create a variable `score`. Print a grade:
def print_grade(score):
    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
score_input = input("Enter your score: ")
print_grade(int(score_input))

#Loops
# Q5: Print all numbers from 1 to 10 using a for loop.
for i in range(1, 10):
    print(f"Current number: {i}")
# Q6: Loop through a list of fruits and print each fruit in uppercase.
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(f"Fruit: {fruit.upper()}")

# Q7: Loop through numbers 1 to 20. For each number:
#     - If divisible by 3, print "Fizz"
#     - If divisible by 5, print "Buzz"
#     - If divisible by both, print "FizzBuzz"
#     - Otherwise, print the number
for num in range(1, 21):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
# Q8: Loop through a dictionary of country-capital pairs and print each pair as "Capital of X is Y".
statecapital = {
    "California": "Sacramento",
    "Texas": "Austin",
    "Florida": "Tallahassee",
    "New York": "Albany"
}
for state, capital in statecapital.items():
    print(f"The capital of {state} is {capital}.")

#Whileloops
# Q9: Write a while loop that counts down from 5 to 1 and prints each number.
countdown = 5
while countdown > 0:
    print(f"Countdown: {countdown}")
    countdown -= 1

# Q10: Ask the user to guess a secret number (e.g., 7). Keep prompting until they guess it right.
secret_number = 7
def guess_secret_number():
    while True:
        guess = input("Guess the secret number (between 1 and 10): ")
        if guess.isdigit() and 1 <= int(guess) <= 10:
            if int(guess) == secret_number:
                print("Congratulations! You've guessed the secret number.")
                break
            else:
                print("Wrong guess, try again!")
        else:
            print("Please enter a valid number between 1 and 10.")
guess_secret_number()

# Q11: Initialize a variable with a random number between 1 and 100. Using a while loop, print all even numbers less than it.
import random
def print_even_numbers():
    random_number = random.randint(1, 100)
    print(f"Random number: {random_number}")
    num = 0
    while num < random_number:
        if num % 2 == 0:
            print(f"Even number: {num}")
        num += 1
print_even_numbers()

#Loop Control Statements
# Q12: Use a for loop to iterate through numbers 1 to 10. Use `continue` to skip even numbers.
def skip_even_numbers():
    for num in range(1, 11):
        if num % 2 == 0:
            continue  # Skip even numbers
        print(f"Odd number: {num}")
skip_even_numbers()
# Q13: Loop through characters in a string. Use `break` if you find the letter "x".
def find_x_in_string(s):
    for char in s:
        if char == 'x':
            print("Found 'x', breaking the loop.")
            break
        print(f"Current character: {char}")
find_x_in_string("example string with x in it")

#mini Chanllenge
# Q14: Create a simple CLI menu using a while loop:
#     Options: 1. Say Hello, 2. Show Date, 3. Exit
#     Use if-elif to handle menu options and a while loop to keep showing the menu until Exit is chosen.
def cli_menu():
    while True:
        print("\nMenu:")
        print("1. Say Hello")
        print("2. Show Date")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            print("Hello!")
        elif choice == '2':
            from datetime import datetime
            print(f"Current date and time: {datetime.now()}")
        elif choice == '3':
            print("Exiting the menu. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
cli_menu()