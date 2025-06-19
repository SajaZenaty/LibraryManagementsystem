from abc import ABC, abstractmethod

class library_item(ABC):
    def __init__(self,title,author):
        self.title = title
        self.author = author
    @abstractmethod
    def display_info(self):
        pass
    
    @abstractmethod
    def check_availability(self,items_id):
        pass