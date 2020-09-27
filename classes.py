# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
#
# point1 = Point(10, 20)
# print(point1.x)
# point1.draw()
# point1.move()
#
# point2 = Point(34, 67)


# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print(f"{self.name} is talking!")
#
# person1 = Person("Fred")
# person2 = Person("Wilma")
# person1.talk()
# person2.talk()


class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")


dog1 = Dog()
cat1 = Cat()


dog1.walk()
dog1.bark()

cat1.be_annoying()