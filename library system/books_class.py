# Book class that will take 8 parameters for each Book object created
class Book:
    def __init__(self, isbn, title, author, genre, publisher, publication_year, pages, availability):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.publisher = publisher
        self.publication_year = publication_year
        self.pages = pages
        self.availability = availability 