class Book:
    def __init__(self , title: str , author : str , isbn : int , is_borrowed : bool):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = is_borrowed

    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {'Borrowed' if self.is_borrowed else 'Available'}"

class Library_Management:

    def __init__(self):
         self.list_of_book = [
            Book("Python Crash Course", "Eric Matthes", 9781593279288, False),
            Book("Clean Code", "Robert C. Martin", 9780132350884, True),
            Book("Artificial Intelligence", "Stuart Russell", 9780136042594, False),
            Book("Think Python", "Allen B. Downey", 9781491939369, False),
            Book("Fluent Python", "Luciano Ramalho", 9781491946008, True)
        ]
         
    def Add_book(self , book : Book):
        self.list_of_book.append(book)

    def Remove_book(self, title : str):
        self.list_of_book = [book for book in self.list_of_book if book.title != title ]

    def list_books(self):
        return self.list_of_book

    def Search_book(self, author : str , title : str):
        return [book for book in self.list_of_book if book.title == title or book.author == author]

    def is_borrowed(self, title: str):
        for book in self.list_of_book:
            if book.title == title:
                return book.is_borrowed
        return None 

library = Library_Management()  
for book in library.list_books():  
    print(book)

