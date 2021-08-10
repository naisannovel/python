student = {
    "name": "naisan",
    "age": 24,
    "color": "black"
}
print(student)  # print dictionary

for key in student:
    print(key)
    print(student[key])

print("name" in student)    # True

print(student["name"])      # naisan
print(student["age"])       # 24
print(student["color"])     # black

print(student.get('name'))
print(student.get('subject', 'biology'))
# if subject key not found in student dictionary.then it will return None. so here we can set default value

x = {
    "1": "one",
    "2": "two",
    "3": "three"
}

y = (input('> '))
msg = ''
for a in y:
    z = x.get(a, '!')
    msg += f'{z} '
print(msg)
