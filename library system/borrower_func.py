from extra_func import *
from books_list import books


# func used to search for a book by entering any keyword 
# will check if it matches with any keyword of a book on the list
# allowing the borrower to borrow the book searched within this search menu w/o open the borrow menu
# allowing to borrow multiple books searched by entering the corresponding book index number on the searched book list
# still showing the 'unavailable' book in the books list displayed but can not be borrowed (since this is the search book menu)
def search_and_borrow_book():
    while True:
        # handling searching book
        search_query = input("\nEnter your search keyword (type 'exit' to cancel and back to main menu): ").strip().lower()

        if search_query.lower() == 'exit':
            print("Search book operation canceled.")
            return

        if not search_query:
            print("Please enter a search keyword.")
            continue

        searched_books = []
        # iterates through the books list and checks if any of the attribute value of each book match/contain the search_query 
        attributes = ['isbn', 'title', 'author', 'genre', 'publisher', 'publication_year', 'pages', 'availability']
        for book in books:
            for attr in attributes:
                attribute_value = str(getattr(book, attr)).lower()
                if attr == 'availability':
                    if search_query == 'available' and book.availability:
                        searched_books.append(book)
                    elif search_query == 'unavailable' and not book.availability:
                        searched_books.append(book)
                    break
                else:
                    if search_query.lower() in attribute_value:
                        searched_books.append(book)
                        break

        if not searched_books:
            print("\nNo matching books found.")
            try_again = ask_try_again()
            if try_again != 'yes':
                print("Searching book canceled.")
                return
            continue

        print("\nMatching Books:\n")
        display_books(searched_books)

        confirm_borrow = input("\nDo you want to borrow any of these books? (yes/no): ").strip().lower()
        while confirm_borrow not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'.")
            confirm_borrow = input("\nDo you want to borrow any of these books? (yes/no): ").strip().lower()

        # handling borrowing book
        if confirm_borrow == 'yes':
            selected_indexes = set() # initialize an empty set to store selected book indexes (prevents duplicate books being called)
            while True:
                borrow_selected_idx = input("\nEnter the index numbers corresponding to the books you want to borrow (separated by commas) or press Enter to borrow all: ").strip()

                # handling case when borrower presses Enter -> borrow all books
                success_borrowed = False
                if not borrow_selected_idx:
                    for book in searched_books:
                        if book.availability:
                            # set the value to True to print out the "book return info" (preventing multiple printing)
                            success_borrowed = True 
                            # set the value to False, which means changing the book availability status from 'available' to 'unavailable' for borrowing
                            book.availability = False 
                            print(f"\nBook '{book.title}' with ISBN '{book.isbn}' borrowed successfully.")
                        else:
                            print(f"\nSorry, the book '{book.title}' with ISBN '{book.isbn}' is currently unavailable for borrowing.")
                    # book return info
                    # at least one condition true (1 book borrowed) will print out the message (printing only once)
                    if success_borrowed: 
                        print("\nIt is mandatory to return the books within 7 days, starting from the day you borrowed them. Thank you!")
                        break
                    else:
                        print("\nAll selected books are currently unavailable for borrowing.")
                        break
                
                # handling case when borrower entering book index number(s) -> borrow only selected books
                # extract valid book indexes from borrower input
                book_index_raw = [int(index.strip()) for index in borrow_selected_idx.replace(' ', '').split(',') if index.strip().isdigit()]
                # remove the index of an already selected indexes to prevent the book from being called twice
                book_index = list(set(book_index_raw) - selected_indexes)

                invalid_index = [index for index in book_index if index < 1 or index > len(searched_books)] # identifying invalid index inputted
                invalid_str = [index for index in borrow_selected_idx.split(',') if not index.strip().isdigit()] # identifying invalid input e.g. str (not isdigit)

                if all(char.isdigit() or char == ',' or char == ' ' for char in borrow_selected_idx): # condition checking the input
                    if all(1 <= index <= len(searched_books) for index in book_index): # condition checking the inputted index
                        for index in book_index:
                            book = searched_books[index - 1] # get the real index of the book (adjusted for zero-based indexing)
                            if book.availability:
                                # set the value to True to print out the "book return info" (preventing multiple printing)
                                success_borrowed = True
                                # set the value to False, which means changing the book availability status from 'available' to 'unavailable' for borrowing
                                book.availability = False
                                print(f"\nBook '{book.title}' with ISBN '{book.isbn}' borrowed successfully.")
                            else:
                                print(f"\nSorry, the book '{book.title}' with ISBN '{book.isbn}' is currently unavailable for borrowing.")
                        # book return info
                        # at least one condition true (1 book borrowed) will print out the message (printing only once)
                        if success_borrowed:
                            print("\nIt is mandatory to return the books within 7 days, starting from the day you borrowed them. Thank you!")
                            break
                        else:
                            print("\nAll selected books are currently unavailable for borrowing.")
                            break
                    else:
                        # mapping all invalid index to str and join it using comma separator
                        print(f"Invalid book index number(s): {', '.join(map(str, invalid_index))}")
                        print("Please enter a valid book index number(s) or press Enter to borrow all searched books.")
                else:
                    # mapping all invalid input (inc: incorrect index and not isdigit input) to str and join it using comma separator
                    invalid_input = ', '.join(map(str, invalid_index + invalid_str))
                    print(f"Invalid input(s): {invalid_input}")
                    print("Please enter numeric value(s) and a valid book index number(s) separated by commas or press Enter to borrow all searched books.")
        else:
            print("Borrowing process canceled.")
        
        search_again = input("\nDo you want to search again? (yes/no): ").strip().lower()
        while search_again not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'.")
            search_again = input("\nDo you want to search again? (yes/no): ").strip().lower()
        if search_again != 'yes':
            break


