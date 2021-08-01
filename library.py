library = {
    "name": "CodeClan Library",
    "books": [
        {
            "author": "George RR Martin",
            "title": "A Song of Ice and Fire"
        },
        {
            "author": "J R. R. Tolkien",
            "title": "The Hobbit"
        },
        {
            "author": "Paul Barry",
            "title": "Head-First Python"
        },
        {
            "author": "Allen B. Downey",
            "title": "Think Python: How to Think Like a Computer Scientist"
        },
        {
            "author": "Eric Matthes",
            "title": "Python Crash Course"
        }
    ]
}

library_name = library["name"]

print(f"Welcome to the {library_name}. Please see options below.")

option = ""
while option != "q":
    print("Options:")
    print("1 - List all books")
    print("2 - Search for a book by title")
    print("3 - Add a book")
    print("4 - Remove a book")
    print("5 - Update a book")
    print("q - Quit")
    option = input("What would you like to do? ")

    if option == "1":
        print("Listing all books...")
        books = library["books"]
        for book in books:
            print(f"{book['title']} by {book['author']}")
    
    if option == "2":
        print("Searching for a book by title...")

        book_found = False
        
        search_input = input("What book are you looking for? ")
        search = library["books"]    
        for search_item in search:
            if search_item["title"] == search_input:
                book_found = True
                print(f"{search_item['title']} by {search_item['author']}")

        if not book_found:
            print("Book not found.")


    if option == "3":
        print("Adding a book...")
        title = input("Enter title: ")
        author = input("Enter author: ")
        books = library["books"]
        books.append({"author": author, "title": title})
        for book in books:
            print(f"{book['title']} by {book['author']}")


    if option == "4":
        print("Removing a book...")
        remove_book_input = input("Enter title: ")
        books = library["books"] 
     
        book_remove = False   
        for book in books:
            if book["title"] == remove_book_input:
                book_remove = True
                books.remove(book)
                for book in books:
                    print(f"{book['title']} by {book['author']}")


        if not book_remove:
            print("Book not found.")

        

    if option == "5":
        print("Updating a book...")
        update_input = input("Enter title here: ")
        books = library["books"]

        for book in books:
            if book["title"] == update_input:
                title_update = input("Enter new title here: ")
                update_author = input("Enter new author here: ") 
                if title_update and update_author:
                    book["title"] = title_update
                    book["author"] = update_author
                for book in books:
                    print(f"{book['title']} by {book['author']}")

