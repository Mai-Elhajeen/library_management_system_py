from models.library_item import LibraryItem
from models.reservable import Reservable
from exceptions.item_already_reserved import ItemAlreadyReservedError

class Book(LibraryItem, Reservable):
    def __init__(self, item_id, title, author, genre, is_available, reserved_by):
        super().__init__(item_id, title, is_available, reserved_by)
        self.author = author
        self.genre = genre

    def display_info(self):
        print(f"Book-ID: {self.item_id}, Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Available: {self.is_available}")
    
    def reserve(self, user):
        if self.reserved_by is not None:
            raise ItemAlreadyReservedError("Book already reserved")
        self.reserved_by = user.user_id