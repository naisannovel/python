# input() - take input
name = input('what is your name: \n')   # \n use for new line
print(name)
# print input string

# len() - get length
full_name = 'naisan novel'
length = len(full_name)     # len func use for get length
print(length)
# 12
my_name = 'naisan novel'
print(my_name[0])   # n
print(my_name[len(my_name)-1])   # l

# float() - get floating num
age = 24
print(float(age))
# 24.0

# int() - get int num
total = 150.25
print(int(total))
# 150

# str() - convert string
age = 24
print(str(age))
# 24

# print() - end, sep
print('hello', end=' ')
print('world')
# hello world

print('i', 'am', 'naisan', sep=',')
# i,am,naisan

# f-string
n = 'hasan'
print(f'akib {n}')  # akib hasan


# importance
# left to right
# ()
# **
# * /
# + -

print(3 * 3 + 3 / 3 - 3)
# 7.0
