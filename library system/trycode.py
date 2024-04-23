def add_book():
    isbn = input("\nEnter the isbn number of the book: ")
    existing_book = next((book for book in books if book.isbn == isbn), None)
    if existing_book:
        print(f"\nBook with the isbn number of '{isbn}' already exists in the list.")
        choice = input("Do you want to update the existing book instead? (yes/no): ")
        if choice.lower() == "yes":
            view_books_list()
            return
        else:
            print("Operation cancelled.")
            return
        
    title = input("\nEnter the title of the book: ")
    author = input("\nEnter the author of the book: ")
    genre = input("\nEnter the genre of the book: ")
    publisher = input("\nEnter the publisher of the book: ")
    
    publication_year = int(input("\nEnter the publication year of the book: "))
    pages = int(input("\nEnter the pages number of the book: "))
    try:
        publication_year = int(publication_year)
        pages = int(pages)
    except ValueError:
        print("Publication year and pages must be integers. Book not added.")
        return
    
    availability_input = input("Enter the availability of the book (available/unavailable): ").lower()
    
    if availability_input not in ['available', 'unavailable']:
            print("Invalid input for availability. Book not added.")
            return
        
    availability = availability_input == 'available'
    
    new_book = Book(isbn, title, author, genre, publisher, publication_year, pages, availability)
    books.append(new_book)
    print("Book added successfully.")
    
    
    


def update_book():
    isbn_or_title = input("\nEnter the ISBN or title of the book to update: ")

    # Find the book to update
    found_book = None
    for book in books:
        if isbn_or_title.lower() == book.isbn.lower() or isbn_or_title.lower() == book.title.lower():
            found_book = book
            break

    # If book is not found
    if not found_book:
        print("\nBook not found.")
        return

    # Display current details of the book
    print("\nCurrent details of the book:")
    print("ISBN:", found_book.isbn)
    print("Title:", found_book.title)
    print("Author:", found_book.author)
    print("Genre:", found_book.genre)
    print("Publisher:", found_book.publisher)
    print("Publication Year:", found_book.publication_year)
    print("Pages:", found_book.pages)
    print("Availability:", "Available" if found_book.availability else "Unavailable")

    # Input validation and update loop
    while True:
        if not hasattr(found_book, 'new_isbn'):
            new_isbn = input("\nNew ISBN of the book (press enter to keep current): ")
            if new_isbn:
                if is_num(new_isbn):
                    found_book.new_isbn = new_isbn
                else:
                    print("Invalid input for ISBN. Please enter a numeric value.")
                    continue
            else:
                found_book.new_isbn = found_book.isbn

        if not hasattr(found_book, 'new_title'):
            new_title = input("New Title of the book (press enter to keep current): ")
            if new_title:
                found_book.new_title = new_title
            else:
                found_book.new_title = found_book.title

        if not hasattr(found_book, 'new_author'):
            new_author = input("New Author of the book (press enter to keep current): ")
            if new_author:
                if is_alphabet(new_author):
                    found_book.new_author = new_author
                    break  # Assuming author was the last input needed
                else:
                    print("Invalid input for author. Author can only contain alphabetic characters.")
                    continue
            else:
                found_book.new_author = found_book.author
                break  # Assuming author was the last input needed

    # Update the book details with new values
    found_book.isbn = found_book.new_isbn
    found_book.title = found_book.new_title
    found_book.author = found_book.new_author
    # Remove temporary attributes
    del found_book.new_isbn, found_book.new_title, found_book.new_author

    print("\nBook details updated successfully!")






