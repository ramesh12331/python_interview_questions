try:
    print(10/0)
except ZeroDivisionError:
    print("Inavalid")
finally:
    print("Valid")
# ============================
class Animal:
    def sound(self):
        print("animal")

class Dog(Animal):
    def sound(self):
        print("bow")

class Cat(Dog):
    def meow(self):
        print("meow")

d= Dog()
d.sound()
