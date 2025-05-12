
# 11. Class Methods
class book:
   total_books = 0 

   def __init__(self, title):
        self.title = title
        book.increment_book_count()

   @classmethod
   def increment_book_count(cls):
        cls.total_books += 1


book1 = book("Python Basics topic")
book2 = book("Advanced Python topic")

print("Total books:", book.total_books)
