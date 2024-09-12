books=[]

def add_books():
        
        b_no=int(input("Enter book number:"))
        name=input("Enter book name:")
        a_name= input("Enter author name:")
        price= int(input("Enter book price:"))
        
        books.append({'book_no':b_no,'book_name': name,'author_name': a_name,'b_price': price})


def update_books() :
    name=input("Enter book name:")
    f=0
    for i in books:
        if  i["book_name"]==name:
            n_name=input("Enter the new  book name:")
            i.update({'book_name':n_name})

            au_name=input("enter the new author name:")
            i.update({'author_name':au_name})

            price= int(input("enter the new price:"))
            i.update({'b_price':price})
            f=1

    if f==0:   
            print("sorry invalid book name,try again")   


def remove_book():
    book_num=int(input("Enter the book number of the book to be deleted:"))
    for i in books:
        if i["book_no"]==book_num:
            books.remove(i)
            break
        else:
            print("invalid book number")   


def display_books():
    for i in books:
        print("{:<15}{:<20}{:<20}{:<10}".format("book number","book name","author","price"))
    print('_'*50)
    for i in books:
        print(("{:<15}{:<20}{:<20}{:<10}").format(i['book_no'],i['book_name'],i['author_name'],i['b_price']))


def search_books():
    s_name=input("enter book name to search:")
    for i in books:
        if s_name in i[' book_name']:
                print(i)

