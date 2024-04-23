# importing Book class, books list, and all func in the extra_func.py file
from books_class import Book
from books_list import books
from functions.extra_func import *


# func used to view all books in the list and allow the user to sort the book data by all attributes
def view_books_list():
    if not books:
        print("\nNo books are available. Exiting program.")
        exit(0)
    else:
        print("\nBooks List:\n")
        display_books(books)
    
    while True:
        # allows the user to sort the book data based on all the book's attributes
        sort_choice = input("\nDo you want to sort the data? (yes/no): ").strip().lower()
        while sort_choice not in ['yes', 'no']:  
            print("Invalid input. Please enter 'yes' or 'no'.")
            sort_choice = input("\nDo you want to sort the data? (yes/no): ").strip().lower()
        
        if sort_choice == 'yes':
            while True:
                sort_attribute = input("\nEnter the attribute to sort by (ISBN/Title/Author/Genre/Publisher/Publication Year/Pages/Availability): ").strip().lower()
                while sort_attribute not in ["isbn", "title", "author", "genre", "publisher", "publication year", "pages", "availability"]:
                    print("Invalid attribute. Please enter a valid attribute.")
                    sort_attribute = input("\nEnter the attribute to sort by (ISBN/Title/Author/Genre/Publisher/Publication Year/Pages/Availability): ").strip().lower()

                # asks the user if they want to sort the books list in DESC order 
                # if 'no' then it will sorted in ASC order by default
                sort_order = input("\nDo you want to sort the data in descending order? (yes/no): ").strip().lower()
                while sort_order not in ['yes', 'no']:  
                    print("Invalid input. Please enter 'yes' or 'no'.")
                    sort_order = input("\nDo you want to sort the data in descending order? (yes/no): ").strip().lower()
                reverse_sort = sort_order == 'yes'

                sorted_books_data = sort_books(books, sort_attribute)
                # if 'yes' reverse the books list order to DESC order
                if reverse_sort:
                    sorted_books_data.reverse()

                print("\nSorted Books List:\n")
                display_books(sorted_books_data)

                sort_again = input("\nDo you want to sort again using another attribute? (yes/no): ").strip().lower()
                while sort_again not in ['yes', 'no']:
                    print("Invalid input. Please enter 'yes' or 'no'.")
                    sort_again = input("\nDo you want to sort again using another attribute? (yes/no): ").strip().lower()
                if sort_again != 'yes':
                    break

        else:
            print("Sorting canceled.")
        break


# func used to view all unavailable/borrowed books in the list and allow the user to sort the book data by all attributes
def view_unavailable_books():
    # filter out the unavailable books from the books list
    unavailable_books = [book for book in books if not book.availability]
    
    if not unavailable_books:
        print("\nNo unavailable/borrowed books are available.")
        return
    else:
        print("\nUnavailable/Borrowed Books List:\n")
        display_books(unavailable_books)
    
    while True:
        # allows the user to sort the book data based on all the book's attributes
        sort_choice = input("\nDo you want to sort the data? (yes/no): ").strip().lower()
        while sort_choice not in ['yes', 'no']:  
            print("Invalid input. Please enter 'yes' or 'no'.")
            sort_choice = input("\nDo you want to sort the data? (yes/no): ").strip().lower()
        
        if sort_choice == 'yes':
            while True:
                sort_attribute = input("\nEnter the attribute to sort by (ISBN/Title/Author/Genre/Publisher/Publication Year/Pages/Availability): ").strip().lower()
                while sort_attribute not in ["isbn", "title", "author", "genre", "publisher", "publication year", "pages", "availability"]:
                    print("Invalid attribute. Please enter a valid attribute.")
                    sort_attribute = input("\nEnter the attribute to sort by (ISBN/Title/Author/Genre/Publisher/Publication Year/Pages/Availability): ").strip().lower()

                # asks the user if they want to sort the books list in DESC order 
                # if 'no' then it will sorted in ASC order by default
                sort_order = input("\nDo you want to sort the data in descending order? (yes/no): ").strip().lower()
                while sort_order not in ['yes', 'no']:  
                    print("Invalid input. Please enter 'yes' or 'no'.")
                    sort_order = input("\nDo you want to sort the data in descending order? (yes/no): ").strip().lower()
                reverse_sort = sort_order == 'yes'

                sorted_books_data = sort_books(unavailable_books, sort_attribute)
                # if 'yes' reverse the books list order to DESC order
                if reverse_sort:
                    sorted_books_data.reverse()

                print("\nSorted Unavailable/Borrowed Books List:\n")
                display_books(sorted_books_data)

                sort_again = input("\nDo you want to sort again using another attribute? (yes/no): ").strip().lower()
                while sort_again not in ['yes', 'no']:
                    print("Invalid input. Please enter 'yes' or 'no'.")
                    sort_again = input("\nDo you want to sort again using another attribute? (yes/no): ").strip().lower()
                if sort_again != 'yes':
                    break

        else:
            print("Sorting canceled.")
        break


