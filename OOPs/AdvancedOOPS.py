# advanced concepts of OOPS in Python
class pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I Don't know what to say")


class Cat(pet):

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print("Iam {self.name} and I am {self.age} years old and I am {self.color}")


class Dog(pet):

    def speak(self):
        print("Bark")

    def show(self):
        print()


class Fish(pet):
    pass


p = pet("tim", 19)
p.speak()
c = Cat("bill", 34, "brown")
c.show()
d = Dog("jill", 25)
d.speak()
f = Fish("bubbles", 10)
f.speak()
