# empty dictionary
d ={}
print(f"my dictionaty is: {d}")
students = {1: "john", 2: "Valentina", 3: "Beatriz"}
students_list = {"John", "Valentina", "Beatriz"}

# add a new student
students[7] = "Carlos"
print(f"My Studenst are: {students}")
print(f"Carlos is number:{students[7]}")

students["nine"] = "Ignacio"
print(f"My Studenst are: {students}")
# delete Valentina
del students[2]
print(f"My Studenst are: {students}")

# we can iterate over a dictionary
for key in students:
    print(f"{key} -> {students[key]}")