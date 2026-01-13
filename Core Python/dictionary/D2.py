student = {
    "name": "Jay",
    "subject": "python",
    "marks": 45,
}

print(student.items())
print(student)

# remove all item from the dicitonary
#student.clear()
print(student)

#remove specific item from the dictionary
student.pop("subject")
print(student)

# remove last inserted item from the dictionary
student.popitem()
print(student) 
