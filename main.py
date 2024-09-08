import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Pizza Order")

# Create entry boxes
person_name = tk.Entry(root, width=30)
person_name.grid(row=0, column=1, padx=20, pady=10)
pizza_type = tk.Entry(root, width=30)
pizza_type.grid(row=1, column=1, padx=20, pady=10)
n_slices = tk.Entry(root, width=30)
n_slices.grid(row=2, column=1, padx=20, pady=10)

root.mainloop()
