from models.library_item import LibraryItem
from models.reservable import Reservable

class DVD(LibraryItem, Reservable):
    def __init__(self, item_id, title, director, duration, is_available, reserved_by):
        super().__init__(item_id, title, is_available, reserved_by)
        self.director = director
        self.duration = duration
    
    def display_info(self):
        print(f"DVD-ID: {self.item_id}, Title: {self.title}, Duration: {self.duration} mins, Available: {self.is_available}")

    def reserve(self, user):
        if self.reserved_by:
            raise Exception("DVD already reserved")
        self.reserved_by = user.user_id