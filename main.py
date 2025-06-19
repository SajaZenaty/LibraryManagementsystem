import json
from models.Library import library  
from models.Book import book
from models.DVD import dvd
from models.Magazine import magazine
from models.User import user
from exceptions.user_exceptions import DuplicateUserError, EmptyItemIDError , UserNotFoundError, ItemNotFoundError
from exceptions.user_exceptions import ItemNotAvailableError, EmptyUserIDError, EmptyUserNameError


      
# Initialize the library with the name and address
library_name = 'GSG Library'
library_address = 'AlRemal, Gaza, Palestine'
my_library = library(library_name, library_address)
        
def main():
  
      print ('Welcome to the Library Management System')
      print('1. View all available items')
      print('2. Search item by title or type')
      print('3. Register new user')
      print('4. Borrow an item')
      print('5. Reserve an item')
      print('6. Return an item')
      print('7. Remove an item ')
      print('8. Remove a user')
      print('9. Exit and Save')

      choice = int(input('Please enter your choice (1-9): '))
      
      while choice != 9:
          if choice == 1:
              my_library.view_available_items()
              
          elif choice == 2:
              search_term = input("Enter title or type to search: ").strip().lower()
              my_library.search_item(search_term)
              
          elif choice == 3:
               try:
                 user_id = input("Enter your user ID: ").strip().title()
                 user_name = input("Enter your user name: ").strip().title()

                 if not user_id:
                   raise EmptyUserIDError()
                 if not user_name:
                   raise EmptyUserNameError()
                  
                 new_user = user(user_id, user_name)
                 my_library.add_user(new_user)

               except (EmptyUserIDError, EmptyUserNameError, DuplicateUserError) as e:
                   print(e)


          elif choice == 4:
                
                try:
                 item_id = input("Enter the item ID to borrow: ").strip().title()
                 user_id = input("Enter your user ID: ").strip().title()
                
                 if  not item_id:
                   raise EmptyItemIDError()
                 
                 if not user_id:
                   raise EmptyUserIDError()
                 
                 my_library.borrow_item(item_id, user_id)
                 
                except (EmptyItemIDError, EmptyUserIDError,
                        DuplicateUserError,ItemNotAvailableError,
                        UserNotFoundError) as e:
                   print(e)
            
                  
                
          elif choice == 5:
            try:
                item_id = input("Enter the item ID to reserve: ").strip().title()
                user_id = input("Enter your user ID: ").strip().title()
                
                if not item_id:
                   raise EmptyItemIDError()
                 
                if not user_id:
                  raise EmptyUserIDError()
                  
                my_library.reserve(item_id, user_id)
                
            except (EmptyItemIDError, EmptyUserIDError, ItemNotFoundError, UserNotFoundError) as e:
                print(e)

          elif choice == 6:
            try:
                item_id = input("Enter the item ID to return: ").strip().title()
                user_id = input("Enter your user ID: ").strip().title()
                
                if  not item_id:
                   raise EmptyItemIDError()
                 
                if not user_id:
                   raise EmptyUserIDError()
                 
                my_library.return_item(item_id, user_id)
                
            except (EmptyItemIDError, EmptyUserIDError ,UserNotFoundError) as e:
                 print(e)
                
                
          elif choice == 7:
            try:
                item_id = input("Enter the item ID to remove: ").strip().title()
                if not item_id:
                   raise EmptyItemIDError()
                my_library.remove_item(item_id)
            except(ItemNotFoundError,EmptyItemIDError) as e:
                print(e)
                
          elif choice == 8:
            try :
                user_id = input("Enter the user ID to remove: ").strip().title()
                if not user_id:
                   raise EmptyUserIDError()
                my_library.remove_user(user_id)
                
            except(UserNotFoundError,EmptyUserIDError) as e:
              print(e)
          else:
                print("\n❗ Invalid choice. Please enter a number between 1 and 9.\n")
          choice = int(input('Please enter your choice (1-9): '))
        
if __name__== "__main__":
    main()          
              

          
        
        




  



    
 
 