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

n = input('score')
sc = n.split(' ')
h = 0
for nu in sc:
    tn = int(nu)
    if h < tn:
        h = tn

print(h)

total = 0

for n in range(1, 5):
    total += n

print(total)

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)
