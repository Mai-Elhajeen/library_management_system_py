# 📚 Library Management System (OOP Python Project)

## 📖 Overview

This project is a **Command-Line Library Management System** developed using **Object-Oriented Programming (OOP)** principles in Python.

The system simulates real-world library operations such as:

* Managing different types of library items
* Registering users
* Borrowing, returning, and reserving items
* Persisting data using JSON files

This project was built as a practical implementation of **abstraction, interfaces, exception handling, and custom class design**.

---

## 🎯 Objectives

* Apply **OOP Design Concepts** in a real application.
* Use **Abstract Base Classes** to model shared behavior.
* Implement an **interface-like structure** using abstract methods.
* Handle errors using **custom exceptions**.
* Read and write system state using **JSON persistence**.
* Build a modular, maintainable Python application.

---

## 🏗️ Project Structure

```
library_management_system_py/
│
├── main.py                  # Application entry point (CLI interface)
│
├── models/
│   ├── library_item.py      # Abstract base class
│   ├── reservable.py        # Interface-like abstract class
│   ├── book.py              # Book implementation
│   ├── dvd.py               # DVD implementation
│   ├── magazine.py          # Magazine implementation
│   ├── user.py              # User model
│   └── library.py           # Core system logic
│
├── utils/
│   └── file_handler.py      # JSON loading & saving utilities
│
├── exceptions/
│   ├── item_not_found.py
│   ├── user_not_found.py
│   ├── item_not_available.py
│   └── item_already_reserved.py
│
├── data/
│   ├── items.json           # Stored library items
│   └── users.json           # Stored users
│
└── README.md
```

---

## 🧠 OOP Concepts Implemented

### ✅ Abstraction

`LibraryItem` is an abstract class that defines shared attributes and behavior for all items.

```python
class LibraryItem(ABC):
    @abstractmethod
    def display_info(self):
        pass
```

---

### ✅ Interface (via Abstract Class)

`Reservable` ensures only specific items can be reserved.

```python
class Reservable(ABC):
    @abstractmethod
    def reserve(self, user):
        pass
```

Implemented only by:

* `Book`
* `DVD`

---

### ✅ Inheritance & Specialization

Each item type extends the base class with its own fields:

| Type     | Additional Attributes |
| -------- | --------------------- |
| Book     | author, genre         |
| DVD      | director, duration    |
| Magazine | publisher, issue      |

---

### ✅ Encapsulation of Business Logic

All operations are handled through the `Library` class:

* User lookup
* Item lookup
* Borrowing validation
* Reservation rules
* Returning items

---

### ✅ Exception Handling

Custom exceptions enforce system rules:

* User not found
* Item not found
* Borrowing unavailable items
* Reserving already reserved items

---

### ✅ Data Persistence (JSON-Based)

System loads initial state from:

```
data/items.json
data/users.json
```

And **automatically saves updates** when exiting.

---

## ⚙️ Features

✔ View available items

✔ Search by title or type

✔ Register new users

✔ Borrow items

✔ Reserve supported items

✔ Return borrowed items

✔ Data saved automatically on exit

✔ Prevent borrowing items reserved by another user

✔ Robust error handling

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Mai-Elhajeen/library_management_system_py.git
cd library_management_system_py
```

### 2️⃣ Run the Application

```bash
python main.py
```

---

## 💻 Example Menu

```
Welcome to the Library System
1. View all available items
2. Search item by title or type
3. Register as a new user
4. Borrow an item
5. Reserve an item
6. Return an item
7. Exit and Save
```

---

## 🔐 Business Rules Enforced

* An item cannot be borrowed if:

  * It is unavailable
  * It is reserved by another user
* Only reservable items (Book/DVD) can be reserved.
* Returning an item clears its reservation.
* IDs are used for internal consistency instead of titles.

---

## 📦 Technologies Used

* Python 3
* OOP (ABC, Inheritance, Polymorphism)
* JSON for lightweight persistence
* CLI-based interaction

---

## 👩‍💻 Author

Developed as part of a hands-on learning project to strengthen:

* Software design thinking
* Clean architecture practices
* Real-world OOP implementation

---

## 📜 License

This project is for educational purposes.
