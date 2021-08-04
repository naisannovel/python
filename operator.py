# operator
# arithmetic operator
# +, -, *, /, %
print(20+10)    # 30
print(20-10)    # 10
print(20*10)    # 200
print(20/10)    # 2.0 (floating output)
print(20//10)   # 2 (int output)
print(float(20//10))   # 2.0 (floating output for float func)
print(int(20/10))   # 2 (int output for int func)
print(20 % 10)    # 0
print(3**3)       # 3 to the power 3. 3*3*3=27

# relational or comparison operator
# >, <, ==, <=, >=, !=
print(10 > 20)      # false
print(10 < 20)      # true
print(10 == 20)     # false
print(10 <= 20)     # true
print(10 >= 20)     # false
print(10 != 20)     # true

# logical operator
# and, or, not
print(10 > 5 and 5 < 9)
# true
print(10 < 5 or 15 > 7)
# true
print(not 10 > 20)
# true

# assignment operator
# =
age = 24
age += 1
print(age)
# 25
age -= 1
print(age)
# 24

# identity operator
# is, in
n = 10
m = 10
o = 20
print(n is m)   # true
print(n is o)   # false
print(n is not o)   # true

name = 'naisan'
print('n' in name)  # true
print('m' in name)  # false
print('p' not in name)  # true
