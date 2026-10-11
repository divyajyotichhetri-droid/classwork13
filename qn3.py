# Library Management System

books = [
    {"title": "Python Basics", "author": "John", "available": True},
    {"title": "Data Science", "author": "Mike", "available": True},
    {"title": "AI Guide", "author": "Sarah", "available": False},
    {"title": "Web Development", "author": "Tom", "available": True},
    {"title": "Database Systems", "author": "Emma", "available": True}
]

def search_book(title):
    for book in books:
        if book["title"].lower() == title.lower():
            return book
    raise ValueError

def borrow_book(title):
    book = search_book(title)

    if book["available"]:
        book["available"] = False
        print("Book borrowed successfully.")
    else:
        print("Book is already borrowed.")

def return_book(title):
    book = search_book(title)
    book["available"] = True
    print("Book returned successfully.")

print("Available Books:")
for book in books:
    if book["available"]:
        print(book["title"])

try:
    title = input("Enter book title: ")
    borrow_book(title)

    choice = input("Return book? (yes/no): ")
    if choice.lower() == "yes":
        return_book(title)

except ValueError:
    print("Book doesnot exist.")
    