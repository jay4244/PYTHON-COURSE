student = {
    "name": "Jay",
    "subject": "python",
    "marks": 45,
}

print(student["name"])
print(student.get("subject"))

student.setdefault("status","pending")
print(student)

student.update({"marks": 55})
print(student)