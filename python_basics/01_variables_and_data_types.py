# Q1: Declare a variable to store your name and another for your age. Print both.
name = "John Doe"
age = 30
print("Name:", name)
print("Age:", age)

# Q2: Store your height in meters as a float and print it along with its type.
height = 1.75
print("Height:", height, "meters")

# Q3: Is Python dynamically typed? Demonstrate this by reassigning different types to the same variable.
dynamic_var = 42  # Initially an integer
print("Dynamic variable (int):", dynamic_var, type(dynamic_var))
dynamic_var = "Now I'm a string"  # Reassigned to a string
print("Dynamic variable (str):", dynamic_var, type(dynamic_var))

# Q4: Use the type() function to display the type of these values: 42, 3.14, "Hello", True.
print("Type of 42:", type(42))
print("Type of 3.14:", type(3.14))
print("Type of 'Hello':", type("Hello"))
print("Type of True:", type(True))

# Q5: Convert the integer 100 to a float. Then convert it to a string.
int_value = 100
float_value = float(int_value)
str_value = str(float_value)
print("Integer:", int_value, "Type:", type(int_value))
print("Converted to float:", float_value, "Type:", type(float_value))
print("Converted to string:", str_value, "Type:", type(str_value))

# Q6: What happens when you try to convert the string "hello" to an integer? Use a try-except block.
try:
    int_value = int("hello")
except BaseException as e:
    print("Error converting 'hello' to integer:", e)

# Q7: Concatenate your first and last name with a space in between.
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("Full name:", full_name)
print(f"Full name using f-string: {full_name}")

# Q8: Print the number of characters in your full name using len().
full_name_length = len(full_name)
print("Length of full name:", full_name_length)

# Q9: Print your name in uppercase, lowercase, and title case.
print("Uppercase:", full_name.upper())
print("Lowercase:", full_name.lower())
print("Title case:", full_name.title())

# Q10: Slice the first 3 characters from your name and print them.
first_three_chars = full_name[:3]
print("First 3 characters of full name:", first_three_chars)

# Q11: Create two boolean variables: has_license = True, is_over_18 = False.
#      Use an expression to check if someone is allowed to drive.
has_license = True
is_over_18 = False
print("Has license:", has_license)
print("Is over 18:", is_over_18)
can_drive = has_license and is_over_18
print("Can drive:", can_drive)

# Q12: Use the bool() function on values like 0, "", [], {}, and print the results.
print("Bool of 1:", bool(1))          # True
print("Bool of 0:", bool(0))          # False
print("Bool of empty string:", bool(""))  # False  
print("Bool of string:", bool("NotNull"))  # True
print("Bool of None:", bool(None))  # False  
print("Bool of empty list:", bool([]))  # False
print("Bool of empty dict:", bool({}))  # False
print("Bool of non-empty string:", bool("Hello"))  # True
print("Bool of non-empty list:", bool([1, 2, 3]))  # True

# Q13: Write a script that takes your birth year and calculates your current age (assume current year is 2025).
birth_year = 1992
current_year = 2025
current_age = current_year - birth_year
print("Current age:", current_age)

# Q14: Store the result in a variable and print: "You are X years old."
age_message = f"You are {current_age} years old."
print(age_message)