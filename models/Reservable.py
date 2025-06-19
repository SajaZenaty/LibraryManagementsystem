from abc import ABC, abstractmethod
class reservable(ABC):
    @abstractmethod
    def reserve(self,item_id, user_id):
        pass