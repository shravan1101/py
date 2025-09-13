class Employe:
    company = "apple"

    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"name is {self.name} and company is {self.company}")

    # def change_company(
    #     cls, newCompany  ):  # it will not change the class variable but the instance variable
    #     cls.company = newCompany
    # but now it will chage the class variable

    @classmethod
    def change_company(cls, newCompany):  # it will  change the class variable
        cls.company = newCompany


e1 = Employe("shravan")
e1.show()

e2 = Employe("sarvesh")
e2.change_company("nakiya")
e2.show()  # it will chage the instance variable not the class variable


print(Employe.company)
