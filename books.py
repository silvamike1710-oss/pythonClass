books = [
    {"title": "Dune", "author": "Frank Herbert", "amount": 10, "loaned": 7},
    {"title": "Project Hail Mary", "author": "Andy Weir", "amount": 4, "loaned": 4},
    {"title": "Journey to the Center of the Earth", "author": "Jules Verne", "amount": 5, "loaned": 2}
]

def addBook():
    title = input("Title: ").strip()
    author = input("Author: ").strip()

    for book in books:
        if book["title"].lower() == title.lower():
            print("Book already in library")
            return
    
    books.append({"title": title, "author": author, "amount": 1, "loaned": 0})
    print("Book added.")

def listBook():
    if not books:
        print("Library empty")
        return
    
    print("\n-- Books --")
    for book in sorted(books, key=lambda x: x["title"]):
        available = book["amount"] - book["loaned"]
     
        print(f"{book['title']} - {book['author']} - Available: {available}/{book['amount']}")

def removeBook(): 
    title = input("Title to remove: ").strip()

    for book in books:
        if book["title"].lower() == title.lower():
            books.remove(book)
            print("Book removed.")
            return
    print("Book not found")

def loanBook():
    title = input("Title to loan: ").strip()

    try:
        amount_to_loan = int(input("How many to loan: "))
        if amount_to_loan <= 0:
            print("Must be higher than zero.")
            return
    except ValueError:
        print("Invalid number")
        return
    
    for book in books:
        if book["title"].lower() == title.lower():
            available = book["amount"] - book["loaned"]

            if amount_to_loan > available:
                print(f"Can't loan {amount_to_loan}. Only {available} available.")
                return
            
            book["loaned"] += amount_to_loan
            print(f"Loaned {amount_to_loan} copies of '{title}'.")
            print(f"Remaining: {book['amount'] - book['loaned']}")
            return

    print("Book not available")

def loanHistory():
    loaned = [book for book in books if book["loaned"] > 0]

    if not loaned:
        print("No loaned books")
        return

    print("\n-- Loaned Books --")
    print(f"Total: {len(loaned)}")
    print("-" * 25)

    for book in sorted(loaned, key=lambda x: x["title"]):
        print(f"{book['title']} by {book['author']}")

def returnBook():
    title = input("Title for return: ").strip()

    for book in books:
        if book["title"].lower() == title.lower():
            if book["loaned"] > 0:
                book["loaned"] -= 1
                print(f"'{title}' returned.")
            else:
                print("No copies loaned.")
            return
        
    print("No such title found.")

def updateBook():
    title = input("Title to update: ").strip()

    for book in books:
        if book["title"].lower() == title.lower():
            try:
                new_amount = int(input("New total amount: "))
               
                if new_amount < 0:
                    print("Invalid amount. Must be zero or greater.")
                    return
             
                if new_amount < book["loaned"]:
                    print(f"Cannot set amount lower than copies already loaned ({book['loaned']}).")
                    return
            except ValueError:
                print("Invalid number.")
                return

            book["amount"] = new_amount
            print("Book updated.")
            return
       
    print("Book not available")

def menu():
    while True:
        print("\n--- MENU ---")
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