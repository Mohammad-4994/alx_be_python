class Book: 

    def __init__(self, title , author ) :
        
        self.title = title 
        self.author = author
        self._is_checked_out = False
        
    def add_book (self) :

        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out :
            self._is_checked_out = False
            return True
        return False
    

    def is_available(self):
        return not self._is_checked_out

class Library:
    def __init__(self):
        self._books = []  

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        
        for book in self._books:
            if book.title == title and book.is_available():
                return book.check_out()
                

    def return_book(self, title):

        for book in self._books:
            if book.title == title and not book.is_available():
               return book.return_book()
                

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                return f"Title: {book.title}, Author: {book.author}"
       
