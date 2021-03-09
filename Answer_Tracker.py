students = {"Padi": 0, "Carlos": 0, "Andres": 0, "Eduardo": 0}
# There are 10 q so we need to add a for with 10 steps
for i in range(10):
    name = input(f"Who got the answer right for question number {i+1}?")
    if name in students:
        students[name] = students[name]+1
    else:
        # this means the student name was not in the dict, so put value 1
        students[name] = 1

print(f"Here as the list of students and answers: {students}")

# Find the winner (find the key with the highest vale)
# Step 1: get a list of all the keys

values = list(students.values())
# print(f"sorted values {values}")

values.sort(reverse=True) # Sorts the list descending
# print(f"sorted values {values}")
winner = values[0]

# Step 2: once I have the Winner value, go over each key and see if he/she is the winner
for key in students:
    if students[key] == winner:
        print(f"{key} is the winner! Congrats!!")
