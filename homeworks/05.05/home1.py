class Book:
    def __init__(self, title, author, num_pages, book_type):
        self.title = title.strip()
        self.author = author.strip()
        self.num_pages = int(num_pages)
        self.book_type = book_type.strip()

    def print_info(self):
        print(f"{self.title}, {self.author}, {self.num_pages}, {self.book_type}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def print_books(self):
        print("Books in the library:")
        for book in self.books:
            book.print_info()

    def borrow_book(self, title):
        title = title.strip().lower()
        for book in self.books:
            if book.title.lower() == title:
                self.books.remove(book)
                return book
        return None



def main():
    lib = Library()

    with open("books.txt", "r") as file:
        for line in file:
            title, author, num_pages, book_type = line.split(",")
            lib.add_book(Book(title, author, num_pages, book_type))

    lib.print_books()

    while True:
        title = input("Enter the title of the book you want to borrow: ")
        borrowed_book = lib.borrow_book(title)

        if borrowed_book:
            print(f"The book {borrowed_book.title} successfully borrowed!\n")
            lib.print_books()
            break
        else:
            print("Cannot find such book, try again!")



main()
