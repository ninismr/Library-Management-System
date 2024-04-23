## Library Management System

This Python-based Library Management System allows for comprehensive management of library books and user interaction in two main roles: Administrator and Borrower. Each role is equipped with specific functionalities to streamline the management and borrowing of books.

### System Overview

1. *Start-Up*: When the program is executed, users are prompted to identify themselves as either an 'admin' or a 'borrower'. Users can also choose to exit the system by typing 'exit'.

2. *User Authentication*: 
   - *Administrator Authentication*: Requires the user to enter a password. If authentication fails, the user can retry or exit to the main menu.
   - *Borrower*: No authentication is required; they are directed straight to the borrower menu.

3. *Role-Based Functionalities*:
   - *Administrator*:
     - View all books.
     - View unavailable/borrowed books.
     - Search for books by various attributes.
     - Add new books to the system.
     - Update existing book information.
     - Delete books from the system.
     - Switch to the borrower menu.
   - *Borrower*:
     - View all books.
     - View unavailable/borrowed books.
     - Search for books and borrow directly from the search results.
     - Borrow books.
     - Return books.
     - Switch to the admin menu.

### Menus and Choices

#### Admin Menu
1. *View Books List*: Displays all the books in the library.
2. *View Unavailable/Borrowed Books List*: Shows books that are currently borrowed.
3. *Search Book*: Allows searching books by keywords.
4. *Add Book*: Adds a new book to the library.
5. *Update Book*: Updates details of an existing book.
6. *Delete Book*: Removes a book from the library.
7. *Exit to Borrower Menu*: Switches the user from the admin to the borrower menu.

#### Borrower Menu
1. *View Books List*: Displays all the books in the library.
2. *View Unavailable/Borrowed Books List*: Shows books that are currently borrowed.
3. *Search and Borrow Book*: Search for books by keywords and borrow immediately.
4. *Borrow Book*: Initiates the borrowing process for a selected book.
5. *Return Book*: Returns a previously borrowed book.
6. *Exit to Admin Menu*: Changes the role to admin after password verification.

### Usage

1. *Run the main script*: Start the program by running the Python script (main.py).
2. *Choose your role*: Type 'admin' or 'borrower' at the prompt. If 'admin', provide the required password.
3. *Navigate through the menu*: Use the numbered options to perform actions like viewing, adding, updating, or deleting books (as an admin) or browsing and managing borrowings (as a borrower).
4. *Switch roles or exit*: At any point, switch roles or type 'exit' to close the program.

### Exiting the Program

To exit the system at any point, the user can type 'exit' during the role selection prompt. This flexibility ensures that users can quickly terminate their session without navigating through additional menus.

# Capstone_1_purwadhika ✨
## Overview
Capstone project for module 1 Purwadika DTIDS. Case of the system is to create bakery management system. This system is designed to provide a simple and efficient way for authorized bakers to manage their bread stocks and for customer to buy the products.

## Usage
1. Clone repository to your local machine https://github.com/ivansetya/Ahjussi_bakeryshop_capstone1_purwadhika.git
2. Ensure you have python installed
3. Install the required dependencies by running pip install -r requirements.txt
4. Run the main.py file using python

## Presentation
https://www.canva.com/design/DAGDKB9-2Yk/XDwm1agX3gIX27_Hj-6qIw/edit?utm_content=DAGDKB9-2Yk&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

## Setup environment

pip install tabulate


## System Flowchart
### main.py
![Main_py drawio](https://github.com/ivansetya/Ahjussi_bakeryshop_capstone1_purwadhika/assets/75768911/b692136a-87ec-4b6d-a1ab-9a19fc282208)
### User/login_as_baker.py
![login_to_baker drawio (1)](https://github.com/ivansetya/Ahjussi_bakeryshop_capstone1_purwadhika/assets/75768911/94f22abc-1871-4605-b641-6ec6a0bedc70)
### User/login_as_customer.py
![login_to_customer drawio](https://github.com/ivansetya/Ahjussi_bakeryshop_capstone1_purwadhika/assets/75768911/0c6bb12a-4537-4093-b27e-7d7280b84e69)
### Main_features/show_bread.py
![show_bread drawio (1)](https://github.com/ivansetya/Ahjussi_bakeryshop_capstone1_purwadhika/assets/75768911/96e26572-add0-4484-9f50-4db36c8efe85)
### Main_features/create_update_bread.py
![AddandEdit drawio](https://github.com/ivansetya/Ahjussi_bakeryshop_capstone1_purwadhika/assets/75768911/6772ba2d-fe27-4ce4-bc1f-0ea4fd01c893)
### Main_features/remove_bread.py
![delete_item drawio](https://github.com/ivansetya/Ahjussi_bakeryshop_capstone1_purwadhika/assets/75768911/42183b4a-4bbd-4c2a-b0d6-b593d210aef5)
### Main_features/sorted_show_bread
![sort_table drawio](https://github.com/ivansetya/Ahjussi_bakeryshop_capstone1_purwadhika/assets/75768911/53a04b75-03ec-410e-a1d4-8fb8511fc637)
### Additional_features/buy_bread.py
![buy_bread drawio](https://github.com/ivansetya/Ahjussi_bakeryshop_capstone1_purwadhika/assets/75768911/db65601f-cdb1-4ad2-be1d-5276428bea87)
