# variable
a = 10
c, d = 10, 20

# take input
name = input('what is your name: \n')   # \n use for new line
# print name variables
print(name)

# list = array
li = [1, 2, 3, 4]

# set don't take duplicate data
print(type(li))
print(len(li))
se = {1, 2, 3}

# tuple must take 2 elements
tup = (1, 2, 3)

# dictionary = object
di = {
    'name': name,
    'age': 25
}
print(di)


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

print(10 > 20)      # false
print(10 < 20)      # true
print(10 == 20)     # false
print(10 <= 20)     # true
print(10 >= 20)     # false
print(10 != 20)     # true
