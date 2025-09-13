class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromstr(cls, string):   # cls in the class in this case Employee and it returns agr to default construtor or def __inti__()
        return cls(string.split(" ")[0], string.split(" ")[1])


e1 = Employee("shrava", "20000")
print(e1.name)
print(e1.salary)

str = "shravan 20000"
e2 = Employee.fromstr(str)
print(e2.name)
print(e2.salary)