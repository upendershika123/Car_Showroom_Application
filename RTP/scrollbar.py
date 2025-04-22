import tkinter as tk
from tkinter import ttk

# Create the main application window
root = tk.Tk()
root.title("Treeview with Scrollbar Example")
root.geometry("400x300")

# Create the Treeview widget
tree = ttk.Treeview(root)
tree.place(x=0, y=0, width=380, height=280)  # Adjust the width and height as needed

# Create vertical scrollbar
vsb = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
vsb.place(x=380, y=0, height=280)  # Place to the right of the Treeview

# Create horizontal scrollbar
hsb = ttk.Scrollbar(root, orient="horizontal", command=tree.xview)
hsb.place(x=0, y=280, width=380)  # Place below the Treeview

# Configure the Treeview to use the scrollbars
tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

# Add some sample data to the Treeview
tree["columns"] = ("one", "two", "three")
tree.column("#0", width=100, minwidth=100)
tree.column("one", width=100, minwidth=100)
tree.column("two", width=100, minwidth=100)
tree.column("three", width=100, minwidth=100)

tree.heading("#0", text="Item")
tree.heading("one", text="Column 1")
tree.heading("two", text="Column 2")
tree.heading("three", text="Column 3")

for i in range(100):
    tree.insert("", "end", text=f"Item {i}", values=(f"Value {i}a", f"Value {i}b", f"Value {i}c"))

# Run the application
root.mainloop()
