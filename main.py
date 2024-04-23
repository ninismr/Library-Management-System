from functions.admin_func import *
from functions.borrower_func import *


# constant var to store the admin password
ADMIN_PASSWORD = 'admin'

# multi-line str var to store admin menu
admin_menu = '''

LIBRARY MANAGEMENT SYSTEM
ADMINISTRATOR MENU:

Press
1 to View Books List
2 to View Unavailable/Borrowed Books List
3 to Search Book
4 to Add Book
5 to Update Book
6 to Delete Book
7 to Exit 
'''

# multi-line str var to store borrower menu
borrower_menu = '''

LIBRARY MANAGEMENT SYSTEM
BORROWER MENU:

Press
1 to View Books List
2 to View Unavailable/Borrowed Books List
3 to Search Book
4 to Borrow Book
5 to Return Book
6 to Exit 
'''


# func used to handle the login attempt of the admin user type
def admin_login():
    while True:
        password = input("\nEnter the admin password or press Enter to cancel: ")
        if not password:
            break
        
        if password == ADMIN_PASSWORD:
            print("Login successful.")
            return True
        else:
            print("Incorrect password. Please try again")


# func used to change the user type from borrower to admin w/o re-running the program 
# call the admin_login() func to do the authentication for login
def change_user_to_admin():
    change_user = input("\nDo you want to change the user type to administrator? (yes/no): ").strip().lower()
    while change_user not in ['yes', 'no']:
        print("Invalid input. Please enter 'yes' or 'no'.")
        change_user = input("\nDo you want to change the user type to administrator? (yes/no): ").strip().lower()
    if change_user == 'yes':
        if admin_login():
            admin_menu_choice()
        else: 
            print("The login attempt is canceled.")
            print("\nThank you for visiting! Have a nice day ^-^")
    else: 
        print("\nThank you for visiting! Have a nice day ^-^")


# func used to change the user type from admin to borrower w/o re-running the program
def change_user_to_borrower():
    change_user = input("\nDo you want to change the user type to borrower? (yes/no): ").strip().lower()
    while change_user not in ['yes', 'no']:
        print("Invalid input. Please enter 'yes' or 'no'.")
        change_user = input("\nDo you want to change the user type to borrower? (yes/no): ").strip().lower()
    if change_user == 'yes':
        borrower_menu_choice()
    else: 
        print("\nThank you for visiting! Have a nice day ^-^")


# func used to print the admin menu 
# handle the admin's choice and call the corresponding func to the admin's choice
def admin_menu_choice():
    while True:
        print(admin_menu)
        choice = input("\nEnter your Choice: ")

        if choice == '1':
            view_books_list()
        elif choice == '2':
            view_unavailable_books()
        elif choice == '3':
            search_book()
        elif choice == '4':
            add_book()
        elif choice == '5':
            update_book()
        elif choice == '6':
            delete_book()
        elif choice == '7':
            change_user_to_borrower()
            exit(0)
        else:
            print("Invalid Choice. Try Again")


# func used to print the borrower menu 
# handle the borrower's choice and call the corresponding func to the borrower's choice
def borrower_menu_choice():
    while True:
        print(borrower_menu)
        choice = input("\nEnter your Choice: ")

        if choice == '1':
            view_books_list()
        elif choice == '2':
            view_unavailable_books()
        elif choice == '3':
            search_and_borrow_book()
        elif choice == '4':
            borrow_book()
        elif choice == '5':
            return_book()
        elif choice == '6':
            change_user_to_admin()
            exit(0)
        else:
            print("Invalid Choice. Try Again")


# main() func used to print the very first interface of the program which asks the user's type (admin/borrower)
def main():
    print("\nWELCOME TO THE LIBRARY MANAGEMENT SYSTEM ^-^")
    while True:
        user_type = input("\nAre you an admin or a borrower? (admin/borrower) or type 'exit' to close the program: ").lower()
        if user_type.lower() == 'exit':
            print("\nThank you for visiting! Have a nice day ^-^")
            break
        
        if user_type == 'admin':
            if admin_login():
                admin_menu_choice()
            else: 
                print("The login attempt is canceled.")
        elif user_type == 'borrower':
            borrower_menu_choice()
        else:
            print("Invalid user type! Please enter 'admin' or 'borrower'.")


# call/execute the main() func if the script is run directly
if __name__ == "__main__":
    main()