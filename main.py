from users import *
from function import *

while True:
    print("\n Welcome To Library Management System")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice =  int(input("  Please enter your choice: "))

    if choice == 1:
        username = input("Enter Username: ")
        password = input("Set a Password: ")
        if register_user(username, password):
            print("Registration successful!")
        else:
            print("Username already exists.")
    
    elif choice == 2:
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        if login_user(username, password):
            print("Login successful!")

            while True:
                print("\n Welcome To  The Library Management System")
                print("1.Add books")
                print("2. Update book")
                print("3.Remove book")
                print("4. View all books")
                print("5. search book")
                print("6. Exit")

            a=int(input("Select an option:")) 
            if a==1:
                add_books()
            elif a==2:
                update_books() 
            elif a==3:
                remove_book()
            elif a==4:
                display_books()
            elif a==5:
                search_books() 
            elif a== 6:
                break
            else:
                print("invalid option")  

    elif choice == 3:
        print("Thank you for visting library management system")
        break

    else:
        print("Invalid choice. Please try again.")