# func used to search for a book by entering any keyword 
# will check if it matches with any keyword of a book on the list
def search_book():
    while True:
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
        else:
            print("\nMatching Books:\n")
            display_books(searched_books)

        search_again = input("\nDo you want to search again? (yes/no): ").strip().lower()
        while search_again not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'.")
            search_again = input("\nDo you want to search again? (yes/no): ").strip().lower()
        if search_again != 'yes':
            break


# func used to add new book data along with the input validation for each attribute 
# and check for the possibility of duplicate book data
# allowing to update the existing book instead of adding it as a new book
def add_book():
    while True:
        isbn = None
        title = None
        author = None
        genre = None
        publisher = None
        publication_year = None
        pages = None
        availability = None

        while True:
            # input validation for ISBN (allowing just numeric value to be inputted and can not be an empty input)
            if isbn is None:
                isbn_input = input("\nEnter the ISBN number of the book (type 'exit' to cancel and back to main menu): ").strip().lower()
                
                if isbn_input.lower() == 'exit':
                    print("Add book operation canceled.")
                    return
                
                is_isbn_valid, isbn_error = is_num(isbn_input)
                if not is_isbn_valid:
                    print(isbn_error)
                    continue
                
                # checking if the ISBN of the book or the book is already on the list (prevent duplicate book data)
                # allowing to update the existing book instead of adding it as a new book
                existing_book = next((book for book in books if book.isbn == isbn_input), None)
                if existing_book:
                    print(f"\nBook with the ISBN number '{isbn_input}' already exists in the books list.")
                    choice = input("\nDo you want to update the existing book instead? (yes/no): ").strip().lower()
                    while choice not in ['yes', 'no']:
                        print("Invalid input. Please enter 'yes' or 'no'.")
                        choice = input("\nDo you want to update the existing book instead? (yes/no): ").strip().lower()
                    if choice == "yes":
                        update_exist_book(existing_book)
                    else:
                        print("Operation canceled.")
                    break
                
                isbn = isbn_input

            # input validation for title (can not be an empty input)
            if title is None:
                title_input = input("\nEnter the title of the book: ")
                if not title_input:
                    print("Input cannot be empty.")
                    continue
                title = title_input.title()

            # input validation for author (allowing just alphabet value to be inputted and can not be an empty input)
            if author is None:
                author_input = input("\nEnter the author of the book: ")
                is_author_valid, author_error = is_alphabet(author_input)
                if not is_author_valid:
                    print(author_error)
                    continue
                author = author_input.title()

            # input validation for genre (allowing just alphabet value to be inputted and can not be an empty input)
            if genre is None:
                genre_input = input("\nEnter the genre of the book: ")
                is_genre_valid, genre_error = is_alphabet(genre_input)
                if not is_genre_valid:
                    print(genre_error)
                    continue
                genre = genre_input.title()

            # input validation for publisher (can not be an empty input)
            if publisher is None:
                publisher_input = input("\nEnter the publisher of the book: ")
                if not publisher_input:
                    print("Input cannot be empty.")
                    continue
                publisher = publisher_input.title()

            # input validation for publication year (allowing just non-negative int value to be inputted and can not be an empty input)
            if publication_year is None:
                publication_year_input = input("\nEnter the publication year of the book: ")
                is_year_valid, year_error = is_non_negative_int(publication_year_input)
                if not is_year_valid:
                    print(year_error)
                    continue
                publication_year = int(publication_year_input)

            # input validation for pages (allowing just non-negative int value to be inputted and can not be an empty input)
            if pages is None:
                pages_input = input("\nEnter the number of pages of the book: ")
                is_pages_valid, pages_error = is_non_negative_int(pages_input)
                if not is_pages_valid:
                    print(pages_error)
                    continue
                pages = int(pages_input)

            # input validation for availability (allowing just 'available' or 'unavailable' value to be inputted and can not be an empty input)
            if availability is None:
                availability_input = input("\nEnter the availability of the book (available/unavailable): ").lower()
                is_availability_valid, availability_error = is_valid_availability(availability_input)
                if not is_availability_valid:
                    print(availability_error)
                    continue
                availability = availability_input == 'available'

            # create the new Book object and add it to the books list
            new_book = Book(isbn, title, author, genre, publisher, publication_year, pages, availability)
            books.append(new_book)
            print("\nDetails of the new book:")
            print("ISBN             :", new_book.isbn)
            print("Title            :", new_book.title)
            print("Author           :", new_book.author)
            print("Genre            :", new_book.genre)
            print("Publisher        :", new_book.publisher)
            print("Publication Year :", new_book.publication_year)
            print("Pages            :", new_book.pages)
            print("Availability     :", "Available" if new_book.availability else "Unavailable")
            print("\nBook added successfully.")

            # allowing dynamic update for the new book data (in case the admin still inputted the wrong book data)
            choice = input("\nDo you want to change/update the new book data? (yes/no): ").strip().lower()
            while choice not in ['yes', 'no']:
                print("Invalid input. Please enter 'yes' or 'no'.")
                choice = input("\nDo you want to change/update the new book data? (yes/no): ").strip().lower()
            if choice == "yes":
                update_exist_book(new_book)
            break

        add_again = input("\nDo you want to add another book's data? (yes/no): ").strip().lower()
        while add_again not in ['yes', 'no']: 
            print("Invalid input. Please enter 'yes' or 'no'.")
            add_again = input("\nDo you want to add another book's data? (yes/no): ").strip().lower()
        if add_again != 'yes':
            break


