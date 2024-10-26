from functionality import *
books=[]
while True:
    print("\n1.Add Book \n 2.Display Books \n 3.Update  Book Details \n 4.Search Book\n 5.Delete Books \n 6.exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        add_books(books)
        print('details added')
    elif ch==2:
        display_books(books)
    elif ch==3:
        update_details(books)  
    elif ch==4:
        search_book(books)
    elif ch==5:
        delete_books(books)
    elif ch==6:
        break   