try:
    age = int(input('age: '))
    print(age + 4)
except ValueError:
    print('invalid value')
# except OtherError:
#     print('other error message')
