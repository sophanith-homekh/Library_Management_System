import json
import os

# File to store books
BOOK_FILE = "books.json"

# Load books from JSON file
def load_books():
    """Load books from JSON file. If file doesn't exist or is empty, return empty list."""
    if not os.path.exists(BOOK_FILE):
        return []
    with open(BOOK_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

# Save books to JSON file
def save_books(books):
    with open(BOOK_FILE, "w") as file:
        json.dump(books, file, indent=4)

# Create a new book
def create_book():
    books = load_books()
    book = {}
    book["id"] = input("Enter book ID: ")
    book["title"] = input("Enter book title: ")
    book["author"] = input("Enter author name: ")
    books.append(book)
    save_books(books)
    print("Book added successfully!\n")

# Read / View all books
def read_books():
    books = load_books()
    if not books:
        print("No books found.\n")
        return
    print("\n--- Book List ---")
    for book in books:
        print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}")
    print("----------------\n")

# Update a book
def update_book():
    books = load_books()
    book_id = input("Enter book ID to update: ")
    for book in books:
        if book["id"] == book_id:
            book["title"] = input(f"Enter new title ({book['title']}): ") or book["title"]
            book["author"] = input(f"Enter new author ({book['author']}): ") or book["author"]
            save_books(books)
            print("Book updated successfully!\n")
            return
    print("Book not found!\n")

# Delete a book
def delete_book():
    books = load_books()
    book_id = input("Enter book ID to delete: ")
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            save_books(books)
            print("Book deleted successfully!\n")
            return
    print("Book not found!\n")

# Main menu
def menu():
    while True:
        print("=== Library Book System ===")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            create_book()
        elif choice == "2":
            read_books()
        elif choice == "3":
            update_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

# Run the program
if __name__ == "__main__":
    menu()