# Shoe Inventory Management System

A Python-based application for managing a shoe inventory using **SQLite** as the database and **Tkinter** for the graphical user interface (GUI). This system allows users to easily add, remove, search, and manage shoe records in a structured and efficient way. The application provides advanced search functionality, allowing users to search by shoe ID, name, brand, type, and price range.

## Features

- **Add Records**:
  - Add shoe records with details such as ID, name, brand, type, and price.
  - Data is stored securely in an SQLite database, ensuring data integrity and efficient querying.

- **Remove Records**:
  - Remove existing shoe records by entering the Shoe ID.
  - The system checks if the Shoe ID exists and removes the record if found.

- **Search Records**:
  - Search for shoes by ID, name, brand, or type.
  - Advanced search options allow users to filter results based on a price range, enhancing the search experience.

- **Graphical User Interface (GUI)**:
  - Developed with **Tkinter**, the GUI provides an intuitive and user-friendly interface for interacting with the inventory system.
  - Easy-to-use input fields for entering shoe details, removing records, and displaying search results.

- **SQLite Database**:
  - The system uses an **SQLite** database for storing and retrieving shoe records. It ensures fast data processing and scalability for larger datasets.
  - The database supports operations such as adding, displaying, searching, and removing records.

## Requirements

- Python 3.x
- SQLite (included with Python)
- Tkinter (included with Python)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/YourUsername/Shoe-Inventory-System.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Shoe-Inventory-System
    ```

3. Run the application:
    ```bash
    python shoe_inventory.py
    ```

The application will open a GUI window where you can begin adding, searching, and removing shoe records.

## Usage

- **Add a Record**: Enter the shoe details (ID, name, brand, type, and price) and click "Add Record" to store it in the database.
- **Remove a Record**: Enter the Shoe ID of the record you want to remove and click "Remove Record." The record will be deleted from the database if found.
- **Search for Records**: Use the search bar to filter records by shoe ID, name, brand, type, or price range.
- **View Results**: Search results will be displayed in a list, showing the shoe's ID, name, brand, type, and price.
