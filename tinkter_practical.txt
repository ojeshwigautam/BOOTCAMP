import tkinter as tk
from tkinter import messagebox

def show_dialog(dialog_type):
    if dialog_type == "info":
        messagebox.showinfo("Information", "This is an information dialog")
    elif dialog_type == "warning":
        messagebox.showwarning("Warning", "This is a warning dialog")
    elif dialog_type == "error":
        messagebox.showerror("Error", "This is an error dialog")
    elif dialog_type == "question":
        result = messagebox.askquestion("Question", "Do you want to proceed?")
        if result == 'yes':
            messagebox.showinfo("Response", "You chose to proceed")
        else:
            messagebox.showinfo("Response", "You chose not to proceed")

root = tk.Tk()
root.title("Dialog Box Example")
root.geometry("400x300")

def clear_text():
    text.delete(1.0, tk.END)

def get_text():
    return text.get(1.0, tk.END)

def insert_text():
    current_text = get_text()
    new_text = "This is new text.\n"
    text.insert(tk.END, new_text)

def delete_text():
    text.delete(tk.SEL_FIRST, tk.SEL_LAST)

text_frame = tk.Frame(root)
text_frame.pack(fill=tk.BOTH, expand=True)

text = tk.Text(text_frame, wrap=tk.WORD)
text.pack(fill=tk.BOTH, expand=True)

edit_frame = tk.Frame(root)
edit_frame.pack()

clear_button = tk.Button(edit_frame, text="Clear Text", command=clear_text)
clear_button.pack(side=tk.LEFT, padx=5, pady=5)

insert_button = tk.Button(edit_frame, text="Insert Text", command=insert_text)
insert_button.pack(side=tk.LEFT, padx=5, pady=5)

delete_button = tk.Button(edit_frame, text="Delete Selected Text", command=delete_text)
delete_button.pack(side=tk.LEFT, padx=5, pady=5)

dialog_types = ["info", "warning", "error", "question"]
for dialog_type in dialog_types:
    button = tk.Button(root, text=f"Show {dialog_type.capitalize()}", 
                       command=lambda dialog_type=dialog_type: show_dialog(dialog_type))
    button.pack(pady=5)

root.mainloop()
