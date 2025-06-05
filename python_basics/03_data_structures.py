#List Operations in Python
# Q1: Create a list of your 5 favorite programming languages.
favorite_languages = ["Python", "JavaScript", "Java", "C++", "Ruby"]
print(f"Favorite languages: {favorite_languages}")
# Q2: Add a new language to the end of the list.
favorite_languages.append("Go")
print(f"After adding a new language: {favorite_languages}")
# Q3: Insert a language at index 2.
favorite_languages.insert(2, "Swift")
print(f"After inserting a language at index 2: {favorite_languages}")

# Q4: Remove the last language from the list and print the list.
favorite_languages.pop()  # Remove the last language
print(f"After removing the last language: {favorite_languages}")

# Q5: Sort the list alphabetically and print it.
favorite_languages.sort()  # Sort the list alphabetically
print(f"After sorting the languages: {favorite_languages}")

# Q6: Loop through the list and print each language in uppercase.
for lang in favorite_languages:
    print(f"Language: {lang.upper()}")

# Q7: Check if "Python" is in your list and print a message accordingly.
if "Python" in favorite_languages:
    print("Python is in the list of favorite languages.")

# Tuples
# Q8: Create a tuple of 3 important HTTP methods (e.g., GET, POST, PUT).
http_methods = ("GET", "POST", "PUT")
print(f"HTTP Methods: {http_methods}")

# Q9: Try changing the second element — what error do you get? Comment your observation.
#http_methods[2] = "DELETE"  # This will raise an error because tuples are immutable
#print(f"HTTP Methods after trying to change PUT to DELETE: {http_methods}")
#'tuple' object does not support item assignment

# Q10: Use slicing to get the first two elements of the tuple.
first_two_methods = http_methods[:2]
print(f"First two HTTP methods: {first_two_methods}")

# Q11: Convert the tuple to a list, add "DELETE", then convert it back to a tuple.
http_methods_list = list(http_methods)  # Convert tuple to list
http_methods_list.append("DELETE")  # Add "DELETE" to the list
http_methods = tuple(http_methods_list)  # Convert back to tuple
print(f"HTTP Methods after adding DELETE: {http_methods}")

#Dictionaries
# Q12: Create a dictionary with keys: name, age, and favorite_language.
person_info={"name":"John Doe", "age": 30, "favorite_language": "Python"}
print(f"Person Info: {person_info}")
print(f"{type(person_info)}")

# Q13: Print the value associated with "favorite_language".
print(f"favorite_language: {person_info['favorite_language']}")  # Accessing value by key

# Q14: Add a new key "country" and assign a value.
person_info.update({"location": "USA"})  # Adding a new key-value pair
print(f"Person Info after adding location: {person_info}")

# Q15: Loop through the dictionary and print each key-value pair.
for key, value in person_info.items():
    print(f"{key}: {value}")  # Looping through dictionary items

# Q16: Use `.get()` to safely access a non-existent key (e.g., "email").
email =person_info.get("email")
if email is None:
    print("Email key does not exist in the dictionary.")

# Q17: Delete the "age" key from the dictionary and print the result.
person_info.pop("age", None)  # Remove the key "age" if it exists, do nothing if it doesn't
print(f"Person Info after removing age: {person_info}")

#SETS
# Q18: Create two sets:
#      - set_a = {"Python", "Java", "C++"}
#      - set_b = {"Python", "Go", "Rust"}
set_a = {"Python", "Java", "C++"}
set_b = {"Python", "Go", "Rust"}
# Q19: Find the common elements between both sets (intersection).
common_elements = set_a.intersection(set_b)  # Intersection of two sets
print(f"Common elements: {common_elements}")
print(f"{type(set_a)}")

# Q20: Find all unique elements across both sets (union).
union_items =set_a.union(set_b)  # Union of two sets
print(f"Union of both sets: {union_items}")

# Q21: Find elements that are in set_a but not in set_b (difference).
difference_items = set_a.difference(set_b)  # Difference between two sets
print(f"Elements in set_a but not in set_b: {difference_items}")

# Q22: Add "TypeScript" to set_b and print it.
set_b.add("TypeScript")  # Adding an element to set_b
print(f"set_b after adding TypeScript: {set_b}")

#Mini Integration Task
# Q23: Create a list of dictionaries representing students with keys: name, age, and favorite_subject.
students = [
    {"name": "Alice", "age": 20, "marks": "90"},
    {"name": "Bob", "age": 22, "marks": "80"},
    {"name": "Charlie", "age": 21, "marks": "50"}
]
for student in students:
    if(student["marks"] > "80"):
        print(f"{student['name']} has the highest marks: {student['marks']}")

#      - Calculate and print the average marks
average_marks = sum(int(student["marks"]) for student in students) / len(students)
print(f"Average marks of students: {average_marks}")