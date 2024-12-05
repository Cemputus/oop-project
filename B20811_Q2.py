


### creating a book class

class Book:
    def __init__(self, title, author, copies_available):
        self.title = title
        self.author = author
        self.copies_available = copies_available

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Copies Available: {self.copies_available}"

### creating a Library class
class Library:
    def __init__(self):
        self.total_books = []
        
          #### Create a new Book 

    def add_book(self, title, author, copies):
      
        book = Book(title, author, copies)
        self.total_books.append(book)
        
        
        #### Search for the book in the library and Check if there are available copies

    def borrow_book(self, title):
        
        for book in self.total_books:
            if book.title == title:
               
                if book.copies_available > 0:
                    book.copies_available -= 1
                    print(f"You have borrowed '{title}'.")
                    return
                else:
                    print(f"Sorry, '{title}' is currently unavailable.")
                    return
        print(f"Book '{title}' not found in the library.")

 ### return the book by Searching  for the book in the library 
    def return_book(self, title):
       
        for book in self.total_books:
            if book.title == title:
                book.copies_available += 1
                print(f"Thank you for returning '{title}'.")
                return
        print(f"Book '{title}' not found in the library.")

    def display_library_info(self):
        if not self.total_books:
            print("No books available in the library.")
            return
        print("Library Books:")
        for book in self.total_books:
            print(book)


##### running the program
if __name__ == "__main__":
    
    # Creating  a Library object
    library = Library()

    # Adding the books to the library
    library.add_book("Tusome oluganda", "Yokana Kachere", 5)
    library.add_book("Uganda's Darkside", "Laura Mukasa", 3)
    library.add_book("Understanding the Bible", "Rev Jeremaih Ward", 2)

    # Displaying the library's books
    library.display_library_info()

    #### Borrow a book
    library.borrow_book("Tusome oluganda")
    
    library.borrow_book("Tusome oluganda")
    
    library.borrow_book("Tusome oluganda")
    
    library.borrow_book("Tusome oluganda") 

    #### Return a book
    library.return_book("Tusome oluganda")




    ####### Display the library's books again
    library.display_library_info()

    
    
    
   
    library.borrow_book("The river between")