def update_book():
    isbn_or_title = input("\nEnter the ISBN or title of the book to update: ")

    # Find the book to update
    found_book = None
    for book in books:
        if isbn_or_title.lower() == book.isbn.lower() or isbn_or_title.lower() == book.title.lower():
            found_book = book
            break

    # If book is not found
    if not found_book:
        print("\nBook not found.")
        return

    # Display current details of the book
    print("\nCurrent details of the book:")
    print("ISBN:", found_book.isbn)
    print("Title:", found_book.title)
    print("Author:", found_book.author)
    print("Genre:", found_book.genre)
    print("Publisher:", found_book.publisher)
    print("Publication Year:", found_book.publication_year)
    print("Pages:", found_book.pages)
    print("Availability:", "Available" if found_book.availability else "Unavailable")

    # Input validation and update loop
    while True:
        new_isbn = input("\nNew ISBN of the book (press enter to keep current): ")
        if new_isbn:
            if is_num(new_isbn):
                found_book.isbn = new_isbn
            else:
                print("Invalid input for ISBN. Please enter a numeric value.")
                continue

        new_title = input("New Title of the book (press enter to keep current): ")
        if new_title:
            found_book.title = new_title

        new_author = input("New Author of the book (press enter to keep current): ")
        if new_author:
            if is_alphabet(new_author):
                found_book.author = new_author
            else:
                print("Invalid input for author. Author can only contain alphabetic characters.")
                continue

        new_genre = input("New Genre of the book (press enter to keep current): ")
        if new_genre:
            if is_alphabet(new_genre):
                found_book.genre = new_genre
            else:
                print("Invalid input for genre. Genre can only contain alphabetic characters.")
                continue

        new_publisher = input("New Publisher of the book (press enter to keep current): ")
        if new_publisher:
            found_book.publisher = new_publisher

        new_publication_year = input("New Publication Year of the book (press enter to keep current): ")
        if new_publication_year:
            if is_non_negative_int(new_publication_year):
                found_book.publication_year = int(new_publication_year)
            else:
                print("Invalid input for publication year. Please enter a non-negative integer.")
                continue

        new_pages = input("New Pages of the book (press enter to keep current): ")
        if new_pages:
            if is_non_negative_int(new_pages):
                found_book.pages = int(new_pages)
            else:
                print("Invalid input for pages. Please enter a non-negative integer.")
                continue

        new_availability = input("New Availability of the book (available/unavailable) (press enter to keep current): ")
        if new_availability:
            if new_availability.lower() in ['available', 'unavailable']:
                found_book.availability = new_availability.lower() == 'available'
            else:
                print("Invalid input for availability. Please enter 'available' or 'unavailable'.")
                continue

        # Ask if the user wants to continue updating
        choice = input("\nDo you want to continue updating this book? (yes/no): ")
        if choice.lower() != 'yes':
            break

    print("\nBook details updated successfully.")
    
    
    
    
    
    
    
    
def is_valid_availability(s):
    return s.lower() in ['available', 'unavailable']

