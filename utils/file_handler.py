import json
from models.book import Book
from models.dvd import DVD
from models.magazine import Magazine
from models.user import User

def load_items(file_path):
    try:
        with open(file_path, 'r') as file:
            items_data = json.load(file)

        items = []
        for item in items_data:
            item_type = item.get("type")
            item_data = {k: v for k, v in item.items() if k != "type"}
            if item_type == 'Book':
                obj = Book(**item_data)
            elif item_type == 'DVD':
                obj = DVD(**item_data)
            elif item_type == 'Magazine':
                obj = Magazine(**item_data)
            else:
                print(f"Unknown item type: {item_type}")
                continue
            items.append(obj)
        return items
    
    except FileNotFoundError:
        print(f"File {file_path} not found.")

    except json.JSONDecodeError:
        print(f"Invalid JSON format in file {file_path}.")

    except IOError:
        print(f"An error occurred while reading the file {file_path}.")

    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

    return []

def load_users(file_path):
    try:
        with open(file_path, 'r') as file:
            users_data = json.load(file)

        users = [User(**user) for user in users_data]
        return users
    
    except FileNotFoundError:
        print(f"File {file_path} not found.")

    except json.JSONDecodeError:
        print(f"Invalid JSON format in file {file_path}.")

    except IOError:
        print(f"An error occurred while writing to the file {file_path}.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

    return []


def save_items(items, file_path):
    try:
        data = []
        for item in items:
            item_dict = item.__dict__.copy()
            item_dict['type'] = item.__class__.__name__
            data.append(item_dict)

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        
    except IOError:
        print(f"An error occurred while writing to the file {file_path}.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")


def save_users(users, file_path):
    try:
        users_data = [user.__dict__ for user in users]

        with open(file_path, 'w') as file:
            json.dump(users_data, file, indent=4)

    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
