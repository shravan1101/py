class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"the name is {self.name}")


class Dancer:

    def __init__(self, dancer):
        self.dancer = dancer

    def show(self):
        print(f" the dance is {self.dancer}")


class DancerEmployee(
    Dancer, Employee
):  # when you call a the show fun the class written in the braket . there show fun get called
    def __init__(self, name, dance):
        self.name = name
        self.dancer = dance


o = DancerEmployee("shravan", "lungi_dance")

print(o.name)
print(o.dancer)
o.show()
print(DancerEmployee.mro())
