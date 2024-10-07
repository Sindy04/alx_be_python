class Book:
  def __init__(self,title,author):
    """
    Initilizes a Book instance with title and author.

    Args:
    title(str): The title of the book.
    author(str): The author of the book.
    """
    self.title = title
    self.author = author

def __str__(self):
  """
  Returns a string representation of the Book instance.
  Returns:
  str: A human-readable representation of the Book instance.
  """
  return f"Book: {self.title} by {self.author}"

class EBook(/Book):
  def __int__(self,title,author,file_size):
    """
    Initializes an EBook instance with title,author and file_size

    Args:
    title (str): The title of the book.
    author (str): The author of the book.
    file_size (int): The file size of the eBook in KB.
    """
    super()__init__(title,author)
    self.file_size = file_size

def __str__(self):
  """
  Reurns a strong representation of the EBook instance.

  Returns:
  str: A human-readable representation of the EBook instance.
  """
  return f"EBook:{self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
  def __init__(self,title,author,page_count):
    """
    Initializes a PrintBook instance with title,author and page count.

    Args:
    title (str): The title of the book.
    author (str): The author of the book.
    page_count (int): The page count of the print book.
  
