from models.Library_item import library_item
from models.Reservable import reservable

class dvd(library_item , reservable):
    # here I defined extra one attribute for dvd class
    # release_year and it is an integer that represents the year the DVD was released
    def __init__(self, title, author , release_year , id):
        super().__init__(title, author)
        self.release_year = release_year
        self.id = id
        


    def display_info(self):
        return f"DVD ID: {self.id}, Title: {self.title}, Author: {self.author}, Release Year: {self.release_year}"
    
    def check_availability(self, items_id):
        return self.id not in items_id
    
    def reserve(self,item_id, user_id):
        pass
     