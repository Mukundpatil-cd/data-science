class book:
    def __init__(self, title, author, isbn, copies):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.copies=copies
    
    def display_books(self):
        print(f"{self.title} by {self.author} | {self.isbn} | {self.copies}")

        

class user:
    def __init__(self,name , userid):
        self.name=name
        self.userid=userid
    
    def display_user_info(self):
        print(f"user {self.name} ID : {self.userid}")

        

class member(user):
    def __init__(self,name , userid):
        super().__init__(name , userid)
        self.borrowed_books=[]
        
    def display_user_info(self):
        print(f"user {self.name} ID : {self.userid} borrowed {len(self.borrowed_books)} books")

    def borrow_book(self, library, isbn):
        for book in library.books:
            if book.isbn == isbn and book.copies > 0:
                book.copies -= 1
                self.borrowed_books.append(book)
                print(f"{self.name} borrowed '{book.title}'.")
                return
        print("Book not available.")

    def return_book(self, library, isbn):
        for book in self.borrowed_books:
            if book.isbn == isbn:
                book.copies += 1
                self.borrowed_books.remove(book)
                print(f"{self.name} returned '{book.title}'.")
                return
        print("You don't have this book.")
        
class staf(user):
    def __init__(self, name, userid):
        super().__init__(name, userid)
    
    def display_user_info(self):
        print(f"Staff: {self.name}, ID: {self.userid}")
    def add_book_to_library(self, library, book):
        library.add_books(book)
    
    def remove_book_from_library(self, library, isbn):
        library.remove_book(isbn)
        
        
class library:
    def __init__(self):
        self.books = []
    
    def display_books(self):
        if not self.books:
            print("No books available.")
        else:
            for book in self.books:
                book.display_books()
                
    def add_books(self,books):
        self.books.append(books)
        print(f"'{books.title}' added to the library")
        
    def remove_book(self,isbn):
        for b in self.books:
            if b.isbn == isbn :
                self.books.remove(b)
                print(f"Book '{b.title}' removed from the library.")
                return
        print("Book not found.")
                
Library = library()

staff = staf("Admin", "S001")
Member = member("John Doe", "M001")

while True:
    print("\n=== Library Management System ===")
    print("1. Login as Staff")
    print("2. Login as Member")
    print("3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        while True:
            print("\n--- Staff Menu ---")
            print("1. Add Book")
            print("2. Remove Book")
            print("3. Display Books")
            print("4. Search Book")
            print("5. Back")
            staff_choice = input("Enter choice: ")

            if staff_choice == "1":
                title = input("Enter book title: ")
                author = input("Enter author: ")
                isbn = input("Enter ISBN: ")
                copies = int(input("Enter number of copies: "))
                new_book = book(title, author, isbn, copies)
                staff.add_book_to_library(Library, new_book)


            elif staff_choice == "2":
                isbn = input("Enter ISBN to remove: ")
                staff.remove_book_from_library(Library, isbn)

            elif staff_choice == "3":
                Library.display_books()

            elif staff_choice == "4":
                title = input("Enter title to search: ")
                
                found = False
                for b in Library.books:
                    if title.lower() in b.title.lower():
                        b.display_books()
                        found = True
                if not found:
                    print("Book not found.")

            elif staff_choice == "5":
                break
            else:
                print("Invalid choice.")

    elif choice == "2":
        while True:
            print("\n--- Member Menu ---")
            print("1. Borrow Book")
            print("2. Return Book")
            print("3. Display Books")
            print("4. Search Book")
            print("5. Back")
            member_choice = input("Enter choice: ")

            if member_choice == "1":
                isbn = input("Enter ISBN to borrow: ")
                Member.borrow_book(Library, isbn)

            elif member_choice == "2":
                isbn = input("Enter ISBN to return: ")
                Member.return_book(Library, isbn)

            elif member_choice == "3":
                Library.display_books()

            elif member_choice == "4":
                title = input("Enter title to search: ")
                # Search functionality
                found = False
                for b in Library.books:
                    if title.lower() in b.title.lower():
                        b.display_books()
                        found = True
                if not found:
                    print("Book not found.")

            elif member_choice == "5":
                break
            else:
                print("Invalid choice.")

    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")            