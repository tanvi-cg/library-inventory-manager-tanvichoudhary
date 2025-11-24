class Book:
    def __init__(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def __str__(self):
        return f"{self.title} by {self.author} | ISBN: {self.isbn} | Status: {self.status}"

    def issue(self):
        if self.status == "available":
            self.status = "issued"
            return True
        return False

    def return_book(self):
        if self.status == "issued":
            self.status = "available"
            return True
        return False


class LibraryInventory:
    def __init__(self, filename="library_data.txt"):
        self.filename = filename
        self.books = []
        self.load_data()

    def add_book(self, book):
        self.books.append(book)
        self.save_data()

    def search_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def search_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def display_all(self):
        if not self.books:
            print("No books in the library.")
            return
        for book in self.books:
            print(book)

    def save_data(self):
        try:
            with open(self.filename, "w") as file:
                for book in self.books:
                    line = f"{book.title},{book.author},{book.isbn},{book.status}\n"
                    file.write(line)
        except Exception:
            print("Error saving data.")

    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    if len(parts) == 4:
                        title, author, isbn, status = parts
                        book = Book(title, author, isbn, status)
                        self.books.append(book)
        except FileNotFoundError:
            print("No existing file found. Starting fresh.")
        except Exception:
            print("Error loading data.")

def main():
    inventory = LibraryInventory()

    while True:
        print("\n===== Library Menu =====")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Search Book")
        print("5. View All Books")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")

            new_book = Book(title, author, isbn)
            inventory.add_book(new_book)
            print("Book added successfully!")

        elif choice == "2":
            isbn = input("Enter ISBN to issue: ")
            book = inventory.search_by_isbn(isbn)

            if book:
                if book.issue():
                    inventory.save_data()
                    print("Book issued successfully!")
                else:
                    print("Book is already issued.")
            else:
                print("Book not found.")

        elif choice == "3":
            isbn = input("Enter ISBN to return: ")
            book = inventory.search_by_isbn(isbn)

            if book:
                if book.return_book():
                    inventory.save_data()
                    print("Book returned successfully!")
                else:
                    print("Book is not issued.")
            else:
                print("Book not found.")

        elif choice == "4":
            print("\nSearch by:")
            print("1. Title")
            print("2. ISBN")
            search_choice = input("Enter choice: ")

            if search_choice == "1":
                title = input("Enter title: ")
                results = inventory.search_by_title(title)

                if results:
                    print("\nSearch Results:")
                    for b in results:
                        print(b)
                else:
                    print("No books found.")

            elif search_choice == "2":
                isbn = input("Enter ISBN: ")
                book = inventory.search_by_isbn(isbn)

                if book:
                    print(book)
                else:
                    print("Book not found.")

        elif choice == "5":
            print("\nAll Books:")
            inventory.display_all()

        elif choice == "6":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()