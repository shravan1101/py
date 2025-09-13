class employ:
    company_name = "google"  # class variable
    no_emp = 0

    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.25  # instace variable
        employ.no_emp += 1

    def show(self):
        print(
            f"the name of the Employe is {self.name} and the rasie is amount is {self.raise_amount} is in {self.company_name} employe mo {employ.no_emp}"
        )


# employ.show(emp1)
emp1 = employ("shravan")
emp1.company_name = "google india"  # instace variable
emp1.show()

emp2 = employ("sarvehs")
emp2.company_name = "you tube"  # instace variable
emp2.show()

emp3 = employ("sachin")  # instace variable
emp3.show()
