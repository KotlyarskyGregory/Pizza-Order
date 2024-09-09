import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Pizza Order")
main_frame = tk.Frame(root, bg="lightblue", padx=10, pady=10)
main_frame.grid(row=4, column=0, columnspan=2)
submission_list = []

#Create submit function
def submit_func(name, topping, n_slices):
    # Add entries to dictionary
    submit_dic = {
        "name": name.get(),
        "topping": topping.get(),
        "slices": n_slices.get(),
    }
    submission_list.append(submit_dic)
    
    # Clear entries
    name.delete(0, tk.END)
    topping.delete(0, tk.END)
    n_slices.delete(0, tk.END)


def calculate_func():
    
    return


# Create entry boxes and labels
label_list = ["Name:", "Topping:", "Number of slices"]
entries = {}

for i, label_text in enumerate(label_list):
    # Create labels
    label = tk.Label(root, text=label_text)
    label.grid(row=i, column=0, padx=10, pady=5)
    
    # Create entry widget
    entry = tk.Entry(root, width=30)
    entry.grid(row=i, column=1, padx=5)

    # Store entry in a dictionary
    entries[label_text.lower().replace(" ", "_").strip(":")] = entry

# Create submit button
submit_btn = tk.Button(
    root, text="Submit", 
    command=lambda: submit_func(entries["name"], 
    entries["topping"], 
    entries["number_of_slices"])
    )
submit_btn.grid(row = 3, column=1)

# Create text boxes
root.mainloop()
