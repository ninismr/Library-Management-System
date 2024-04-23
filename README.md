## Library Management System 
(Capstone Project Module 1 - DTIDS Purwadhika)

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

1. *Clone repository*: clone it to your local machine https://github.com/ninismr/Library-Management-System.git.
2. *Python Installed*: Ensure you have python installed.
3. *Requirements.txt*: Install the required dependencies by running pip install -r requirements.txt.
4. *Run the main script*: Start the program by running the Python script (main.py).
5. *Choose your role*: Type 'admin' or 'borrower' at the prompt. If 'admin', provide the required password.
6. *Navigate through the menu*: Use the numbered options to perform actions like viewing, adding, updating, or deleting books (as an admin) or browsing and managing borrowings (as a borrower).
7. *Switch roles or exit*: At any point, switch roles or type 'exit' to close the program.

## Setup environment

pip install tabulate

### Exiting the Program

To exit the system at any point, the user can type 'exit' during the role selection prompt. This flexibility ensures that users can quickly terminate their session without navigating through additional menus.


