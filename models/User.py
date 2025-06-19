class user:
    def __init__(self, user_id, name, borrowed_items=None):
        self.user_id = user_id
        self.name = name
        self.borrowed_items = borrowed_items if borrowed_items is not None else []



    def __repr__(self):
        return f"User({self.user_id}, {self.name}, {self.email})"