from Book import Book
from Library import Library

def main():
    book = Book("9;Animal Farm;Orwell George;Available")
    print(book, end='\n\n')

    library = Library("data.txt")
    print(library, end='\n\n')

    library.add_book(book)
    print()

    book.set_id(library.get_unique_id())
    library.add_book(book)
    print()

    print("Dostupné knihy:")
    library.show_available_books()
    print()

    print("Pujceni knihy:")
    library.find_book_and_borrow_it("Kill")
    print()
    library.find_book_and_borrow_it("a")
    print()
    library.find_book_and_borrow_it("Great")
    print()

    print("Dostupné knihy:")
    library.show_available_books()
    print()

if __name__ == "__main__":
    main()
