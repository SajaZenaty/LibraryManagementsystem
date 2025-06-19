from models.Reservable import reservable
from models.User import user
import json 
from exceptions.user_exceptions import DuplicateUserError
from models.Book import book
from models.DVD import dvd
from models.Magazine import magazine
from exceptions.user_exceptions import DuplicateUserError, UserNotFoundError, ItemNotFoundError
from exceptions.user_exceptions import ItemNotAvailableError


class library(reservable):

    def __init__(self, name, address ):
        self.name = name
        self.address = address
        
# Define the paths to the JSON files for users and items

    users_path= '/Users/macbookanan/Desktop/Machine learning/GSG-skillPath/LibraryManagementSystem/data/users.json'
    items_path= '/Users/macbookanan/Desktop/Machine learning/GSG-skillPath/LibraryManagementSystem/data/items.json'

#Read and write methods for users and items JSON files

    def read_users_file(self):
        try:
            with open(self.users_path, 'r') as file:
                users = json.load(file)
            return users
        except (json.JSONDecodeError, FileNotFoundError):
            return []
        
    def write_users_file(self, users):
        with open(self.users_path, 'w') as file:
            json.dump(users, file, indent=2)   

    def read_items_file(self):
        try:
            with open(self.items_path, 'r') as file:
                items = json.load(file)
            return items
        except (json.JSONDecodeError, FileNotFoundError):
            return []
        
    def write_items_file(self, items):
        with open(self.items_path, 'w') as file:
            json.dump(items, file, indent=2) 


   
# Add a new user to the library
    def add_user(self, user):
       new_user = {
        'user_id': user.user_id,
        'name': user.name,
        'borrowed_items': user.borrowed_items
    }
       users = self.read_users_file()
       for existing_user in users:
          if existing_user['user_id'] == new_user['user_id']:
            raise DuplicateUserError(new_user['user_id'])

    
       users.append(new_user)
       self.write_users_file(users)
       print(f"User {new_user['user_id']} registered successfully.")

        

#Remove an item from library           
    def borrow_item(self, item_id, user_id):
        items = self.read_items_file()
        users = self.read_users_file()

        item = None
        for i in items:
            if i['id'] == item_id:
                item = i
                break

        if item is None:
            raise ItemNotFoundError(item_id)

        borrowed_ids = set()
        for user in users:
            borrowed_ids.update(user['borrowed_items'])

        if item_id in borrowed_ids:
            raise ItemNotAvailableError(item_id)

        found_user = None
        for u in users:
            if u['user_id'] == user_id:
                found_user = u
                break

        if found_user is None:
            raise UserNotFoundError(user_id)

        reservation_queue = item.get("reservation_queue", [])

        if reservation_queue:
            if reservation_queue[0] != user_id:
                if user_id not in reservation_queue:
                    response = input(f"❌ Item '{item['title']}' is reserved by another user. You are not in the reservation queue.\nDo you want to be added to the reservation queue? (y/n): ").strip().lower()
                    if response == 'y':
                        reservation_queue.append(user_id)
                        item["reservation_queue"] = reservation_queue
                        self.write_items_file(items)
                        print(f"ℹ️ User {user_id} added to the reservation queue of item '{item['title']}'.")
                    else:
                        print("You chose not to join the reservation queue.")
                else:
                    print(f"❌ Item '{item['title']}' is reserved by another user. You must wait for your turn.")
                return

        found_user['borrowed_items'].append(item_id)
        self.write_users_file(users)

        if user_id in reservation_queue:
            reservation_queue.remove(user_id)
            item["reservation_queue"] = reservation_queue
            print(f"ℹ️ User {user_id} removed from reservation queue of item '{item['title']}'.")

        self.write_items_file(items)

        print(f"✅ Item '{item['title']}' borrowed successfully by {found_user['name']}.")



                    
                                
           
# Return an item to the library
    def return_item(self, item_id, user_id):
        users = self.read_users_file()
        user_found = False
        
        for user in users:
            if user['user_id'] == user_id:
                user_found=True
                if item_id in user['borrowed_items']:
                    user['borrowed_items'].remove(item_id)
                    self.write_users_file(users)
                    print(f"Item with ID {item_id} returned successfully by {user['name']}.")
                    
                else:
                    print(f"Item with ID {item_id} was not borrowed by {user['name']}.")
                break 
               
            if not user_found:
                raise UserNotFoundError(user_id)
                    
                
        
# Reserve an item in the library
    def  reserve(self, item_id, user_id):
        items=self.read_items_file()
        users=self.read_users_file()
        user_found = False
        item_found= False
        
        for user in users:
            if user['user_id'] == user_id:
                user_found = True
                break
        for item in items:
                if item['id']==item_id:
                    if item['type']=='Magazine':
                       print("❌ You can't reserve a Magazine item!")
                       item_found=True
                       break
                    else:
                        item_found = True
                        item.setdefault("reservation_queue", [])
                        if user_id in item['reservation_queue']:
                                print(f"User {user_id} has already reserved this item.")
                        else:
                            item['reservation_queue'].append(user_id)
                            self.write_items_file(items)
                            print(f"Item {item['title']} reserved successfully by user {user_id}.")
                        break
            
        if not user_found:
            raise UserNotFoundError(user_id)
        
        if not item_found:
            raise ItemNotFoundError(item_id)
        
    
#View all available items in the library
    def view_available_items(self):
        items = self.read_items_file()
        users = self.read_users_file()

        borrowed_items_id = set()
        for user in users:
            borrowed_items_id.update(user['borrowed_items'])
            
        items_obj=[]
        for item in items:
            if item['type']=='Book':
                items_obj.append(book(item['title'], item['author'], item['isbn'], item['id']))
                
            elif item['type']=='DVD':
                items_obj.append(dvd(item['title'], item['author'], item['release_year'], item['id']))
                
            elif item['type']=='Magazine':
                items_obj.append(magazine(item['title'], item['author'], item['issue_number'], item['id']))
                
            else:
                print(f"Unknown item type: {item['type']}")
                
        
        available_items = []
        borrowed_items = []

        for item in items_obj:
            if item.check_availability(borrowed_items_id):
                available_items.append(item)
            else:
                borrowed_items.append(item)

    
        print("\n=== 📚 Available Items ===")
        if available_items:
            for item in available_items:
                print(item.display_info())
                print("-" * 40)
        else:
            print("No items are currently available.")

        print("\n=== 🔒 Borrowed Items ===")
        if borrowed_items:
            for item in borrowed_items:
                print(f"{item.title} is currently borrowed.")
        else:
            print("No items are currently borrowed.")
            
        
        
#Search an item by type or name .

    def search_item(self, search_term):
        items = self.read_items_file()
        search_results = [item for item in items if search_term in item['title'].lower() or search_term in item['type'].lower()]
        
        if not search_results:
            print("No items found.")
            return 
        
        print(f"\n🔍 Search Results for '{search_term}':\n")
        
        for item in search_results:
               if item['type'] == 'Book':
                    item_obj = book(item['title'], item['author'], item['isbn'], item['id'])
               elif item['type'] == 'DVD':
                    item_obj = dvd(item['title'], item['author'], item['release_year'], item['id'])
               elif item['type'] == 'Magazine':
                    item_obj = magazine(item['title'], item['author'], item['issue_number'], item['id'])
               else:
                    print(f"Unknown item type: {item['type']}")
                    continue        
               print(item_obj.display_info())
    

