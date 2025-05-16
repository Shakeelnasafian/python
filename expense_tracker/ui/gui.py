import tkinter as tk
from tkinter import ttk, messagebox
from expense_tracker.models.expense import Expense
from expense_tracker.storage.database import create_table, insert_expense, fetch_all_expenses

class ExpenseTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        create_table()
        self.setup_widgets()
        self.refresh_expenses()

    def setup_widgets(self):
        frame = ttk.Frame(self.root, padding=10)
        frame.pack(fill='x')

        ttk.Label(frame, text="Name:").grid(row=0, column=0)
        self.name_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.name_var, width=40).grid(row=0, column=1, columnspan=3, sticky='ew')

        ttk.Label(frame, text="Amount:").grid(row=1, column=0)
        self.amount_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.amount_var, width=40).grid(row=1, column=1, columnspan=3, sticky='ew')

        ttk.Label(frame, text="Category:").grid(row=2, column=0)
        self.category_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.category_var, width=40).grid(row=2, column=1, columnspan=3, sticky='ew')

        ttk.Label(frame, text="Date:").grid(row=3, column=0)
        self.date_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.date_var, width=40).grid(row=3, column=1, columnspan=3, sticky='ew')

        ttk.Label(frame, text="Description:").grid(row=4, column=0)
        self.desc_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.desc_var, width=40).grid(row=4, column=1, columnspan=3, sticky='ew')

        ttk.Button(frame, text="Add Expense", command=self.add_expense).grid(row=5, column=0, columnspan=4, pady=5)

        self.tree = ttk.Treeview(self.root, columns=("Name", "Amount", "Category", "Date", "Description"), show='headings')
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.pack(fill='both', expand=True, padx=10, pady=10)

    def add_expense(self):
        try:
            exp = Expense(
                name=self.name_var.get(),
                amount=float(self.amount_var.get()),
                category=self.category_var.get(),
                date=self.date_var.get(),
                description=self.desc_var.get()
            )
            insert_expense(exp)
            self.refresh_expenses()
            self.name_var.set("")
            self.amount_var.set("")
            self.category_var.set("")
            self.date_var.set("")
            self.desc_var.set("")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def refresh_expenses(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for row in fetch_all_expenses():
            self.tree.insert("", "end", values=row[1:])

def main():
    root = tk.Tk()
    app = ExpenseTrackerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
