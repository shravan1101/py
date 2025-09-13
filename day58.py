class person:

    def __init__(self, name, occ):
        self.name = name
        self.occ = occ

    # def __init__(self):
    #     print("hwllo")

    def info(self):
        print(f" i am {self.name} and a {self.occ}")


a = person("shravan", "hacker")  # self is the frist arg to pass
b = person("sarvesh", "Hr")
a.info()
b.info()

