#BOOK MANAGEMENT SYSTEM
print("------- LIBRARY BOOK MANAGEMENT SYSTEM -------")

# list to store all books
library = []

# function to add a book
def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    
    book = {
        "ID": book_id,
        "Title": title,
        "Author": author,
        "Status": "Available"
    }
    
    library.append(book)
    print("Book added successfully!")

# function to display all books
def display_books():
    if len(library) == 0:
        print("No books in the library!")
    else:
        print("\n---- All Books ----")
        for book in library:
            print(f"ID: {book['ID']}, Title: {book['Title']}, Author: {book['Author']}, Status: {book['Status']}")

# function to issue a book
def issue_book():
    book_id = input("Enter Book ID to issue: ")
    for book in library:
        if book["ID"] == book_id:
            if book["Status"] == "Available":
                book["Status"] = "Issued"
                print("Book issued successfully!")
            else:
                print("Book is already issued!")
            return
    print("Book not found!")

# function to return a book
def return_book():
    book_id = input("Enter Book ID to return: ")
    for book in library:
        if book["ID"] == book_id:
            if book["Status"] == "Issued":
                book["Status"] = "Available"
                print("Book returned successfully!")
            else:
                print("This book was not issued.")
            return
    print("Book not found!")

# main menu loop
while True:
    print("\n------ MENU ------")
    print("1. Add Book")
    print("2. Display All Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        display_books()

    elif choice == "3":
        issue_book()

    elif choice == "4":
        return_book()

    elif choice == "5":
        print("Exiting... Thank you!")
        break

    else:
        print("Invalid choice! Try again.")
