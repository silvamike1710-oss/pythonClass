def loanMultipleBooks():
    title = input("Title to loan: ").strip()
    
    try:
        amount_to_loan = int(input("How many copies to loan: ").strip())
        if amount_to_loan <= 0:
            print("Amount must be greater than 0")
            return
    except ValueError:
        print("Invalid number")
        return
    
    for book in books:
        if book["title"].lower() == title.lower():
            available = book["quantity"] - book["loaned_count"]
            
            if amount_to_loan > available:
                print(f"Can't loan {amount_to_loan}. Only {available} available")
                return
            
            book["loaned_count"] += amount_to_loan
            new_available = book["quantity"] - book["loaned_count"]
            print(f"Loaned {amount_to_loan} copies of {title}")
            print(f"Remaining available: {new_available}")
            return
    
    print("Book not found")