# func used to update book data by entering the ISBN/title of the book
# showing the current and updated details of the book updated
# provides a dynamic update for the book (asking for confirmation of changes made) 
# by allowing the admin to make continuous updates to a book at a time w/o re-running the program each time  
def update_book():
    while True:
        update_input = input("\nEnter the ISBN or title of the book to update (type 'exit' to cancel and back to main menu): ").strip().lower()

        if update_input.lower() == 'exit':
            print("Update book operation canceled.")
            return

        # checking if the book with the ISBN/title inputted is on the books list or not
        found_book = None
        for book in books:
            if update_input.lower() == book.isbn.lower() or update_input.lower() == book.title.lower():
                found_book = book
                break

        if not found_book:
            print("Book not found.")
            try_again = ask_try_again()
            if try_again != 'yes':
                print("Update book canceled.")
                return
            continue

        # printing the current details of the book to be updated
        print("\nCurrent details of the book:")
        print("ISBN             :", found_book.isbn)
        print("Title            :", found_book.title)
        print("Author           :", found_book.author)
        print("Genre            :", found_book.genre)
        print("Publisher        :", found_book.publisher)
        print("Publication Year :", found_book.publication_year)
        print("Pages            :", found_book.pages)
        print("Availability     :", "Available" if found_book.availability else "Unavailable")

        # dict where the index numbers serve as keys with the attribute name and validation function as the associated value
        # mapping each attribute of a book to its corresponding validation function
        attribute_validators = {
            1: ("ISBN", is_num),
            2: ("Title", accept_any_input),
            3: ("Author", is_alphabet),
            4: ("Genre", is_alphabet),
            5: ("Publisher", accept_any_input),
            6: ("Publication_Year", is_non_negative_int),
            7: ("Pages", is_non_negative_int),
            8: ("Availability", is_valid_availability)
        }

        selected_indexes = set() # initialize an empty set to store selected attribute indexes (prevents duplicate attributes being called)
        while True:
            # choosing the attributes of a book to update by entering the corresponding index number to the attributes
            print("\nChoose the attributes to update:")
            for index, (attribute_name, _) in attribute_validators.items():
                print(f"{index}. {attribute_name}")

            update_input = input("\nEnter the index numbers corresponding to the attributes to update (comma-separated, or press Enter to cancel): ")
            if not update_input:
                break

            # extract valid attribute indexes from admin input
            update_input_index_raw = [int(index.strip()) for index in update_input.replace(',', ' ').split() if index.strip().isdigit()]
            # remove the index of an already selected attribute to prevent the attribute from being called twice
            update_input_index = list(set(update_input_index_raw) - selected_indexes)

            invalid_index = [index for index in update_input_index if index not in attribute_validators] # identifying invalid index inputted
            invalid_str = [index.strip() for index in update_input.split(',') if not index.strip().isdigit()] # identifying invalid input e.g. str (not isdigit)

            if invalid_str:
                # mapping all invalid input (inc: incorrect index and not isdigit input) to str and join it using comma separator
                invalid_input = ', '.join(map(str, invalid_index + invalid_str))
                print(f"Invalid input(s): {invalid_input}")
                print("Please enter numeric value(s) and a valid attribute index number(s) separated by commas.") 
                continue

            if invalid_index:
                # mapping all invalid index to str and join it using comma separator
                print(f"Invalid attribute index number(s): {', '.join(map(str, invalid_index))}") 
                print("Please enter a valid attribute index number(s) separated by commas.")
                continue

            for index in sorted(update_input_index):
                # retrieves and unpacks tuple (dict value) associated with the index
                # and assigns its values to corresponding variables defined
                current_value, validator = attribute_validators[index] 
                attribute_name = current_value

                if attribute_name.lower() == "availability":
                    while True:
                        new_value = input(f"\nNew {attribute_name} of the book (available/unavailable) (press Enter to keep current): ").title()
                        if not new_value:
                            print(f"{attribute_name} kept as '{'Available' if found_book.availability else 'Unavailable'}'.")
                            break
                        elif new_value.lower() not in ['available', 'unavailable']:
                            print("Invalid input. Please enter 'available' or 'unavailable'.")
                            continue
                        elif new_value.lower() == 'available' and found_book.availability or new_value.lower() == 'unavailable' and not found_book.availability:
                            print(f"{attribute_name} kept as '{'Available' if found_book.availability else 'Unavailable'}'.")
                            break
                        else:
                            # sets the new value to the availability attribute of a book updated
                            setattr(found_book, attribute_name.lower(), new_value.lower() == 'available')
                            print(f"{attribute_name} updated successfully to '{new_value}'.")
                            break
                else:
                    while True:
                        new_value = input(f"\nNew {attribute_name} of the book (press Enter to keep current): ").title()
                        current_attr_value = getattr(found_book, attribute_name.lower())
                        if not new_value:
                            print(f"{attribute_name} kept as '{getattr(found_book, attribute_name.lower())}'.")
                            break
                        elif new_value == str(current_attr_value) :
                            print(f"{attribute_name} kept as '{getattr(found_book, attribute_name.lower())}'.")
                            break
                        else:
                            is_valid, error_msg = validator(new_value)
                            if not is_valid:
                                print(error_msg)
                                continue

                            # sets the new value to the corresponding attribute updated of a book updated
                            setattr(found_book, attribute_name.lower(), new_value)
                            print(f"{attribute_name} updated successfully to '{new_value}'.")
                            break

            # printing the updated details of the book updated
            print("\nUpdated details of the book:")
            print("ISBN             :", found_book.isbn)
            print("Title            :", found_book.title)
            print("Author           :", found_book.author)
            print("Genre            :", found_book.genre)
            print("Publisher        :", found_book.publisher)
            print("Publication Year :", found_book.publication_year)
            print("Pages            :", found_book.pages)
            print("Availability     :", "Available" if found_book.availability else "Unavailable")
            print("\nBook details updated successfully.")

            # asks for confirmation if the admin still wants to change the updated book data
            # or the admin wants to proceed with the changes/updated book data  
            # if it is 'yes' -> it will loop back asking for entering the index number of book attributes to be updated (dynamic updating)
            confirm_update = input("\nDo you want to make another update for this book? (yes/no): ").strip().lower()
            while confirm_update not in ['yes', 'no']:
                print("Invalid input. Please enter 'yes' or 'no'.")
                confirm_update = input("\nDo you want to make another update for this book? (yes/no): ").strip().lower()
            if confirm_update != 'yes':
                break

        update_again = input("\nDo you want to update another book? (yes/no): ").strip().lower()
        while update_again not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'.")
            update_again = input("\nDo you want to update another book? (yes/no): ").strip().lower()
        if update_again != 'yes':
            break


