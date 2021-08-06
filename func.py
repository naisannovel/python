# function

def my_func():
    print('hello, i am naisan')


my_func()   # hello, i am naisan


def sum_num(a, b):
    return a + b


result = sum_num(2, 3)
print(result)   # 5


# global scope and local scope
def func1():
    a = 10
    print(a)


# print(a)    # error because a is local var
func1()     # 10


def func2():
    global b    # using global keyword we can create global var in local scope
    print(b)


b = 25
func2()     # 25
print(b)
