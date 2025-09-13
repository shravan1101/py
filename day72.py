class Parentclass:
    def parent_method(self):
        print("this is the parent method ")


class childClass(Parentclass):
    def parent_method(self):
        print("shravan")
        super().parent_method()

    def child_method(self):
        print("this is called method")
        super().parent_method()  # it call the parent functioms


d = childClass()
d.child_method()
d.parent_method()


class Employe:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Prpgrammer(Employe):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang


tanvir = Employe("tanvir", "12")
shravan = Prpgrammer("shravan", "23", "python ")

print(shravan.name)
print(shravan.id)
print(shravan.lang)
