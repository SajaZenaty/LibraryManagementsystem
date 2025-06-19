from models.Library_item import library_item
class magazine(library_item):
    #Here I define an extra attribute for the magazine class which is issue_number
    def __init__(self, title, author, issue_number , id):
        super().__init__(title, author)
        self.issue_number = issue_number
        self.id = id
        

    def display_info(self):
        return f"Magazine ID: {self.id}, Title: {self.title}, Author: {self.author}, Issue Number: {self.issue_number}"

    def check_availability(self, items_id):
        return  self.id not in items_id 