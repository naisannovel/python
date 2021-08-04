# if elif else
naisan = 24
istiak = 25

if naisan > istiak:
    print('naisan is greater than istiak')
elif naisan < istiak:
    print('istiak is greater than naisan')
else:
    print('they are equal')


# short circuit
name = 'naisan'
# 1
default_name = name or 'guest'
print(default_name)     # depend on name var
# 2
name and print(name.upper())    # depend on name var


# ternary operator
a, b = 40, 30
min = a if a < b else b
print(min)  # 30

full_name = ''
user = full_name if full_name != '' else 'Guest'
print(user)     # Guest