# func used to borrow books by entering the ISBN/title of the book to be borrowed
# allowing to borrow multiple books by entering multiple ISBN/title of the book
# the borrower will be asked to choose the corresponding book index number to be borrowed
# will not show the 'unavailable' book in the books list displayed 
# it is filtered first and shows only available books to borrow
def borrow_book():
    while True:
        borrow_input = input("\nEnter the ISBNs or titles of the books to borrow (separated by commas) or type 'exit' to cancel and back to main menu: ").strip()

        if borrow_input.lower() == 'exit':
            print("Borrowing book operation canceled.")
            return

        if not borrow_input:
            print("No input provided. Borrowing book canceled.")
            try_again = ask_try_again()
            if try_again != 'yes':
                print("Borrowing book operation canceled.")
                return
            continue

        borrow_input_list = [item.strip() for item in borrow_input.split(',')]

        selected_books = []

        for input_item in borrow_input_list:
            input_item = input_item.lower()
            found_book = None
            for book in books:
                if input_item == book.isbn.lower() or input_item == book.title.lower():
                    found_book = book
                    break
            
            # handling case when the book is not found
            if not found_book:
                print(f"\nBook with ISBN or title '{input_item}' not found.")
                continue

            # handling case when the book is unavailable for borrowing (will print the unavailable message instead of displaying it on the list)
            elif not found_book.availability:
                print(f"\nSorry, the book '{found_book.title}' with ISBN '{found_book.isbn}' is currently unavailable for borrowing.")
                continue

            selected_books.append(found_book)

        if not selected_books:
            print("No books selected for borrowing.")
            try_again = ask_try_again()
            if try_again != 'yes':
                print("Borrowing book canceled.")
                return
            continue

        print("\nSelected Books to Borrow:\n")
        display_books(selected_books)
    
        confirm_borrow = input("\nDo you want to borrow any of these books? (yes/no): ").strip().lower()
        while confirm_borrow not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'.")
            confirm_borrow = input("\nDo you want to borrow any of these books? (yes/no): ").strip().lower()

        if confirm_borrow == 'yes':
            selected_indexes = set() # initialize an empty set to store selected book indexes (prevents duplicate books being called)
            while True:
                borrow_selected_idx = input("\nEnter the index numbers corresponding to the books you want to borrow (separated by commas) or press Enter to borrow all: ").strip()
                
                # handling case when borrower presses Enter -> borrow all books
                if not borrow_selected_idx:
                    for book in selected_books:
                        # set the value to False, which means changing the book availability status from 'available' to 'unavailable' for borrowing
                        book.availability = False
                    print("All selected books borrowed successfully.")
                    print("\nIt is mandatory to return the books within 7 days, starting from the day you borrowed them. Thank you!")
                    break
                
                # handling case when borrower entering book index number(s) -> borrow only selected books
                # extract valid book indexes from borrower input
                book_index_raw = [int(index.strip()) for index in borrow_selected_idx.replace(' ', '').split(',') if index.strip().isdigit()]
                # remove the index of an already selected indexes to prevent the book from being called twice
                book_index = list(set(book_index_raw) - selected_indexes)

                invalid_index = [index for index in book_index if index < 1 or index > len(selected_books)] # identifying invalid index inputted
                invalid_str = [index for index in borrow_selected_idx.split(',') if not index.strip().isdigit()] # identifying invalid input e.g. str (not isdigit)

                if all(char.isdigit() or char == ',' or char == ' ' for char in borrow_selected_idx): # condition checking the input
                    if all(1 <= index <= len(selected_books) for index in book_index): # condition checking the inputted index
                        for index in book_index:
                            book = selected_books[index - 1] # get the real index of the book (adjusted for zero-based indexing)
                            # set the value to False, which means changing the book availability status from 'available' to 'unavailable' for borrowing
                            book.availability = False
                            print(f"\nBook '{book.title}' with ISBN '{book.isbn}' borrowed successfully.")
                        print("\nIt is mandatory to return the books within 7 days, starting from the day you borrowed them. Thank you!")
                        break
                    else:
                        # mapping all invalid index to str and join it using comma separator
                        print(f"Invalid book index number(s): {', '.join(map(str, invalid_index))}")
                        print("Please enter a valid book index number(s) or press Enter to borrow all selected books.")
                else:
                    # mapping all invalid input (inc: incorrect index and not isdigit input) to str and join it using comma separator
                    invalid_input = ', '.join(map(str, invalid_index + invalid_str))
                    print(f"Invalid input(s): {invalid_input}")
                    print("Please enter numeric value(s) and a valid book index number(s) separated by commas or press Enter to borrow all selected books.")
        else:
            print("Borrowing process canceled.")
            try_again = ask_try_again()
            if try_again != 'yes':
                print("Borrowing book canceled.")
                return
            continue

        borrow_again = input("\nDo you want to borrow other books? (yes/no): ").strip().lower()
        while borrow_again not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'.")
            borrow_again = input("\nDo you want to borrow other books? (yes/no): ").strip().lower()
        if borrow_again != 'yes':
            print("\nThank you for borrowing our books and do not forget to return them! Have a nice day ^-^")
            break


