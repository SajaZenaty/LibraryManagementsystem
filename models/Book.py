from models.Library_item import library_item
from models.Reservable import reservable

class book(library_item, reservable):
    # here I defined extra one attribute for book class
    # isbn and publisher
    # isbn is a string that represents the book's ISBN number
   
    def __init__(self, title, author, isbn ,id):
        super().__init__(title, author)
        self.isbn = isbn
        self.id = id
        
       
    def display_info(self):
        return f"Book ID: {self.id}, Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"
    
    def check_availability(self, items_id):
        return self.id not in items_id
    
    def reserve(self,item_id, user_id):
        pass
      