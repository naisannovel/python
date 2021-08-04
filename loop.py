# while loop

res = 'y'
while res == 'y':
    num1 = int(input('Enter your age: '))
    num2 = int(input('Enter your roll: '))
    print('result =', str(num1 + num2))
    res = input('do you want to continue? (y/n)')

# for loop
num = 0
for n in range(11):
    num += n
print(num)

name = 'naisan novel'
for l in name:
    print(l, end='\n')


# break and continue
for i in range(1, 11):
    if i == 5: break
    print(i)

for j in range(1, 11):
    if j == 5: continue
    print(j)
