
books = [
    {"title": "Dune", "author": "Frank Herbert", "amount": 10, "loaned": 7},
    {"title": "Project Hail Mary", "author": "Andy Weir", "amount": 4, "loaned": 4},
    {"title": "Journey to the Center of the Earth", "author": "Jules Verne", "amount": 5, "loaned": 2}
]

def addBook():
    title = input("Title: ").strip()
    author = input("Author: ").strip()

#check for dupkicates
    for book in books:
        if book["title"].lower() == title.lower():
            print("Books already in library")
            return
    
    books.append({"title": title, "author": author, "amount": 1, "loaned": 0})
    print("Book added.")

def listBook():
    if not books:
        print("Library empty")
        return
    
    print("\n-- Books --")
    #order by title key
    for book in sorted(books, key=lambda x: x["title"]):
        status = f"{book['loaned']}/{book['amount']} loaned"
        amount = "amount"
        print(f"{book['title']} by {book['author']} - {status}")

def removeBook(): 
    title = input("Title to remove: ").strip()

    for book in books:
        if book["title"].lower() == title.lower():
            books.remove(book)
            print("Book removed.")
            return
    print("Book not found")

def loanBook():
    title = input("title to loan: ").strip()

    for book in books:
        if book["title"].lower() == title.lower():
            if book["loaned"] < book["amount"]:
                book["loaned"] += 1
                print("Book loaned")
            else:
                print("No copies available.")
            return
       
    print("Book not available")

def loanHistory():
    loaned = [book for book in books if book["loaned"]]

    if not loaned:
        print("no loaned books")
        return
    print("\n - loaned -")
    print(f"Loaned books: {len(loaned)}")
    print("-" * 25)

    for book in sorted(loaned, key=lambda x: x["title"]):
        print(f"{book['title']} by {book['author']}")

def returnBook():
    title = input("Title for return: ").strip()

    for book in books:
        if book["title"].lower() == title.lower():
            if book["loaned"] > 0:
                book["loaned"] -= 1
                print(f"{title} returned.")
            else:
                print("No copies loaned.")
            return
        
    print("No such title found.")

def updateBook():
    title = input("title to loan: ").strip()

    for book in books:
        if book["title"].lower() == title.lower():
            new_status = int(input("New amount: "))
            book["amount"] = new_status
            print("Book updated")
            return
       
    print("Book not available")

def menu():
    while True:
        print("\n---MENU---")
        print("1 - Add book")
        print("2 - Remove book")
        print("3 - List books")
        print("4 - Update book")
        print("5 - Loan book")
        print("6 - Loan history")
        print("7 - Return book")
        print("8 - Exit")
        
        opcao = input("Choose: ").strip()

        if opcao == "1":
            addBook()
        elif opcao == "2":
            removeBook()
        elif opcao == "3":
            listBook()
        elif opcao == "4":
            updateBook()
        elif opcao == "5":
            loanBook()
        elif opcao == "6":
            loanHistory()
        elif opcao == "7":
            returnBook()
        elif opcao == "8":
            print("Closing")
            break
        else:
            print("Invalid option")

menu()