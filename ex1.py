# 1. Ask the user how many students they want to enroll
n = int(input("Give me a number !!"))

# 2. Create an empty list to store student names
students = []

# 3. Loop 'n' times to get each student's name and add to the list
for i in range(n):
    name = input(f"Give me the name of student {i+1}")  # Ask for the student's name
    students.append(name)  # Add the name to the list

# 4. Display the full list of students
print("Displaying the list of students !! ")
print(students)

# 5. Sort the list alphabetically and display it
print("Displaying list of student in order")
students.sort()
print(students)

# 6. Display the total number of students
print(f"Displaying the total number of student: {len(students)}")

# 7. Ask for a name to remove from the list
student_to_remove = input("Enter the name to remove")

# Check if the name is in the list, and remove it if found
if student_to_remove in students:
    students.remove(student_to_remove)  # Remove the name
    print(f"{student_to_remove} removed from the list")
else:
    print(f"{student_to_remove} was not found in the list")

# 8. Display the updated student list
print("\nDisplay the new list\n")
print(students)
