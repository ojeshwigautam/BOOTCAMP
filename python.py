import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked!")

# Create the main application window
root = tk.Tk()
root.title("Tkinter Revision")

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!")
label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create a button widget
button = tk.Button(root, text="Click Me", command=on_button_click)
button.grid(row=1, column=0, padx=10, pady=10)

# Create an entry widget
entry = tk.Entry(root)
entry.grid(row=1, column=1, padx=10, pady=10)

# Create a text widget
text = tk.Text(root)
text.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
