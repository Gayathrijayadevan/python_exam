def add_books(books):
        book_id=int(input("Enter  book id:"))
        book_name=input("Enter  book name:")
        author=input("Enter author name:")
        dop=input("Enter date of publishment:")
        genres=input("Enter the books genres:")
        stock=int(input("Enter stock:"))
        price=int(input("Enter price of book:"))
        books.append({'b_id': book_id,'b_name':book_name,'b_author':author,'date_pulished':dop,'b_genres':genres,'b_stock':stock
                    ,'b_price':price}) 
        
def display_books(books):
    print("{:<10}{:<20}{:<20}{:<20}{:<15}{:<10}{:<15}".format("Book_Id","Book_Name", "Author", "Date_ pulished", "Genres", "Stocks", "Price"))
    print('_' * 90)
    for i in books:
        print("{:<10}{:<20}{:<20}{:<20}{:<15}{:<10}{:<15}".format(i['b_id'],i['b_name'], i['b_author'], i['date_pulished'], i['b_genres'], 
                                                           i['b_stock'], i['b_price']))        
        
def update_details(books):
    b = int(input("Enter the id of books to update : "))
    f = 0
    for i in books:
        if i['b_id'] == b :
            new_name = input("Enter new  book name: ")
            if new_name:
                i.update({"b_name": new_name})

            new_author=input("Enter new author name:")
            i.update({'b_author':new_author })
            
            new_dop = input("Enter new date pulished: ")
            i.update({"date_pulished": new_dop})
            
            new_genre = input("Enter new genre: ")
            i.update({"b_genres": new_genre})

            new_stock = input("Enter new no. of stock: ")
            i.update({"b_stock": new_stock})

            new_price = input("Enter new price: ")
            i.update({"b_price": new_price})
           
            f = 1
            print("Details updated successfully.")
            break
    
    if f == 0:
        print("Sorry, this book is not in the dictionary.")

def search_book(books):
    id=int(input("Enter the id of book to search:"))
    print("{:<10}{:<20}{:<20}{:<20}{:<15}{:<10}{:<15}".format("Book_Id","Book_Name", "Author", "Date_ pulished", "Genres", "Stocks", "Price"))
    print('_' * 100)
    for i in books:
        if i['b_id']==id:
            print("{:<10}{:<20}{:<20}{:<20}{:<15}{:<10}{:<15}".format(i['b_id'],i['b_name'], i['b_author'], i['date_pulished'], i['b_genres'], 
                                                           i['b_stock'], i['b_price'])) 
        else:
            print("sorry there is no such book in this dictionary")    

def delete_books(books):
    a=int(input("Enter the id of book to delete:"))
    for i in books:
        if i["b_id"]==a:
            books.remove(i)
        print("This book has been removed from dictionary ")    
        