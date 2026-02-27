import sys
import os
from models.library import Library
from models.user import User
from utils.file_handler import load_users, load_items, save_users, save_items

ITEMS_FILE = os.path.join("data", "items.json")
USERS_FILE = os.path.join("data", "users.json")

class Main:
    def __init__(self):
        self.library = Library()

    def menu(self):
        print("""Welcome to the Library System
    1. View all available items
    2. Search item by title or type
    3. Register as a new user
    4. Borrow an item
    5. Reserve an item
    6. Return an item
    7. Exit and Save
""")
        choice = input("Enter your choice: ")
        try: 
            choice = int(choice)
            return choice
        except ValueError:
            print("Invalid input. Please enter a number.")
            print("*" * 30 + "Try again" + "*" * 30)
        return -1

    def view_all_available_items(self):
        for item in self.library.items:
            if item.is_available:
                item.display_info()

    def search_item(self):
        keyword= input("Enter a keyword to search (title or type): ")
        found_items = []
        for item in self.library.items:
            if keyword.lower() in item.title.lower() or keyword.lower() in type(item).__name__.lower():
                found_items.append(item)
        if found_items:
            print(f"{"*"*30}Found {len(found_items)} item(s) matching '{keyword}'{"*"*30}")
            for item in found_items:
                item.display_info()
            else:
                print(f"No items found matching '{keyword}'.")

    def register_user(self):
        name= input("Enter username: ")
        new_id= len(self.library.users) + 1
        new_user = User(user_id=new_id, name=name)
        self.library.add_user(new_user)
        print("User registered successfully with ID:", new_id)

    def borrow_item(self):
        try:
            u_id = int(input("Enter your user ID: "))
            itm_id = int(input("Enter the item ID you want to borrow: "))

            self.library.borrow_item(u_id, itm_id)
            print("Item borrowed successfully.")

        except Exception as e:
            print(f"Error: {e}")

    def reserve_item(self):
        try:
            u_id = int(input("Enter your user ID: "))
            itm_id = int(input("Enter the item ID you want to reserve: "))

            self.library.reserve_item(u_id, itm_id)
            print("Item reserved successfully.")

        except Exception as e:
            print(f"Error: {e}")        

    def return_item(self):
        try:
            u_id = int(input("Enter your user ID: "))
            itm_id = int(input("Enter the item ID you want to return: "))

            self.library.return_item(u_id, itm_id)
            print("Item returned successfully.")

        except Exception as e:
            print(f"Error: {e}")

    def exit_and_save(self):
        save_items(self.library.items, ITEMS_FILE)
        save_users(self.library.users, USERS_FILE)
        print("Data saved. Exiting the program.")

    def run(self):
        self.library.items = load_items(ITEMS_FILE)
        self.library.users = load_users(USERS_FILE)
    
        while True:
            choice = self.menu()

            if choice == 1:
                self.view_all_available_items()
            elif choice == 2:
                self.search_item()
            elif choice == 3:
                self.register_user()
            elif choice == 4:
                self.borrow_item()
            elif choice == 5:
                self.reserve_item()
            elif choice == 6:
                self.return_item()
            elif choice == 7:
                self.exit_and_save()
                break
            else:
                print("Invalid Choice.")

if __name__ == "__main__":
    main = Main()
    code = main.run()
    sys.exit(code)