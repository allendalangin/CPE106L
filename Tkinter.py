import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        label_file.config(text=f"Selected File: {file_path}")
        with open(file_path, "r") as file:
            text_box.delete("1.0", tk.END)
            text_box.insert(tk.END, file.read())

# Create main window
root = tk.Tk()
root.title("File Dialog Example")

# Button to open file
btn_open = tk.Button(root, text="Open File", command=open_file)
btn_open.pack(pady=10)

# Label to show selected file
label_file = tk.Label(root, text="No file selected")
label_file.pack(pady=5)

# Text box to display file content
text_box = tk.Text(root, wrap=tk.WORD, height=15, width=50)
text_box.pack(pady=10)

root.mainloop()