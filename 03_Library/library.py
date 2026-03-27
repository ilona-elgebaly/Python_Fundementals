class Library:
  def __init__(self):
    self.books=[]
  def add_book(self,title,author):
    self.books.append({"title":title,"author":author})
  def remove_book (self,title):
    for book in self.books:
      if book["title"]==title:
        self.books.remove(book)
        return
    print("Book not found")
  def show_books (self):
    for book in self.books:
      print (f"{book['title']} by {book['author']}")
  def __str__(self):
    return "Library has " +str(len(self.books))+" books"


if __name__=="__main__":
  lib =Library()
  lib.add_book("'Winter'","Jackob Adams")
  lib.show_books()
  print(lib)
