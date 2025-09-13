class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("sound made by the animal ")


class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="dog")
        self.breed = breed

    def make_sound(self):
        print("bark")


d = Dog("dog", "lab")
d.make_sound()

a = Animal("dog", "dog")
a.make_sound()
