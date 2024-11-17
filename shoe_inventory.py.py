import sqlite3
import tkinter as tk
from tkinter import messagebox

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('shoes_inventory.db')
cursor = conn.cursor()

# Create table if not already present
cursor.execute('''
    CREATE TABLE IF NOT EXISTS shoes (
        shoe_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        brand TEXT NOT NULL,
        shoe_type TEXT NOT NULL,
        price REAL NOT NULL
    )
''')
conn.commit()

# Function to add a shoe record
def add_record():
    shoe_id = entry_shoe_id.get()
    name = entry_name.get()
    brand = entry_brand.get()
    shoe_type = entry_shoe_type.get()
    price = entry_price.get()

    if shoe_id and name and brand and shoe_type and price:
        try:
            cursor.execute('''
                INSERT INTO shoes (shoe_id, name, brand, shoe_type, price)
                VALUES (?, ?, ?, ?, ?)
            ''', (shoe_id, name, brand, shoe_type, price))
            conn.commit()
            messagebox.showinfo("Success", "Record Added Successfully")
            clear_fields()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Shoe ID already exists.")
    else:
        messagebox.showerror("Error", "All fields are required!")

# Function to remove a shoe record
def remove_record():
    shoe_id = entry_shoe_id.get()

    if shoe_id:
        cursor.execute('DELETE FROM shoes WHERE shoe_id = ?', (shoe_id,))
        conn.commit()
        if cursor.rowcount > 0:
            messagebox.showinfo("Success", "Record Removed Successfully")
        else:
            messagebox.showerror("Error", "Shoe ID not found.")
        clear_fields()
    else:
        messagebox.showerror("Error", "Please enter a valid Shoe ID to remove.")

# Function to search for shoes based on advanced criteria
def search_records():
    search_criteria = entry_search.get()
    min_price = entry_min_price.get()
    max_price = entry_max_price.get()
    
    query = "SELECT * FROM shoes WHERE 1"
    params = []

    if search_criteria:
        query += " AND (name LIKE ? OR brand LIKE ? OR shoe_type LIKE ?)"
        params.extend([f"%{search_criteria}%", f"%{search_criteria}%", f"%{search_criteria}%"])

    if min_price:
        query += " AND price >= ?"
        params.append(min_price)

    if max_price:
        query += " AND price <= ?"
        params.append(max_price)

    cursor.execute(query, params)
    records = cursor.fetchall()
    
    listbox_records.delete(0, tk.END)
    if records:
        for record in records:
            listbox_records.insert(tk.END, f"ID: {record[0]}, Name: {record[1]}, Brand: {record[2]}, Type: {record[3]}, Price: {record[4]}")
    else:
        messagebox.showinfo("No Records", "No records found with the given search criteria.")

# Function to clear all input fields
def clear_fields():
    entry_shoe_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_brand.delete(0, tk.END)
    entry_shoe_type.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_search.delete(0, tk.END)
    entry_min_price.delete(0, tk.END)
    entry_max_price.delete(0, tk.END)

# Tkinter GUI setup
root = tk.Tk()
root.title("Shoe Inventory Management System")
root.geometry("700x600")  # Make the window wider and taller

# Labels and Entry Widgets
label_shoe_id = tk.Label(root, text="Shoe ID:")
label_shoe_id.grid(row=0, column=0, padx=15, pady=10, sticky="e")
entry_shoe_id = tk.Entry(root, width=40)
entry_shoe_id.grid(row=0, column=1, padx=15, pady=10)

label_name = tk.Label(root, text="Shoe Name:")
label_name.grid(row=1, column=0, padx=15, pady=10, sticky="e")
entry_name = tk.Entry(root, width=40)
entry_name.grid(row=1, column=1, padx=15, pady=10)

label_brand = tk.Label(root, text="Brand:")
label_brand.grid(row=2, column=0, padx=15, pady=10, sticky="e")
entry_brand = tk.Entry(root, width=40)
entry_brand.grid(row=2, column=1, padx=15, pady=10)

label_shoe_type = tk.Label(root, text="Shoe Type:")
label_shoe_type.grid(row=3, column=0, padx=15, pady=10, sticky="e")
entry_shoe_type = tk.Entry(root, width=40)
entry_shoe_type.grid(row=3, column=1, padx=15, pady=10)

label_price = tk.Label(root, text="Price:")
label_price.grid(row=4, column=0, padx=15, pady=10, sticky="e")
entry_price = tk.Entry(root, width=40)
entry_price.grid(row=4, column=1, padx=15, pady=10)

# Buttons for Adding, Removing, and Searching
button_add = tk.Button(root, text="Add Record", command=add_record, width=20)
button_add.grid(row=5, column=0, padx=15, pady=15)

button_remove = tk.Button(root, text="Remove Record", command=remove_record, width=20)
button_remove.grid(row=5, column=1, padx=15, pady=15)

label_search = tk.Label(root, text="Search (Name/Brand/Type):")
label_search.grid(row=6, column=0, padx=15, pady=10, sticky="e")
entry_search = tk.Entry(root, width=40)
entry_search.grid(row=6, column=1, padx=15, pady=10)

label_min_price = tk.Label(root, text="Min Price:")
label_min_price.grid(row=7, column=0, padx=15, pady=10, sticky="e")
entry_min_price = tk.Entry(root, width=40)
entry_min_price.grid(row=7, column=1, padx=15, pady=10)

label_max_price = tk.Label(root, text="Max Price:")
label_max_price.grid(row=8, column=0, padx=15, pady=10, sticky="e")
entry_max_price = tk.Entry(root, width=40)
entry_max_price.grid(row=8, column=1, padx=15, pady=10)

button_search = tk.Button(root, text="Search Records", command=search_records, width=20)
button_search.grid(row=9, column=0, columnspan=2, pady=15)

# Listbox to Display Records (for search results)
listbox_records = tk.Listbox(root, width=110, height=15)
listbox_records.grid(row=10, column=0, columnspan=2, padx=15, pady=10)

root.mainloop()

# Close the database connection at the end
conn.close()
