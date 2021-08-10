# class
class Point:
    def __init__(self, x, y):
        self.a = x
        self.b = y

    def move(self):
        print('move')

    def draw(self):
        print(f'draw {self.a}')


point = Point(10, 20)
point.draw()
print(point.a)

# inheritance


class Mamal:
    def walk(self):
        print('walk')


class Dog(Mamal):
    pass


class Cat(Mamal):
    def eat(self):
        print('eat')


dog = Dog()
dog.walk()
cat = Cat()
cat.walk()
cat.eat()