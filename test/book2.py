
class Book:
    def setval(self,libraryname,bookname,author,pages):
           self.libraryname=libraryname
           self.bookname=bookname
           self.author=author
           self.pages=pages
    def printval(self):
         print("libraryname:",self.libraryname)
         print("bookname:",self.bookname)
         print("author:",self.author)
         print("pages:",self.pages)
obj=Book()
obj.setval('xyx','harry potter','jk rawling',500)
obj.printval()