# func used to return books by entering the ISBN/title of the book to be returned
# allowing to return multiple books by entering multiple ISBN/title of the book
# the borrower will be asked to choose the corresponding book index number to be returned
# will not show the 'available' book in the books list displayed 
# it is filtered first and shows only unavailable books to return
# has the SAME LOGIC as the borrow_func the difference only in the availability status for this case 'unavailable'
def return_book():
    while True:
        return_input = input("\nEnter the ISBNs or titles of the books to return (separated by commas) or type 'exit' to cancel and back to main menu: ").strip()

        if return_input.lower() == 'exit':
            print("Returning book operation canceled.")
            return

        if not return_input:
            print("No input provided. Returning book canceled.")
            try_again = ask_try_again()
            if try_again != 'yes':
                print("Returning book operation canceled.")
                return
            continue

        return_input_list = [item.strip() for item in return_input.split(',')]

        selected_books = []

        for input_item in return_input_list:
            input_item = input_item.lower()
            found_book = None
            for book in books:
                if input_item == book.isbn.lower() or input_item == book.title.lower():
                    found_book = book
                    break

            if not found_book:
                print(f"\nBook with ISBN or title '{input_item}' not found.")
                continue

            # handling case when the book is available for borrowing (will print the available message instead of displaying it on the list)
            elif found_book.availability:
                print(f"\nSorry, the book '{found_book.title}' with ISBN '{found_book.isbn}' is currently available or has been returned.")
                continue

            selected_books.append(found_book)

        if not selected_books:
            print("No books selected for returning.")
            try_again = ask_try_again()
            if try_again != 'yes':
                print("Returning book canceled.")
                return
            continue

        print("\nSelected Books to Return:\n")
        display_books(selected_books)
    
        confirm_return = input("\nDo you want to return any of these books? (yes/no): ").strip().lower()
        while confirm_return not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'.")
            confirm_return = input("\nDo you want to return any of these books? (yes/no): ").strip().lower()

        if confirm_return == 'yes':
            selected_indexes = set() # initialize an empty set to store selected book indexes (prevents duplicate books being called)
            while True:
                return_selected_idx = input("\nEnter the index numbers corresponding to the books you want to return (separated by commas) or press Enter to return all: ").strip()

                # handling case when borrower presses Enter -> return all books
                if not return_selected_idx:
                    for book in selected_books:
                        # set the value to True, which means changing the book availability status from 'unavailable' to 'available' for borrowing
                        book.availability = True
                    print("All selected books returned successfully.")
                    print("\nThank you very much for returning the books. Do not hesitate to borrow other books!")
                    break
                
                # handling case when borrower entering book index number(s) -> return only selected books
                book_index_raw = [int(index.strip()) for index in return_selected_idx.replace(' ', '').split(',') if index.strip().isdigit()]
                # remove the index of an already selected indexes to prevent the book from being called twice
                book_index = list(set(book_index_raw) - selected_indexes)

                invalid_index = [index for index in book_index if index < 1 or index > len(selected_books)]
                invalid_str = [index for index in return_selected_idx.split(',') if not index.strip().isdigit()]

                if all(char.isdigit() or char == ',' or char == ' ' for char in return_selected_idx):
                    if all(1 <= index <= len(selected_books) for index in book_index):
                        for index in book_index:
                            book = selected_books[index - 1]
                            # set the value to True, which means changing the book availability status from 'unavailable' to 'available' for borrowing
                            book.availability = True
                            print(f"\nBook '{book.title}' with ISBN '{book.isbn}' returned successfully.")
                        print("\nThank you very much for returning the books. Do not hesitate to borrow other books!")
                        break
                    else:
                        print(f"Invalid book index number(s): {', '.join(map(str, invalid_index))}")
                        print("Please enter a valid book index number(s) or press Enter to return all selected books.")
                else:
                    invalid_input = ', '.join(map(str, invalid_index + invalid_str))
                    print(f"Invalid input(s): {invalid_input}")
                    print("Please enter numeric value(s) and a valid book index number(s) separated by commas or press Enter to return all selected books.")
        else:
            print("Returning book process canceled.")
            try_again = ask_try_again()
            if try_again != 'yes':
                print("Returning book canceled.")
                return
            continue

        return_again = input("\nDo you want to return other books? (yes/no): ").strip().lower()
        while return_again not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'.")
            return_again = input("\nDo you want to return other books? (yes/no): ").strip().lower()
        if return_again != 'yes':
            print("\nThank you very much for returning the books and do not hesitate to borrow other books! Have a nice day ^-^")
            break