class Book:
  def __init__(self, title, author, year):
    """
    Initializes a Book instance with title, author and year.

    Args:
    title(str): The title of the book.
    author(str): The author of the book.
    year(int): The publication year of the book.


    """
    self.title = title
    self.author = author
    self.year = year

def _del_(self):
  """
  Prints "Deleting (title of the book)" upon object deletion.
  """
  def _str_(self):
  """
  Returns a string in the format "(title) by (author), published in (year)".

  Returns:
  str: A human-readable representation of the Book instance.
  """
  return f"{self.title} by {self.author}, published in {self.year}"

def _repr_(self):
  Returns a string that would recreate the Book instance.

    Returns:
  str: An official representation of the Book instance.
  """
  return f"Book('{self.title}','{self.author}',{self.year})"
