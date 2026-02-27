from models.library_item import LibraryItem

class Magazine(LibraryItem):
    def __init__(self, item_id, title, issue, publisher, is_available, reserved_by):
        super().__init__(item_id, title, is_available, reserved_by)
        self.publisher = publisher
        self.issue = issue
    
    def display_info(self):        
        print(f"Magazine-ID: {self.item_id}, Title: {self.title}, Publisher: {self.publisher}, Issue Number: {self.issue}, Available: {self.is_available}")
