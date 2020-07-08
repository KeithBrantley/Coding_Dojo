# Object Orientated Programming

class User:
    # Properties - Define the class
    def __init__(self, n, h, hc, a):
        self.name = n
        self.height = h
        self.hair_color = hc
        self.age = a

    # Methods - What our class can do
    def say_hello(self, person):
        print(f"Hello {person.name} my name is {self.name}!")

John = User("John", 6, 'Brown', 23)
Becky = User("Becky", 5, 'Blonde', 31)
Billy_Bobby = User(h=4, n='Billy Bobby', hc='Red', a=50)
Becky.say_hello(Billy_Bobby)
Billy_Bobby.say_hello(Becky)