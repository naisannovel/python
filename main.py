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

# round()
print(round(3.443))     # 3
print(round(3.5445))    # 4
print(round(3.554444, 2))   # 3.55

print(4 / 2)   # 2.0
print(4 // 2)   # 2

print("{:.2f}".format(20))      # 20.00

# lower case and upper case
name = 'naisan'
print(name.upper())

name = 'NOVEL'
print(name.lower())

full_name = 'naisan novel'
print(full_name.count('a'))     # 2
print(full_name.count('n'))     # 3


# max()
scores = [54, 25, 35, 91, 9, 18, 29]
max_score = max(scores)
print(max_score)

# sum()
total = [54, 25, 35, 91, 9, 18, 29]
total_num = sum(total)
print(total_num)

# min()
lowest = [54, 25, 35, 91, 9, 18, 29]
lowest_num = min(lowest)
print(lowest_num)
