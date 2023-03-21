class LibraryBook:
    def __init__(self,title,author,pub_year, ISBN):
        self.ISBN= ISBN
        self.title= title
        self.author= author
        self.pub_year= pub_year
        self.checked_out= False
    def __str__(self):
        return f"{self.title} by {self.author} ({self.pub_year}) ISBN: {self.ISBN}"
    def check_out(self):
        if self.checked_out:
            print("The books is already checked out")
        else:
            self.checked_out= True
            print(f"{self.title} has been checked-out")
    def check_in(self):
        if not self.checked_out:
            print("book is already ckecked in")
        else:
            self.checked_out= False
            print(f"{self.title} has been ckecked in")
class Library:
    def __init__(self):
        self.books=[]
        self.number_of_books=0
        self.available_books= 0
    def add_book(self,book):
        self.books.append(book)
        self.number_of_books +=1
        self.available_books +=1
    def remove_books(self,book):
        if book in self.books:
            self.books.remove(book)
            self.number_of_books+=1
            if not book.checked_out:
                self.available_books+=1
    def search_book(self,search_term):
        res=[]
        for book in self.books:
            if search_term.lower() in book.title.lower() or search_term.lower() in book.author.lower():
                res.append(book)
        return res
    def display_books(self):
        for book in self.books:
            print(book)
    def checkout_book(self, book):
        book.check_out()
        self.number_of_books -= 1

    def checkin_book(self, book):
        book.check_in()
        self.number_of_books+=1
        
# create class objects
booksLibrary = Library()
book1 = LibraryBook("mps", "Anna Cruz", 2017, "9491957662")
book2 = LibraryBook("Big data analystics", "Jacky jonson", 2013, "7449355730")
book3 = LibraryBook("Python", "Mosh Hamid", 2015, "0491946008")
book3 = LibraryBook("Python", "Mosh Hamid", 2015, "0491946008")
book4 = LibraryBook("java", "Mosh Hamid", 2015, "0491946008")
booksLibrary.add_book(book1)
booksLibrary.add_book(book2)
booksLibrary.add_book(book3)

# remove books
# print(booksLibrary.remove_books(book3))

print("List of Books:")
print(" ")
print(booksLibrary.display_books())

# Search for books with the search term "Python" and print the results.
results = booksLibrary.search_book("Python")
print("Search results:")
for book in results:
    print(book)





