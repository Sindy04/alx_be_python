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

  def 
