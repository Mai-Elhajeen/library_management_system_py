from exceptions.item_not_found import ItemNotFoundError
from exceptions.user_not_found import UserNotFoundError
from exceptions.item_not_available import ItemNotAvailableError
from exceptions.item_already_reserved import ItemAlreadyReservedError


class Library:
    def __init__(self):
        self.items = []
        self.users = []
                
    def add_item(self, item):
        self.items.append(item)

    def add_user(self, user):
        self.users.append(user)

    def find_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        raise UserNotFoundError(f"User with ID {user_id} not found")

    def find_item_by_id(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                return item
        raise ItemNotFoundError(f"Item with ID {item_id} not found")
    
    def borrow_item(self, user_id, item_id):
        user = self.find_user_by_id(user_id)
        item = self.find_item_by_id(item_id)

        if item.reserved_by is not None and item.reserved_by != user_id:
            raise ItemAlreadyReservedError(f"Item with ID {item_id} is reserved by another user")

        if not item.is_available:
            raise ItemNotAvailableError(f"Item with ID {item_id} is not available for borrowing")
        
        item.is_available = False
        user.borrowed_items.append(item.item_id)

    def return_item(self, user_id, item_id):
        user = self.find_user_by_id(user_id)
        item = self.find_item_by_id(item_id)

        if item_id not in user.borrowed_items:
            raise Exception(f"User with ID {user_id} has not borrowed item with ID {item_id}")
        
        user.borrowed_items.remove(item_id)
        item.is_available = True
        item.reserved_by = None

    def reserve_item(self, user_id, item_id):
        user = self.find_user_by_id(user_id)
        item = self.find_item_by_id(item_id)

        if not hasattr(item, "reserve"):
            raise ItemNotAvailableError(f"Item with ID {item_id} cannot be reserved")

        item.reserve(user)