# func used to delete a book data by entering the value of any book attributes chosen as the delete keyword 
# allowing all attributes to be used as the key for deletion
# allowing multiple book data deletions by entering the corresponding book index number on the selected book list
def delete_book():
    while True:
        attribute = input("\nEnter the attribute to use for deletion (ISBN/Title/Author/Genre/Publisher/Publication Year/Pages/Availability): ").strip().lower()

        if attribute not in ['isbn', 'title', 'author', 'genre', 'publisher', 'publication year', 'pages', 'availability']:
            print("Invalid attribute. Please enter a valid attribute.")
            continue

        search_value = input(f"\nEnter the value for {attribute} or press Enter to cancel: ").strip()
        if not search_value:
            try_again = ask_try_again()
            if try_again != 'yes':
                print("Book deletion canceled.")
                return
            continue

        if attribute in ['publication year', 'availability']:
            search_value = search_value.lower()

        matched_books = []
        for book in books:
            if attribute == 'availability':
                if search_value == 'available' and book.availability:
                        matched_books.append(book)
                elif search_value == 'unavailable' and not book.availability:
                        matched_books.append(book)
            elif attribute == 'publication year':
                # retrieves the value of the publication_year attribute from book object 
                # convert it to lower-case and str then compare it to search_value inputted by admin
                publication_year_value = str(getattr(book, 'publication_year', None)).lower() 
                if search_value.lower() in publication_year_value:
                    matched_books.append(book)
            else: 
                # retrieves the value of the attribute entered by the admin from book object 
                # convert it to lower-case and str then compare it to search_value inputted by admin
                attribute_value = str(getattr(book, attribute, None)).lower()
                if search_value.lower() in attribute_value:
                    matched_books.append(book)

        if not matched_books:
            print("\nNo books found matching the specified criteria.")
            try_again = ask_try_again()
            if try_again != 'yes':
                print("Book deletion canceled.")
                return
            continue

        print("\nBooks found matching the specified criteria:\n")
        display_books(matched_books)

        confirm_delete = input("\nDo you want to delete any of these books? (yes/no): ").strip().lower()
        while confirm_delete not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'.")
            confirm_delete = input("\nDo you want to delete any of these books? (yes/no): ").strip().lower()
        if confirm_delete == 'yes':
            selected_indexes = set() # initialize an empty set to store selected book indexes (prevents duplicate books being called)
            while True:
                delete_selected_idx = input("\nEnter the index numbers corresponding to the books you want to delete (separated by commas) or press Enter to delete all: ").strip()
                
                # handling case when admin presses Enter -> delete all books
                if not delete_selected_idx:
                    for book in matched_books:
                        books.remove(book)
                    print("All selected books deleted successfully.")
                    break

                # handling case when admin entering book index number(s) -> delete only selected books
                # extract valid book indexes from admin input
                book_index_raw = [int(index.strip()) for index in delete_selected_idx.replace(' ', '').split(',') if index.strip().isdigit()]
                # remove the index of an already selected indexes to prevent the book from being called twice
                book_index = list(set(book_index_raw) - selected_indexes)

                invalid_index = [index for index in book_index if index < 1 or index > len(matched_books)] # identifying invalid index inputted
                invalid_str = [index for index in delete_selected_idx.split(',') if not index.strip().isdigit()] # identifying invalid input e.g. str (not isdigit)

                if all(char.isdigit() or char == ',' or char == ' ' for char in delete_selected_idx): # condition checking the input 
                    if all(1 <= index <= len(matched_books) for index in book_index): # condition checking the inputted index
                        for index in book_index:
                            book = matched_books[index - 1] # get the real index of the book (adjusted for zero-based indexing)
                            del books[books.index(book)]
                            print(f"\nBook '{book.title}' with ISBN '{book.isbn}' deleted successfully.")
                        break
                    else:
                        # mapping all invalid index to str and join it using comma separator
                        print(f"Invalid book index number(s): {', '.join(map(str, invalid_index))}")
                        print("Please enter a valid book index number(s) or press Enter to delete all selected books.")
                else:
                    # mapping all invalid input (inc: incorrect index and not isdigit input) to str and join it using comma separator
                    invalid_input = ', '.join(map(str, invalid_index + invalid_str))
                    print(f"Invalid input(s): {invalid_input}")
                    print("Please enter numeric value(s) and a valid book index number(s) separated by commas or press Enter to delete all selected books.")
        else:
            print("Books deletion process canceled.")
            try_again = ask_try_again()
            if try_again != 'yes':
                print("Books deletion canceled.")
                return
            continue

        del_again = input("\nDo you want to delete more books? (yes/no): ").strip().lower()
        while del_again not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'.")
            del_again = input("\nDo you want to delete more books? (yes/no): ").strip().lower()
        if del_again != 'yes':
            break

