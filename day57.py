class person:
    name = "harry"
    occupations = "software_developer"
    networth = 10

    def info(self):
        print(f"{self.name} is a {self.occupations}")


a = person()
a.name = "shravan"
a.occupations = "hacker"
# print(a.name, a.occupations)
b = person()
b.name = "kruti"
b.occupations = "hr"

a.info()
b.info()
