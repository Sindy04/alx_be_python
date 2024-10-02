class Book:
  def __init__(self,title,author):
    self.title = title
    self.author = author
    self._is_checked_out = false

def check_out(self):
  self._is_checked_out = True

def return_book(self):
  self._is_checked_out = False

@property
def is_available(self):
  return not self._is_checked_out

class Libriary:
  def __init__(self):
    self.books =[]

  def add_book(self,book):
    self._books.append(book)

  def check_out_book(self,title):
    for book in self._books:
      if book.title == title:
        if book.is_available:
          book.check_out()
          print(f"'{title}'checked out successfully.")
        else:
          print(f"'{title}' is already checked out.")
          return
          print(f"'{title}' not found in library.")

      def return_book(self,title):
        for book in self._books:
          if book.title == title:
            if not book.is_available:
              book.return_book()
              print(f"'{title}' returned successfully.")
              print(f"'{title}' is already available.")
              return
              print(f"'{title}' not found in library.")

            def list_available_books(self):
            available _books = [boo.title for book in self._books if book.is _available]
            print9"Available books.")
            for book in available_books:
              print(book)
            else:
