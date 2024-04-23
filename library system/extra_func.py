from operator import attrgetter
from tabulate import tabulate


# func used to sorts the list of books_data based on the specified sort_attribute 
# using the attrgetter function to get the book attribute (inputted by user) as a key for sorting
def sort_books(books_data, sort_attribute):
    if sort_attribute == "isbn":
        return sorted(books_data, key=attrgetter('isbn'))
    elif sort_attribute == "title":
        return sorted(books_data, key=attrgetter('title'))
    elif sort_attribute == "author":
        return sorted(books_data, key=attrgetter('author'))
    elif sort_attribute == "genre":
        return sorted(books_data, key=attrgetter('genre'))
    elif sort_attribute == "publisher":
        return sorted(books_data, key=attrgetter('publisher'))
    elif sort_attribute == "publication year":
        return sorted(books_data, key=attrgetter('publication_year'))
    elif sort_attribute == "pages":
        return sorted(books_data, key=attrgetter('pages'))
    elif sort_attribute == "availability":
        return sorted(books_data, key=attrgetter('availability'))
    else:
        return books_data


# funcs used to do input validation for each book attribute
# each funcs return tuple where: 
# the first element indicates whether the input is valid or not ('True' or 'False')
# the second element provides an error message if the input is invalid/'False', or None if it is valid/'True'

# func used to check/validate if the input is a numeric value (ISBN)
def is_num(i):
    if not i.isdigit():
        return False, "Invalid input. Input must be a numeric value."
    return True, None

# func used to check/validate if the input contains only alphabetic chars or spaces (author and genre)
# also checks if the input is empty
def is_alphabet(i):
    if not i.strip():
        return False, "Input cannot be empty."
    
    if not all(char.isalpha() or char.isspace() for char in i):
        return False, "Invalid input. Input must contain alphabetic characters only."
    return True, None

# func used to check/validate if the input is a non-negative int (publication year, pages)
def is_non_negative_int(i):
    if not (i.isdigit() and int(i) >= 0):
        return False, "Invalid input. Input must be a non-negative integer."
    return True, None

# func used to check/validate if the input is either 'available' or 'unavailable' (availability)
def is_valid_availability(i):
    if not i.lower() in ['available', 'unavailable']:
        return False, "Invalid input. Please enter 'available' or 'unavailable'."
    return True, None

# func that is always return True, indicating any input is accepted (title, publisher)
def accept_any_input(i):
    return True, None


# func used to update the existing book instead of adding it as a new book (prevent duplicate book data)
# it will call the func if the admin confirms 'yes' to update the book instead
# and it will take the existing book inputted as the arg and automatically show the existing book details to be updated
# this func has SAME LOGIC with the update_book() func the difference is this func only allows updating for the existing book inputted
def update_exist_book(existing_book):
    print("\nCurrent details of the book:")
    print("ISBN             :", existing_book.isbn)
    print("Title            :", existing_book.title)
    print("Author           :", existing_book.author)
    print("Genre            :", existing_book.genre)
    print("Publisher        :", existing_book.publisher)
    print("Publication Year :", existing_book.publication_year)
    print("Pages            :", existing_book.pages)
    print("Availability     :", "Available" if existing_book.availability else "Unavailable")

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

    selected_indexes = set()
    while True:
        print("\nChoose the attributes to update:")
        for index, (attribute_name, _) in attribute_validators.items():
            print(f"{index}. {attribute_name}")

        update_input = input("\nEnter the index numbers corresponding to the attributes to update (comma-separated, or press Enter to cancel): ")
        if not update_input:
            break

        update_input_index_raw = [int(index.strip()) for index in update_input.replace(',', ' ').split() if index.strip().isdigit()]
        update_input_index = list(set(update_input_index_raw) - selected_indexes)

        invalid_index = [index for index in update_input_index if index not in attribute_validators]
        invalid_str = [index.strip() for index in update_input.split(',') if not index.strip().isdigit()]

        if invalid_str:
            invalid_input = ', '.join(map(str, invalid_index + invalid_str))
            print(f"Invalid input(s): {invalid_input}")
            print("Please enter numeric value(s) and a valid attribute index number(s) separated by commas.") 
            continue

        if invalid_index:
            print(f"Invalid attribute index number(s): {', '.join(map(str, invalid_index))}") 
            print("Please enter a valid attribute index number(s) separated by commas.")
            continue

        for index in sorted(update_input_index):
            current_value, validator = attribute_validators[index] 
            attribute_name = current_value

            if attribute_name.lower() == "availability":
                while True:
                    new_value = input(f"\nNew {attribute_name} of the book (available/unavailable) (press Enter to keep current): ").title()
                    if not new_value:
                        print(f"{attribute_name} kept as '{'Available' if existing_book.availability else 'Unavailable'}'.")
                        break
                    elif new_value.lower() not in ['available', 'unavailable']:
                        print("Invalid input. Please enter 'available' or 'unavailable'.")
                        continue
                    else:
                        setattr(existing_book, attribute_name.lower(), new_value.lower() == 'available')
                        print(f"{attribute_name} updated successfully to '{new_value}'.")
                        break
            else:
                while True:
                    new_value = input(f"\nNew {attribute_name} of the book (press Enter to keep current): ").title()
                    if not new_value:
                        print(f"{attribute_name} kept as '{getattr(existing_book, attribute_name.lower())}'.")
                        break

                    is_valid, error_msg = validator(new_value)
                    if not is_valid:
                        print(error_msg)
                        continue

                    setattr(existing_book, attribute_name.lower(), new_value)
                    print(f"{attribute_name} updated successfully to '{new_value}'.")
                    break

        print("\nUpdated details of the book:")
        print("ISBN             :", existing_book.isbn)
        print("Title            :", existing_book.title)
        print("Author           :", existing_book.author)
        print("Genre            :", existing_book.genre)
        print("Publisher        :", existing_book.publisher)
        print("Publication Year :", existing_book.publication_year)
        print("Pages            :", existing_book.pages)
        print("Availability     :", "Available" if existing_book.availability else "Unavailable")
        print("\nBook details updated successfully.")

        confirm_update = input("\nDo you want to make another update for this book? (yes/no): ").strip().lower()
        while confirm_update not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'.")
            confirm_update = input("\nDo you want to make another update for this book? (yes/no): ").strip().lower()
        if confirm_update != 'yes':
            break


# func used to display the details of the books list in a tabulated format
# the book number (index) is started from 1 instead of 0
def display_books(books_list):
    headers = ["No.","ISBN", "Title", "Author", "Genre", "Publisher", "Publication Year", "Pages", "Availability"]
    books_data = [(index + 1, book.isbn, book.title, book.author, book.genre, book.publisher, book.publication_year, book.pages,
                    'Available' if book.availability else 'Unavailable')
                    for index, book in enumerate(books_list)]
    print(tabulate(books_data, headers=headers, tablefmt="rounded_grid"))


# func used to prompt the user whether they want to try again and return their choice
def ask_try_again():
    try_again = input("\nDo you want to try again? (yes/no): ").strip().lower()
    while try_again not in ['yes', 'no']:
        print("Invalid input. Please enter 'yes' or 'no'.")
        try_again = input("\nDo you want to try again? (yes/no): ").strip().lower()
    return try_again