def update_book():
    isbn_or_title = input("\nEnter the ISBN or title of the book to update: ")

    # Find the book to update
    found_book = None
    for book in books:
        if isbn_or_title.lower() == book.isbn.lower() or isbn_or_title.lower() == book.title.lower():
            found_book = book
            break

    # If book is not found
    if not found_book:
        print("\nBook not found.")
        return

    # Display current details of the book
    print("\nCurrent details of the book:")
    print("ISBN:", found_book.isbn)
    print("Title:", found_book.title)
    print("Author:", found_book.author)
    print("Genre:", found_book.genre)
    print("Publisher:", found_book.publisher)
    print("Publication Year:", found_book.publication_year)
    print("Pages:", found_book.pages)
    print("Availability:", "Available" if found_book.availability else "Unavailable")

    # Define attribute prompts and validation functions
    attribute_validators = {
        "Author": is_alphabet,
        "Genre": is_alphabet,
        "Publisher": is_alphabet,
        "Publication Year": is_non_negative_int,
        "Pages": is_non_negative_int,
        "Availability": is_valid_availability
    }

    # Input validation and update loop
    for attr_name, validator_func in attribute_validators.items():
        new_value = input(f"New {attr_name} of the book (press enter to keep current): ")
        if new_value:
            while not validator_func(new_value):
                print(f"Invalid input for {attr_name}.")
                new_value = input(f"New {attr_name} of the book (press enter to keep current): ")
            setattr(found_book, attr_name.lower(), new_value)

    print("\nBook details updated successfully.")
    
    
    


    for attr_name, validator_func in attribute_validators.items():
        while True:
            current_value = getattr(found_book, attr_name.lower())
            new_value = input(f"\nNew {attr_name} of the book (press enter to keep current: '{current_value}'): ")
            if new_value.strip() == "":
                print(f"Keeping current {attr_name}: '{current_value}'")
                break

            is_valid, error_msg = validator_func(new_value)
            if not is_valid:
                print(error_msg)
                continue

            if attr_name == "Availability":
                setattr(found_book, attr_name.lower(), new_value.lower() == 'available')
            else:
                setattr(found_book, attr_name.lower(), new_value)

            break

    print("\nBook details updated successfully.")

    update_again = input("Do you want to update another book? (yes/no): ").strip().lower()
    while update_again not in ['yes', 'no']:
        print("Invalid input. Please enter 'yes' or 'no'.")
        update_again = input("Do you want to update another book? (yes/no): ").strip().lower()
    if update_again != 'yes':
        break





def borrow_book():
        selected_books = []
        while True:
            borrow_input = input("\nEnter the ISBN or title of the book to borrow (type 'exit' to cancel and back to main menu): ").strip().lower()

            if borrow_input.lower() == 'exit':
                print("Borrowing book operation canceled.")
                return

            found_book = None
            for book in books:
                if borrow_input.lower() == book.isbn.lower() or borrow_input.lower() == book.title.lower():
                    found_book = book
                    break

            if not found_book:
                print("\nBook not found.")
                try_again = ask_try_again()
                if try_again != 'yes':
                    print("Borrowing book canceled.")
                    return
                continue
            elif not found_book.availability:
                print("Sorry, this book is currently unavailable for borrowing.")
                try_again = ask_try_again()
                if try_again != 'yes':
                    print("Borrowing book canceled.")
                    return
                continue
            else:
                selected_books.append(found_book)

            if not selected_books:
                print("No books selected for borrowing.")
                return
            
            print("\nSelected Books to Borrow:")
            display_books(selected_books)
            
            confirm_borrow = input("Do you want to borrow these books? (yes/no): ").strip().lower()
            while confirm_borrow not in ['yes', 'no']:
                print("Invalid input. Please enter 'yes' or 'no'.")
                confirm_borrow = input("Do you want to borrow these books? (yes/no): ").strip().lower()
            if confirm_borrow == 'yes':
                for book in selected_books:
                    book.availability = False
                print("Books borrowed successfully.")
                print("It is mandatory to return the book within 7 days, starting from the day you borrowed it. Thank you!")
            else:
                print("Borrowing process canceled.")
                return

            borrow_again = input("Do you want to borrow more books? (yes/no): ").strip().lower()
            while borrow_again not in ['yes', 'no']:
                print("Invalid input. Please enter 'yes' or 'no'.")
                borrow_again = input("Do you want to borrow more books? (yes/no): ").strip().lower()
            if borrow_again != 'yes':
                print("Thank you for borrowing our book and do not forget to return it back ^-^")
                break
            
            
            
def display_books(books_list):
    headers = ["No.", "ISBN", "Title", "Author", "Genre", "Publisher", "Publication Year", "Pages", "Availability"]
    books_data = [(index + 1, book.isbn, book.title, book.author, book.genre, book.publisher, book.publication_year, book.pages,
                    'Available' if book.availability else 'Unavailable')
                    for index, book in enumerate(books_list)]
    indented_table = "\n".join(["\t" + row for row in tabulate(books_data, headers=headers, tablefmt="grid").split("\n")])
    print(indented_table)
