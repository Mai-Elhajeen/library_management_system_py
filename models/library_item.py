from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, item_id, title, is_available=True, reserved_by=None):
        self.item_id = item_id
        self.title = title
        self.is_available = is_available
        self.reserved_by = reserved_by
    
    @abstractmethod
    def display_info(self):
        pass

    def check_availability(self):
        return self.is_available
