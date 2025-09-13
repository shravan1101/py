class Library:
    def __init__(self):
        self.no_book = 0
        self.book = []

    def add_book(self, book):
        self.book.append(book)
        self.no_book = len(self.book)

    def showInfo(self):
        print(f"book are {self.book} and the number of book are {self.no_book}")


l1 = Library()
l1.add_book("python")
l1.add_book("python")
l1.add_book("python")
l1.showInfo()



# class Library:
#     def __init__(self):
#         self._books = []  # private attribute

#     # 👉 Getter for books
#     @property
#     def books(self):
#         return self._books

#     # 👉 Setter for books
#     @books.setter
#     def books(self, book):
#         self._books.append(book)

#     # 👉 Getter for number of books
#     @property
#     def no_books(self):
#         return len(self._books)

#     def showInfo(self):
#         print(f"Books are {self.books} and the number of books are {self.no_books}")

# # Using the class
# l1 = Library()
# l1.books = "Python"   # setter is called here
# l1.books = "C++"      # setter is called again
# l1.showInfo()         # uses the getter for books and no_books
