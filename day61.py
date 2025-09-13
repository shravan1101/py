class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def show(self):
        print(f"the name of employe  : {self.name} and id {self.id}")


class programer(employee):
    def show_lang(self):
        print("the defalut language is python")


e1 = employee("shravan" ,"12")
e1.show()
e2 = programer("sachin", "01")
e2.show()
e2.show_lang()
