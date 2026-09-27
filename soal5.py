books={}
while True:
    command= input("enter command:")
    if command=="add":
        bookname=input("enter bookname:") 
        author=input("enter author:")
        books[bookname]=author
        print("book added")
    elif command=="search":
         bookname=input("enter bookname:") 
         if bookname in books:
             print(f"Author is {books[bookname]}")
         else:
             print("this book doesnt exist.")
    elif command=="show":
        if len(books)==0:
            print("no books available")
        else:
            for bookname, author in books.items():
                print( bookname, "-" ,author)
    elif command=="exit":
        break
    else:
        print("invalid input")

