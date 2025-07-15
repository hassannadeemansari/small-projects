import streamlit as st

# --- Your Book and Library_Management classes ---
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

# --- Streamlit Interface ---
st.set_page_config(page_title="📚 Library Manager", layout="centered")
st.title("📚 Personal Library Management System")

library = Library_Management()

menu = st.sidebar.selectbox("Choose Action", ["List All Books", "Add Book", "Search Book", "Remove Book", "Check if Borrowed"])

if menu == "List All Books":
    st.subheader("📖 All Books")
    for book in library.list_books():
        st.write(str(book))

elif menu == "Add Book":
    st.subheader("➕ Add a New Book")
    title = st.text_input("Book Title")
    author = st.text_input("Author Name")
    isbn = st.number_input("ISBN", step=1)
    is_borrowed = st.checkbox("Is Borrowed?")
    if st.button("Add Book"):
        if title and author:
            new_book = Book(title, author, isbn, is_borrowed)
            library.Add_book(new_book)
            st.success(f"Book '{title}' added!")
        else:
            st.error("Please provide both title and author.")

elif menu == "Search Book":
    st.subheader("🔍 Search Book")
    title = st.text_input("Title to Search")
    author = st.text_input("Author to Search")
    if st.button("Search"):
        results = library.Search_book(author, title)
        if results:
            for book in results:
                st.write(str(book))
        else:
            st.warning("No matching books found.")

elif menu == "Remove Book":
    st.subheader("🗑️ Remove Book by Title")
    title = st.text_input("Enter Title to Remove")
    if st.button("Remove"):
        library.Remove_book(title)
        st.success(f"Book '{title}' removed (if existed).")

elif menu == "Check if Borrowed":
    st.subheader("🔐 Check Borrowed Status")
    title = st.text_input("Enter Title to Check")
    if st.button("Check"):
        status = library.is_borrowed(title)
        if status is True:
            st.warning(f"'{title}' is currently borrowed.")
        elif status is False:
            st.success(f"'{title}' is available.")
        else:
            st.error("Book not found.")
