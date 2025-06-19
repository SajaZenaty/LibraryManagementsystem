class DuplicateUserError(Exception):
    def __init__(self, user_id):
        message = f"User with ID '{user_id}' already exists."
        super().__init__(message)
        
class UserNotFoundError(Exception):
    def __init__(self, user_id):
        message = f"User with ID '{user_id}' not found."
        super().__init__(message)
        
class ItemNotFoundError(Exception):
    def __init__(self, item_id):
        message = f"Item with ID '{item_id}' not found."
        super().__init__(message) 
        
class ItemNotAvailableError(Exception):
    def __init__(self, item_id):
        message = f"Item with ID '{item_id}' is not available for borrowing."
        super().__init__(message)
        
class EmptyUserIDError(Exception):
    def __init__(self):
        message = "User ID cannot be empty."
        super().__init__(message)
        
class EmptyUserNameError(Exception):
    def __init__(self):
        message = "User name cannot be empty."
        super().__init__(message)
        
class EmptyItemIDError(Exception):
    def __init__(self):
     message = "Item ID cannot be empty."
     super().__init__(message)
