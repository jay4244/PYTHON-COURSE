student = {
    "name": "Jay",
    "subject": "python",
    "marks": 45,
}
print(student)

# fetching keys using key
print(student.keys())

# fetching value using key
print(student.values())

print("-----------------------")
# fetching keys by loop

for k in student.keys():
    print(k)
    
# fetching values by loop

for v in student.values():
    print(v)    